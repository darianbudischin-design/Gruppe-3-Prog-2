"""Tests für Produkte und CSV-Dateien. tmp_path ist ein temporärer Testordner."""

from pathlib import Path

import pytest

from bestelo.produkte import Produkt


def test_preis_und_steuer() -> None:
    artikel = Produkt("P-1001", " Kaffee ", 8.90, "Lebensmittel")
    assert artikel.bezeichnung == "Kaffee"
    assert (artikel.mwst_satz, artikel.bruttopreis) == (0.07, 9.52)
    artikel.kategorie = "Getränke"
    assert (artikel.mwst_satz, artikel.bruttopreis) == (0.19, 10.59)


def test_ungueltige_produktdaten() -> None:
    # Dieser Testabschnitt besteht, wenn genau der erwartete Fehlertyp auftritt.
    with pytest.raises(ValueError):
        Produkt("1001", "Kaffee", 1)
    with pytest.raises(ValueError):
        Produkt("P-1001", " ", 1)
    with pytest.raises(ValueError):
        Produkt("P-1001", "Kaffee", 0)
    with pytest.raises(ValueError):
        Produkt("P-1001", "Kaffee", 1, "Unbekannt")


def test_csv_zeile() -> None:
    p = Produkt.aus_csv_zeile("P-1003;Orangensaft 1 l;2.80;Getränke\n")
    assert (p.artikelnummer, p.bezeichnung, p.nettopreis, p.kategorie) == (
        "P-1003", "Orangensaft 1 l", 2.80, "Getränke"
    )


def test_csv_datei_ueberspringt_kopf_und_leerzeilen(tmp_path: Path) -> None:
    pfad = tmp_path / "sortiment.csv"
    pfad.write_text("nummer;name;preis;kategorie\n\nP-1009;Öl;4.00;Lebensmittel\n",
                    encoding="utf-8")
    artikel = Produkt.aus_csv_datei(pfad)
    assert [p.bezeichnung for p in artikel] == ["Öl"]


def test_gleichheit_und_sortierung() -> None:
    teuer = Produkt("P-1001", "A", 10)
    billig = Produkt("P-1002", "Z", 2)
    assert teuer == Produkt("P-1001", "Anderer Name", 20)
    assert teuer != "P-1001"
    assert sorted([teuer, billig]) == [billig, teuer]


def test_csv_sortiment_entspricht_vorgabe() -> None:
    """Prüft sämtliche vorgegebenen Artikeldaten aus Abschnitt 5.3."""
    from bestelo.__main__ import CSV_PFAD

    produkte = Produkt.aus_csv_datei(CSV_PFAD)
    assert [(p.artikelnummer, p.bezeichnung, p.nettopreis, p.kategorie)
            for p in produkte] == [
        ("P-1001", "Kaffeebohnen 500 g", 8.90, "Lebensmittel"),
        ("P-1002", "Mineralwasser 12 × 1 l", 7.50, "Getränke"),
        ("P-1003", "Orangensaft 1 l", 2.80, "Getränke"),
        ("P-1004", "Fachbuch Python-Grundlagen", 24.90, "Bücher"),
        ("P-1005", "Küchenhandtücher 3er-Set", 12.00, "Haushalt"),
        ("P-1006", "USB-C-Ladekabel 2 m", 9.90, "Elektronik"),
    ]
    assert min(produkte).artikelnummer == "P-1003"


def test_produkt_darstellung_und_rundung() -> None:
    """Die Beispiele verwenden Python-float und dessen Rundungsverhalten."""
    p = Produkt("P-1001", "Kaffeebohnen 500 g", 8.90, "Lebensmittel")
    assert str(p) == "P-1001 Kaffeebohnen 500 g – 8.90 € netto"
    assert repr(p) == "Produkt('P-1001', 'Kaffeebohnen 500 g', 8.9, 'Lebensmittel')"
    wasser = Produkt("P-1002", "Wasser", 7.50, "Getränke")
    assert wasser.bruttopreis == 8.92
    with pytest.raises(AttributeError):
        p.artikelnummer = "P-9999"
    p.nettopreis = 1.234
    assert p.nettopreis == 1.23


def test_csv_klassenmethode_verwendet_cls() -> None:
    """Auch beim Aufruf über eine Unterklasse muss deren Typ erhalten bleiben."""
    class Lernprodukt(Produkt):
        pass

    p = Lernprodukt.aus_csv_zeile("P-1001;Kaffee;8.90;Lebensmittel")
    assert isinstance(p, Lernprodukt)
