from pathlib import Path

import pytest

from Bestelo.Produkte import Produkt


CSV_PFAD = (
    Path(__file__).resolve().parents[1]
    / "Bestelo"
    / "Daten"
    / "Produkte.csv"
)


def test_produkt_preise_und_steuer() -> None:
    """Prüft beide Steuersätze und die gerundeten Bruttopreise."""
    kaffee = Produkt("P-1001", "Kaffeebohnen 500 g", 8.90, "Lebensmittel")
    wasser = Produkt("P-1002", "Mineralwasser", 7.50, "Getränke")

    assert kaffee.mwst_satz == pytest.approx(0.07)
    assert kaffee.bruttopreis == pytest.approx(9.52)

    assert wasser.mwst_satz == pytest.approx(0.19)

    # Python rundet dieses float-Ergebnis auf 8.92, wie in der PDF beschrieben.
    assert wasser.bruttopreis == pytest.approx(8.92)


def test_produkt_ungueltige_angaben() -> None:
    """Prüft ungültige Produktdaten und die nur lesbare Artikelnummer."""
    with pytest.raises(ValueError):
        Produkt("1001", "Kaffee", 8.90)

    with pytest.raises(ValueError):
        Produkt("P-1001", " ", 8.90)

    with pytest.raises(ValueError):
        Produkt("P-1001", "Kaffee", 0)

    with pytest.raises(ValueError):
        Produkt("P-1001", "Kaffee", 8.90, "Unbekannt")

    produkt = Produkt("P-1001", "Kaffee", 8.90)

    with pytest.raises(AttributeError):
        produkt.artikelnummer = "P-9999"


def test_produkt_csv_zeile_und_darstellung() -> None:
    """Prüft die Erzeugung aus einer Datenzeile."""
    produkt = Produkt.aus_csv_zeile(
        "P-1001;Kaffeebohnen 500 g;8.90;Lebensmittel\n"
    )

    assert produkt.artikelnummer == "P-1001"
    assert produkt.bezeichnung == "Kaffeebohnen 500 g"
    assert produkt.nettopreis == pytest.approx(8.90)
    assert produkt.kategorie == "Lebensmittel"

    assert str(produkt) == "P-1001 Kaffeebohnen 500 g – 8.90 € netto"
    assert repr(produkt) == (
        "Produkt('P-1001', 'Kaffeebohnen 500 g', 8.9, 'Lebensmittel')"
    )


def test_produkt_csv_datei_und_vergleiche() -> None:
    """Prüft die sechs Produkte, ihre Sortierung und ihre Identität."""
    produkte = Produkt.aus_csv_datei(CSV_PFAD)

    assert len(produkte) == 6
    assert [p.artikelnummer for p in sorted(produkte)] == [
        "P-1003",
        "P-1002",
        "P-1001",
        "P-1006",
        "P-1005",
        "P-1004",
    ]

    assert Produkt("P-1001", "Kaffee", 8.90) == Produkt(
        "P-1001", "Anderer Name", 1.00
    )