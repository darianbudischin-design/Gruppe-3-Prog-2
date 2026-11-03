"""Tests für Firmen und Vereine. parametrize führt einen Test mit mehreren Werten aus."""

import pytest

from bestelo.kunden import Geschaeftskunde, Verein


def test_firma_normalisiert_daten() -> None:
    firma = Geschaeftskunde(1002, "Ben", "b@example.de", " IT GmbH ", "de 123 456 789")
    assert firma.ust_id == "DE123456789"
    assert firma.zahlungsziel_tage == 14
    assert firma.rabattsatz() == 0.03
    assert firma.begruessung() == "Sehr geehrte Damen und Herren der IT GmbH,"
    assert str(firma) == "Kunde 1002: IT GmbH (Ansprechpartner: Ben)"


@pytest.mark.parametrize("ust_id", ["AT123456789", "DE1234", "DE12345678X"])
def test_firma_lehnt_falsche_id_ab(ust_id: str) -> None:
    # Dieser Testabschnitt besteht, wenn genau der erwartete Fehlertyp auftritt.
    with pytest.raises(ValueError):
        Geschaeftskunde(1002, "Ben", "b@example.de", "IT GmbH", ust_id)


def test_zahlungsziel_grenzen() -> None:
    firma = Geschaeftskunde(1002, "Ben", "b@example.de", "IT GmbH", "DE123456789", 0)
    firma.zahlungsziel_tage = 60
    with pytest.raises(ValueError):
        firma.zahlungsziel_tage = 61
    assert firma.zahlungsziel_tage == 60


def test_verein_rabatt_und_begruessung() -> None:
    verein = Verein(1003, "SV", "v@example.de", "VR 1234")
    assert verein.begruessung() == "An den Vorstand des Vereins SV"
    assert verein.rabattsatz() == 0.05
    verein.gemeinnuetzig = False
    assert verein.rabattsatz() == 0.02


def test_verein_prueft_registernummer() -> None:
    with pytest.raises(ValueError):
        Verein(1003, "SV", "v@example.de", "VR1234")


def test_firmendaten_setter_pruefen_aenderungen() -> None:
    """Auch nach dem Anlegen gelten dieselben Validierungsregeln."""
    firma = Geschaeftskunde(1002, "Ben", "b@example.de", "IT", "DE123456789")
    with pytest.raises(ValueError):
        firma.firmenname = " "
    with pytest.raises(ValueError):
        firma.ust_id = "DE12345678X"
    with pytest.raises(ValueError):
        firma.zahlungsziel_tage = -1
    assert (firma.firmenname, firma.ust_id, firma.zahlungsziel_tage) == (
        "IT", "DE123456789", 14
    )


def test_polymorphie_wie_im_aufgabenblatt() -> None:
    """Alle drei Kundentypen liefern über dieselbe Methode ihre Rabatte."""
    from bestelo.kunden import Privatkunde

    kunden = [
        Privatkunde(1001, "Anna", "a@example.de", 1995),
        Geschaeftskunde(1002, "Ben", "b@example.de", "IT", "DE123456789"),
        Verein(1003, "SV", "v@example.de", "VR 1234"),
    ]
    assert [kunde.rabattsatz() for kunde in kunden] == [0.0, 0.03, 0.05]
