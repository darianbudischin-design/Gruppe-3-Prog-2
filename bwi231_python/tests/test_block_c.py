import pytest

from block_c import Lagerartikel


def test_block_c_start():
    a = Lagerartikel("Papier", mindestbestand=10)
    assert a.bezeichnung == "Papier"
    assert a.bestand == 0
    assert a.mindestbestand == 10


def test_block_c_zugang_abgang():
    a = Lagerartikel("Papier")
    a.zugang(12)
    a.abgang(5)
    assert a.bestand == 7


def test_block_c_bestand_schreibgeschuetzt():
    a = Lagerartikel("Papier")
    with pytest.raises(AttributeError):
        a.bestand = 100


def test_block_c_mindestbestand_validiert():
    with pytest.raises(ValueError):
        Lagerartikel("Papier", mindestbestand=-1)
    a = Lagerartikel("Papier")
    with pytest.raises(ValueError):
        a.mindestbestand = -5


def test_block_c_ungueltige_mengen():
    a = Lagerartikel("Papier")
    with pytest.raises(ValueError):
        a.zugang(0)
    a.zugang(3)
    with pytest.raises(ValueError):
        a.abgang(4)


def test_block_c_nachbestellen():
    a = Lagerartikel("Papier", mindestbestand=10)
    a.zugang(12)
    assert not a.muss_nachbestellt_werden
    a.abgang(5)
    assert a.muss_nachbestellt_werden
