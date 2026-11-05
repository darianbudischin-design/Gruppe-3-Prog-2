"""Tests für Mengen, Status und die Kontrollbeträge aus dem Aufgabenblatt."""

import pytest

from bestelo.bestellungen import Bestellposition, Bestellung
from bestelo.kunden import Geschaeftskunde, Kunde
from bestelo.produkte import Produkt


def test_position_berechnet_betraege() -> None:
    p = Bestellposition(Produkt("P-1001", "Kaffee", 8.90, "Lebensmittel"), 3)
    assert (p.netto, p.mwst, p.brutto) == (26.70, 1.87, 28.57)
    assert str(p) == "3 × Kaffee à 8.90 € = 26.70 €"
    # Dieser Testabschnitt besteht, wenn genau der erwartete Fehlertyp auftritt.
    with pytest.raises(ValueError):
        p.menge = 0


def test_mischbestellung_und_rabatt() -> None:
    firma = Geschaeftskunde(1002, "Ben", "b@example.de", "IT GmbH", "DE123456789")
    b = Bestellung(firma)
    b.hinzufuegen(Produkt("P-1001", "Kaffee", 8.90, "Lebensmittel"), 3)
    b.hinzufuegen(Produkt("P-1002", "Wasser", 7.50, "Getränke"), 6)
    assert (b.netto_summe, b.rabatt_betrag, b.netto_nach_rabatt,
            b.mwst_betrag, b.brutto_summe) == (71.70, 2.15, 69.55, 10.11, 79.66)


def test_artikel_zusammenfassen() -> None:
    b = Bestellung(Kunde(1001, "Anna", "a@example.de"))
    p = Produkt("P-1001", "Kaffee", 8.90)
    b.hinzufuegen(p, 2)
    b.hinzufuegen(Produkt("P-1001", "Kaffee", 8.90))
    with pytest.raises(ValueError):
        b.hinzufuegen(p, -1)
    assert len(b) == 1
    assert b.positionen[0].menge == 3
    b.positionen.clear()
    assert len(b) == 1


def test_abschlussregeln() -> None:
    b = Bestellung(Kunde(1001, "Anna", "a@example.de"))
    assert b.status == "offen"
    with pytest.raises(ValueError):
        b.abschliessen()
    p = Produkt("P-1001", "Kaffee", 8.90)
    b.hinzufuegen(p)
    b.abschliessen()
    b.abschliessen()
    assert b.status == "abgeschlossen"
    with pytest.raises(ValueError):
        b.hinzufuegen(p)


def test_bestellnummer_fortlaufend() -> None:
    kunde = Kunde(1001, "Anna", "a@example.de")
    erste, zweite = Bestellung(kunde), Bestellung(kunde)
    assert zweite.bestellnummer == f"B-{int(erste.bestellnummer[2:]) + 1:04d}"


def test_nur_lesbare_bestelleigenschaften() -> None:
    """Die öffentlichen Properties verhindern direkte Zuweisungen."""
    kunde = Kunde(1001, "Anna", "a@example.de")
    produkt = Produkt("P-1001", "Kaffee", 8.90)
    b = Bestellung(kunde)
    position = Bestellposition(produkt)
    for objekt, name, wert in (
        (b, "bestellnummer", "B-9999"),
        (b, "kunde", kunde),
        (b, "status", "abgeschlossen"),
        (b, "positionen", []),
        (position, "produkt", produkt),
    ):
        with pytest.raises(AttributeError):
            setattr(objekt, name, wert)


def test_leere_bestellung_und_standardmenge() -> None:
    """Eine neue Bestellung startet leer; die Standardmenge beträgt eins."""
    b = Bestellung(Kunde(1001, "Anna", "a@example.de"))
    assert len(b) == 0
    assert (b.netto_summe, b.rabatt_betrag, b.netto_nach_rabatt,
            b.mwst_betrag, b.brutto_summe) == (0.0, 0.0, 0.0, 0.0, 0.0)
    assert b.hinzufuegen(Produkt("P-1001", "Kaffee", 8.90)) is None
    assert b.positionen[0].menge == 1
    assert b.abschliessen() is None
    assert b.abschliessen() is None
