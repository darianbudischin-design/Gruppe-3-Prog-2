"""Integrationstests verbinden CSV, Kunden und Bestellungen. capsys erfasst die Ausgabe."""

import pytest

from bestelo.__main__ import CSV_PFAD, main
from bestelo.bestellungen import Bestellung
from bestelo.kunden import Verein
from bestelo.produkte import Produkt


def test_verein_bestellt_orangensaft_aus_csv() -> None:
    sortiment = Produkt.aus_csv_datei(CSV_PFAD)
    assert len(sortiment) == 6
    saft = min(sortiment)
    assert saft.artikelnummer == "P-1003"
    b = Bestellung(Verein(1003, "SV Musterstadt", "v@example.de", "VR 1234"))
    b.hinzufuegen(saft, 24)
    assert b.status == "offen"
    assert b.brutto_summe == 75.97


def test_demo_zeigt_beide_bestellungen(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    ausgabe = capsys.readouterr().out
    assert "Brutto: 79.66 €" in ausgabe
    assert "(offen) für SV Musterstadt: 1 Position(en), 75.97 € brutto" in ausgabe


def test_paketstart_entspricht_demo_der_pdf() -> None:
    """Prüft den tatsächlichen Startbefehl in einem neuen Python-Prozess."""
    from pathlib import Path
    import subprocess
    import sys

    result = subprocess.run(
        [sys.executable, "-B", "-X", "utf8", "-m", "bestelo"],
        cwd=Path(__file__).resolve().parents[1],
        capture_output=True, text=True, encoding="utf-8", check=True,
    )
    expected = """Sortiment (nach Preis):
P-1003 Orangensaft 1 l – 2.80 € netto
P-1002 Mineralwasser 12 × 1 l – 7.50 € netto
P-1001 Kaffeebohnen 500 g – 8.90 € netto
P-1006 USB-C-Ladekabel 2 m – 9.90 € netto
P-1005 Küchenhandtücher 3er-Set – 12.00 € netto
P-1004 Fachbuch Python-Grundlagen – 24.90 € netto
Kunde 1001: Anna Müller – 2% Rabatt
Kunde 1002: Schmidt IT GmbH (Ansprechpartner: Ben Schmidt) – 3% Rabatt
Kunde 1003: SV Musterstadt – 5% Rabatt
==================================================
Bestellung B-0001 (abgeschlossen)
Sehr geehrte Damen und Herren der Schmidt IT GmbH,
--------------------------------------------------
3 × Kaffeebohnen 500 g à 8.90 € = 26.70 €
6 × Mineralwasser 12 × 1 l à 7.50 € = 45.00 €
--------------------------------------------------
Netto: 71.70 €
Rabatt 3%: -2.15 €
MwSt.: 10.11 €
Brutto: 79.66 €
Bestellung B-0002 (offen) für SV Musterstadt: 1 Position(en), 75.97 € brutto
"""
    assert result.stdout == expected
    assert result.stderr == ""
