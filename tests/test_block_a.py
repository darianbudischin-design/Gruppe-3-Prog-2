from block_a import Mitarbeiter, lohnsumme, teuerste_person


def team():
    return [Mitarbeiter("Lisa Kraus", 4711, 15.0), Mitarbeiter("Tom Berg", 4712, 32.5), Mitarbeiter("Ali Demir", 4713, 28.0)]


def test_block_a_attribute():
    m = Mitarbeiter("Lisa Kraus", 4711, 15.0)
    assert (m.name, m.personalnummer, m.stundenlohn) == ("Lisa Kraus", 4711, 15.0)


def test_block_a_monatsgehalt():
    assert Mitarbeiter("Tom", 1, 32.5).monatsgehalt(160) == 5200.0
    assert Mitarbeiter("X", 2, 12.345).monatsgehalt(3) == 37.04


def test_block_a_str():
    assert str(Mitarbeiter("Lisa Kraus", 4711, 15.0)) == "4711 Lisa Kraus (15.00 EUR/h)"


def test_block_a_lohnsumme():
    assert lohnsumme(team(), 160) == 12080.0
    assert lohnsumme([], 160) == 0


def test_block_a_teuerste_person():
    assert teuerste_person(team()).name == "Tom Berg"
    assert teuerste_person([]) is None
