import pytest

from Bestelo.__main__ import CSV_PFAD, main
from Bestelo.Bestellungen import Bestellung
from Bestelo.Produkte import Produkt
from Bestelo.Verein import Verein


def test_verein_bestellt_produkt_aus_csv() -> None:
    """Prüft den Ablauf vom CSV-Import bis zur Vereinsbestellung."""
    produkte = Produkt.aus_csv_datei(CSV_PFAD)
    saft = next(p for p in produkte if p.artikelnummer == "P-1003")

    verein = Verein(
        1003, "SV Musterstadt", "info@example.com", "VR 1234"
    )
    bestellung = Bestellung(verein)
    bestellung.hinzufuegen(saft, 24)

    assert bestellung.status == "offen"
    assert len(bestellung) == 1
    assert bestellung.brutto_summe == pytest.approx(75.97)


def test_demo_ausgabe(capsys: pytest.CaptureFixture[str]) -> None:
    """Prüft, ob die Demo läuft und beide erwarteten Endbeträge ausgibt."""
    main()

    ausgabe = capsys.readouterr().out

    assert "Sortiment (nach Preis):" in ausgabe
    assert "Schmidt IT GmbH" in ausgabe
    assert "SV Musterstadt" in ausgabe
    assert "Brutto: 79.66 €" in ausgabe
    assert "75.97 € brutto" in ausgabe