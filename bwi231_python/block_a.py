"""Übung A1/A2 – Mitarbeiter (20 Min., zu zweit, ohne KI)

Ausgangslage:
    Eine kleine Firma verwaltet ihre Mitarbeitenden bisher in Excel. Sie schreiben
    die Klasse Mitarbeiter und zwei Funktionen, die ein Team auswerten.

Ihre Aufgabe – Schritt für Schritt:
    1. Klasse Mitarbeiter: Konstruktor __init__(self, name, personalnummer, stundenlohn)
       speichert alle drei Werte als Attribute.
    2. Methode monatsgehalt(self, stunden): Stundenlohn × Stunden, mit round(..., 2) gerundet.
    3. Methode __str__: liefert genau  4711 Lisa Kraus (15.00 EUR/h)   (Tipp: f-String mit :.2f)
    4. Funktion lohnsumme(team, stunden): Summe aller Monatsgehälter – mit einer Schleife;
       leeres Team -> 0.
    5. Funktion teuerste_person(team): Person mit dem höchsten Stundenlohn – mit einer
       Schleife, OHNE max(); leeres Team -> None.
    6. Unten im __main__-Block ausprobieren, dann im Terminal:  pytest -k block_a

Fertig, wenn pytest -k block_a "5 passed" meldet und Ihre Ausgabe so aussieht:
    4711 Lisa Kraus (15.00 EUR/h)
    5200.0
    12080.0
    Tom Berg
"""


class Mitarbeiter:
    pass  # TODO A1


def lohnsumme(team: list[Mitarbeiter], stunden: float) -> float:
    raise NotImplementedError  # TODO A2


def teuerste_person(team: list[Mitarbeiter]) -> Mitarbeiter | None:
    raise NotImplementedError  # TODO A2


if __name__ == "__main__":
    # Zum Ausprobieren – die Zeilen einkommentieren, sobald Ihre Klasse steht:
    # team = [Mitarbeiter("Lisa Kraus", 4711, 15.0),
    #         Mitarbeiter("Tom Berg", 4712, 32.5),
    #         Mitarbeiter("Ali Demir", 4713, 28.0)]
    # print(team[0])
    # print(team[1].monatsgehalt(160))
    # print(lohnsumme(team, 160))
    # print(teuerste_person(team).name)
    pass
