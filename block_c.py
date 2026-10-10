"""Übung C1 – Lagerartikel (15 Min., zu zweit, ohne KI)

Ausgangslage:
    Ein Lager verwaltet Artikel. Der Bestand darf nur über Zu- und Abgänge verändert
    werden – nie direkt. Fällt er unter den Mindestbestand, muss nachbestellt werden.

Ihre Aufgabe – Schritt für Schritt:
    1. Klasse Lagerartikel: Konstruktor __init__(self, bezeichnung, mindestbestand=0);
       der Bestand startet bei 0 (intern self._bestand).
    2. Property bestand: nur lesend – KEIN Setter.
    3. Property mindestbestand MIT Setter: negativer Wert -> ValueError.
       Im Konstruktor self.mindestbestand = ... schreiben (läuft durch den Setter).
    4. Berechnete Property muss_nachbestellt_werden: True, wenn Bestand < Mindestbestand.
    5. zugang(menge) und abgang(menge): Menge <= 0 -> ValueError;
       Abgang größer als Bestand -> ValueError.

Vorlage: beispiele/konto.py (gleicher Aufbau: saldo ~ bestand, dispo ~ mindestbestand,
verfuegbar ~ muss_nachbestellt_werden)
Fertig, wenn pytest -k block_c "6 passed" meldet und Ihre Ausgabe so aussieht:
    7 True
    bestand ist schreibgeschützt
"""


class Lagerartikel:
    pass  # TODO C1


if __name__ == "__main__":
    # a = Lagerartikel("Druckerpapier", mindestbestand=10)
    # a.zugang(12)
    # a.abgang(5)
    # print(a.bestand, a.muss_nachbestellt_werden)
    # try:
    #     a.bestand = 100
    # except AttributeError:
    #     print("bestand ist schreibgeschützt")
    pass
