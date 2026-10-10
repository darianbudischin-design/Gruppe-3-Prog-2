from block_d import Verein
from kunden import Geschaeftskunde, Kunde, Privatkunde


def verein():
    return Verein("TSG Haßloch", "info@tsg.de", 1003, "VR 1234")


def test_block_d_ist_kunde():
    v = verein()
    assert isinstance(v, Kunde)
    assert (v.name, v.email, v.kundennummer, v.vereinsregisternummer) == ("TSG Haßloch", "info@tsg.de", 1003, "VR 1234")


def test_block_d_begruessung_ueberschrieben():
    assert verein().begruessung() == "An den Vorstand des Vereins TSG Haßloch"


def test_block_d_rabatt():
    assert verein().rabattsatz() == 0.05


def test_block_d_polymorphie():
    kunden: list[Kunde] = [
        Privatkunde("Anna", "a@x.de", 1, 1995),
        Geschaeftskunde("Ben", "b@x.de", 2, "Schmidt IT GmbH", "DE123456789"),
        verein(),
    ]
    assert [k.rabattsatz() for k in kunden] == [0.0, 0.03, 0.05]
