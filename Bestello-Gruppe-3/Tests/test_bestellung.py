import pytest

from Bestelo.Bestellungen import Bestellposition, Bestellung
from Bestelo.Kunden import Geschaeftskunde, Kunde
from Bestelo.Produkte import Produkt


def test_bestellposition() -> None:
    """Prüft Positionsbeträge, Darstellung und ungültige Mengen."""
    kaffee = Produkt("P-1001", "Kaffeebohnen 500 g", 8.90, "Lebensmittel")
    position = Bestellposition(kaffee, 3)

    assert position.netto == pytest.approx(26.70)
    assert position.mwst == pytest.approx(1.87)
    assert position.brutto == pytest.approx(28.57)
    assert str(position) == "3 × Kaffeebohnen 500 g à 8.90 € = 26.70 €"

    with pytest.raises(ValueError):
        position.menge = 0

    with pytest.raises(ValueError):
        position.menge = 1.5

    with pytest.raises(AttributeError):
        position.produkt = kaffee


def test_bestellung_summen_und_zusammenfassen() -> None:
    """Prüft das Rechenbeispiel und das Zusammenfassen gleicher Artikel."""
    kunde = Geschaeftskunde(
        1002, "Ben Schmidt", "ben@example.com",
        "Schmidt IT GmbH", "DE123456789"
    )
    kaffee = Produkt("P-1001", "Kaffeebohnen 500 g", 8.90, "Lebensmittel")
    wasser = Produkt("P-1002", "Mineralwasser", 7.50, "Getränke")

    bestellung = Bestellung(kunde)
    bestellung.hinzufuegen(kaffee, 2)
    bestellung.hinzufuegen(wasser, 6)
    bestellung.hinzufuegen(kaffee)

    assert len(bestellung) == 2
    assert bestellung.positionen[0].menge == 3
    assert bestellung.netto_summe == pytest.approx(71.70)
    assert bestellung.rabatt_betrag == pytest.approx(2.15)
    assert bestellung.netto_nach_rabatt == pytest.approx(69.55)
    assert bestellung.mwst_betrag == pytest.approx(10.11)
    assert bestellung.brutto_summe == pytest.approx(79.66)

    assert str(bestellung) == (
        f"Bestellung {bestellung.bestellnummer} (offen) "
        "für Ben Schmidt: 2 Position(en), 79.66 € brutto"
    )


def test_bestellnummern_und_listenkopie() -> None:
    """Prüft fortlaufende Nummern und den Schutz der internen Liste."""
    kunde = Kunde(1001, "Anna", "anna@example.com")
    erste = Bestellung(kunde)
    zweite = Bestellung(kunde)

    nummer_1 = int(erste.bestellnummer.split("-")[1])
    nummer_2 = int(zweite.bestellnummer.split("-")[1])

    assert nummer_2 == nummer_1 + 1

    erste.hinzufuegen(Produkt("P-1001", "Kaffee", 8.90))
    kopie = erste.positionen
    kopie.clear()

    assert len(erste) == 1


def test_bestellung_abschliessen() -> None:
    """Prüft leere, abgeschlossene und wiederholt abgeschlossene Bestellungen."""
    kunde = Kunde(1001, "Anna", "anna@example.com")
    produkt = Produkt("P-1001", "Kaffee", 8.90)
    bestellung = Bestellung(kunde)

    with pytest.raises(ValueError):
        bestellung.abschliessen()

    with pytest.raises(ValueError):
        bestellung.hinzufuegen(produkt, 0)

    bestellung.hinzufuegen(produkt)
    bestellung.abschliessen()

    assert bestellung.status == "abgeschlossen"

    bestellung.abschliessen()
    assert bestellung.status == "abgeschlossen"

    with pytest.raises(ValueError):
        bestellung.hinzufuegen(produkt)