import pytest

from Bestelo.Kunden import Geschaeftskunde
from Bestelo.Verein import Verein


def test_geschaeftskunde_daten() -> None:
    """Prüft Normalisierung, Standardwerte und Darstellungen."""
    kunde = Geschaeftskunde(
        1002,
        "Ben Schmidt",
        "ben@schmidt-it.de",
        "  Schmidt IT GmbH  ",
        "de 123 456 789",
    )

    assert kunde.firmenname == "Schmidt IT GmbH"
    assert kunde.ust_id == "DE123456789"
    assert kunde.zahlungsziel_tage == 14
    assert kunde.rabattsatz() == pytest.approx(0.03)
    assert kunde.begruessung() == (
        "Sehr geehrte Damen und Herren der Schmidt IT GmbH,"
    )
    assert str(kunde) == (
        "Kunde 1002: Schmidt IT GmbH (Ansprechpartner: Ben Schmidt)"
    )


def test_geschaeftskunde_ungueltige_angaben() -> None:
    """Prüft ungültige Firmendaten."""
    kunde = Geschaeftskunde(
        1002, "Ben", "ben@example.com", "Firma", "DE123456789"
    )

    with pytest.raises(ValueError):
        kunde.firmenname = " "

    for ust_id in ("DE123", "AT123456789", "DE12345678X"):
        with pytest.raises(ValueError):
            kunde.ust_id = ust_id

    for tage in (-1, 90):
        with pytest.raises(ValueError):
            kunde.zahlungsziel_tage = tage


def test_verein_begruessung_und_rabatt() -> None:
    """Prüft beide Vereinsrabatte und die Begrüßung."""
    verein = Verein(
        1003, "SV Musterstadt", "info@sv.de", "VR 1234"
    )

    assert verein.registernummer == "VR 1234"
    assert verein.gemeinnuetzig is True
    assert verein.rabattsatz() == pytest.approx(0.05)
    assert verein.begruessung() == (
        "An den Vorstand des Vereins SV Musterstadt"
    )

    verein.gemeinnuetzig = False
    assert verein.rabattsatz() == pytest.approx(0.02)


def test_verein_ungueltige_registernummer() -> None:
    """Prüft fehlendes Leerzeichen und ungültige Registerzeichen."""
    for nummer in ("VR1234", "VR ABC", "VR "):
        with pytest.raises(ValueError):
            Verein(1003, "Verein", "info@verein.de", nummer)