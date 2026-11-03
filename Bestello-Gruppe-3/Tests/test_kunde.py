import pytest

from Bestelo.Kunden import Kunde


def test_kunde_anlegen() -> None:
    """Prüft die gespeicherten Daten und das Entfernen von Leerzeichen."""
    kunde = Kunde(1001, "  Anna Müller  ", "anna@example.com")

    assert kunde.kundennummer == 1001
    assert kunde.name == "Anna Müller"
    assert kunde.email == "anna@example.com"
    assert str(kunde) == "Kunde 1001: Anna Müller"
    assert repr(kunde) == "Kunde(1001, 'Anna Müller')"


def test_ungueltige_email() -> None:
    """Eine E-Mail ohne @ muss einen ValueError auslösen."""
    with pytest.raises(ValueError):
        Kunde(1001, "Anna Müller", "anna.example.com")


def test_leerer_name() -> None:
    """Der Setter darf keinen leeren Namen speichern."""
    kunde = Kunde(1001, "Anna Müller", "anna@example.com")

    with pytest.raises(ValueError):
        kunde.name = "   "

    assert kunde.name == "Anna Müller"


def test_kundennummer_nur_lesbar() -> None:
    """Die Kundennummer darf nachträglich nicht geändert werden."""
    kunde = Kunde(1001, "Anna Müller", "anna@example.com")

    with pytest.raises(AttributeError):
        kunde.kundennummer = 2000

    assert kunde.kundennummer == 1001