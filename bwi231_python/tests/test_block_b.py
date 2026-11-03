from block_b import Rechnung


def test_block_b_konstruktor_und_klassenattribut():
    r = Rechnung("R-2026-001", "Anna", 250.0)
    assert (r.nummer, r.kunde, r.netto) == ("R-2026-001", "Anna", 250.0)
    assert Rechnung.MWST_SATZ == 0.19


def test_block_b_brutto_default_und_ueberladen():
    r = Rechnung("R-2026-001", "Anna", 250.0)
    assert r.brutto() == 297.5
    assert r.brutto(0.07) == 267.5


def test_block_b_str_repr():
    r = Rechnung("R-2026-001", "Anna", 250.0)
    assert str(r) == "R-2026-001 (Anna): 250.00 EUR netto"
    assert repr(r) == "Rechnung(nummer='R-2026-001', kunde='Anna', netto=250.0)"


def test_block_b_eq_lt():
    a = Rechnung("R-2026-001", "Anna", 250.0)
    b = Rechnung("R-2026-002", "Ben", 99.0)
    assert a == Rechnung("R-2026-001", "Anna M.", 1.0)
    assert a != b
    assert (a == "R-2026-001") is False
    assert [r.nummer for r in sorted([a, b])] == ["R-2026-002", "R-2026-001"]


def test_block_b_classmethod():
    r = Rechnung.aus_text("R-2026-001;Anna;250.00")
    assert isinstance(r, Rechnung)
    assert (r.nummer, r.kunde, r.netto) == ("R-2026-001", "Anna", 250.0)


def test_block_b_staticmethod():
    assert Rechnung.ist_gueltige_nummer("R-2026-001")
    assert not Rechnung.ist_gueltige_nummer("2026-001")
    assert not Rechnung.ist_gueltige_nummer("R-2026-0001")
