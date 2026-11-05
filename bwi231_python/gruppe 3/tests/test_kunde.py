"""Tests für Stammdaten, Vererbung und Rabatt. assert prüft eine erwartete Aussage."""

from datetime import date

import pytest

from bestelo.kunden import Kunde, Privatkunde


def test_name_und_darstellung() -> None:
    kunde = Kunde(1001, "  Anna Müller ", "anna@example.com")
    assert kunde.begruessung() == "Hallo Anna Müller!"
    assert str(kunde) == "Kunde 1001: Anna Müller"
    assert repr(kunde) == "Kunde(1001, 'Anna Müller')"


def test_nummer_ist_nur_lesbar() -> None:
    kunde = Kunde(1000, "Anna", "anna@example.com")
    with pytest.raises(AttributeError):
        kunde.kundennummer = 1002
    # Dieser Testabschnitt besteht, wenn genau der erwartete Fehlertyp auftritt.
    with pytest.raises(ValueError):
        Kunde(999, "Anna", "anna@example.com")


def test_ungueltige_kontaktdaten() -> None:
    with pytest.raises(ValueError):
        Kunde(1000, "Anna", "anna.example@com")
    kunde = Kunde(1000, "Anna", "anna@example.com")
    with pytest.raises(ValueError):
        kunde.name = " "
    assert kunde.name == "Anna"


def test_gleichheit_nach_nummer() -> None:
    a = Kunde(1001, "Anna", "a@example.de")
    assert a == Kunde(1001, "A.", "a2@example.de")
    assert a != Kunde(1002, "Anna", "a@example.de")
    assert a != "1001"


def test_privatkunde_alter_und_rabatt() -> None:
    p = Privatkunde(1001, "Anna", "a@example.de", 1995)
    assert p.alter(2026) == 31
    assert p.alter() == date.today().year - 1995
    assert p.rabattsatz() == 0.0
    p.stammkunde = True
    assert p.rabattsatz() == 0.02
    assert repr(p) == "Privatkunde(1001, 'Anna')"
    with pytest.raises(ValueError):
        p.geburtsjahr = date.today().year + 1


def test_email_setter_behaelt_gueltigen_wert() -> None:
    """Ungültige Änderungen dürfen gültige Stammdaten nicht überschreiben."""
    kunde = Kunde(1001, "Anna", "anna@example.com")
    for email in ("anna.example.com", "anna@example", ""):
        assert Kunde.ist_gueltige_email(email) is False
        with pytest.raises(ValueError):
            kunde.email = email
    assert kunde.email == "anna@example.com"


def test_privatkunde_erbt_gemeinsame_methoden() -> None:
    """Die Unterklasse nutzt Begrüßung und Gleichheit aus der Basisklasse."""
    kunde = Privatkunde(1001, "Anna Müller", "a@example.de", 1900)
    assert str(kunde) == "Kunde 1001: Anna Müller"
    assert kunde.begruessung() == "Hallo Anna Müller!"
    assert kunde == Kunde(1001, "A.", "a@example.de")
    kunde.geburtsjahr = date.today().year
    assert kunde.alter() == 0
    with pytest.raises(ValueError):
        kunde.geburtsjahr = 1899


def test_fruehere_importwege_verwenden_dieselben_klassen() -> None:
    """Die früher getrennten Dateien dürfen keine abweichenden Klassen erzeugen."""
    from kunde import Kunde as AlterKunde
    from kunden_typen import Privatkunde as AlterPrivatkunde

    assert AlterKunde is Kunde
    assert AlterPrivatkunde is Privatkunde
