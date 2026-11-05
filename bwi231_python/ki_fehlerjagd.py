# KI-FEHLERJAGD (8 Min., zu zweit)
# AUFGABE: Der folgende Code wurde von einer KI erzeugt. Er enthält DREI Fehler.
#   1. Lesen Sie den Code und markieren Sie verdächtige Stellen mit einem Kommentar.
#   2. Erzeugen Sie unten zwei Objekte und rufen Sie die Methoden auf – manche Fehler
#      zeigen sich erst bei der Ausführung oder beim zweiten Objekt.
#   3. Korrigieren Sie die Fehler.
# Nach der Korrektur soll dieser Testaufruf  1200.0 300.0 []  ausgeben:
#   lisa = Werkstudent("Lisa", 15.0, "HWG LU")
#   tom = Mitarbeiter("Tom", 30.0)
#   lisa.projekt_hinzufuegen("Bestelo")
#   print(lisa.monatsgehalt(100), tom.monatsgehalt(10), tom.projekte)

# Von einer KI erzeugt auf den Prompt:
# "Schreibe eine Python-Klassenhierarchie Mitarbeiter -> Werkstudent mit
#  Monatsgehalt und einer Liste von Projekten."

class Mitarbeiter:
    def __init__(self, name: str, stundenlohn: float, projekte: list[str] = []) -> None:
        self.name = name
        self.stundenlohn = stundenlohn
        self.projekte = projekte

    def monatsgehalt(self,stundenlohn, stunden: float) -> float:
        return round(stundenlohn * stunden, 2)

    def projekt_hinzufuegen(self, projekt: str) -> None:
        self.projekte.append(projekt)


class Werkstudent(Mitarbeiter):
    MAX_STUNDEN = 80

    def __init__(self, name: str, stundenlohn: float, hochschule: str) -> None:
        self.hochschule = hochschule

    def monatsgehalt(self, stunden: float) -> float:
        return super().monatsgehalt(min(stunden, self.MAX_STUNDEN))
