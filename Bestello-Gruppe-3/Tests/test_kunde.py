import pytest

from Bestelo.Kunden import Kunde, Privatkunde


def test_kunde_daten_und_darstellung() -> None:
    """Prüft Kundendaten, Darstellungen und Gleichheit."""
    kunde = Kunde(1001, "  Anna Müller  ", "anna@example.com")

    assert kunde.kundennummer == 1001
    assert kunde.name == "Anna Müller"
    assert kunde.email == "anna@example.com"
    assert str(kunde) == "Kunde 1001: Anna Müller"
    assert repr(kunde) == "Kunde(1001, 'Anna Müller')"
    assert kunde.begruessung() == "Hallo Anna Müller!"
    assert kunde.rabattsatz() == 0.0
    assert kunde == Kunde(1001, "Anderer Name", "andere@example.com")
    assert kunde != Kunde(1002, "Ben", "ben@example.com")
    assert kunde != 1001


def test_kunde_ungueltige_angaben() -> None:
    """Prüft ungültige Angaben beim Anlegen und Ändern."""
    with pytest.raises(ValueError):
        Kunde(999, "Anna", "anna@example.com")

    with pytest.raises(ValueError):
        Kunde(1001, "Anna", "anna.example.com")

    with pytest.raises(ValueError):
        Kunde(1001, "Anna", "anna@example")

    kunde = Kunde(1001, "Anna", "anna@example.com")

    with pytest.raises(ValueError):
        kunde.name = "   "

    with pytest.raises(ValueError):
        kunde.email = "ungueltig"

    assert kunde.name == "Anna"
    assert kunde.email == "anna@example.com"


def test_kundennummer_nur_lesbar() -> None:
    """Prüft den Schreibschutz der Kundennummer."""
    kunde = Kunde(1001, "Anna", "anna@example.com")

    with pytest.raises(AttributeError):
        kunde.kundennummer = 2000

    assert kunde.kundennummer == 1001


def test_privatkunde() -> None:
    """Prüft Vererbung, Alter, Rabatt und Geburtsjahr."""
    kunde = Privatkunde(1001, "Anna", "anna@example.com", 1995)

    assert isinstance(kunde, Kunde)
    assert kunde.alter(2026) == 31
    assert kunde.rabattsatz() == 0.0
    assert repr(kunde) == "Privatkunde(1001, 'Anna')"

    kunde.stammkunde = True
    assert kunde.rabattsatz() == pytest.approx(0.02)

    with pytest.raises(ValueError):
        kunde.geburtsjahr = 1899