"""Übung B1 – Rechnung (20 Min., zu zweit, ohne KI)

Ausgangslage:
    Bestelo braucht Rechnungen mit Nummer, Kunde und Nettobetrag.
    Sie üben dabei alle Methodenarten von heute.

Ihre Aufgabe – Schritt für Schritt:
    1. Klasse Rechnung mit Klassenattribut MWST_SATZ = 0.19;
       der Konstruktor speichert nummer, kunde, netto.
    2. brutto(self, mwst_satz=None): ohne Argument mit MWST_SATZ rechnen, sonst mit dem
       übergebenen Satz; Ergebnis auf 2 Stellen runden.
    3. __str__  -> R-2026-001 (Anna): 250.00 EUR netto
       __repr__ -> Rechnung(nummer='R-2026-001', kunde='Anna', netto=250.0)
    4. __eq__: gleich bei gleicher Rechnungsnummer (fremder Typ -> NotImplemented);
       __lt__: Vergleich über netto.
    5. @classmethod aus_text(cls, zeile): macht aus "R-2026-001;Anna;250.00" eine Rechnung.
    6. @staticmethod ist_gueltige_nummer(nummer): True, wenn die Nummer mit "R-" beginnt
       und genau 10 Zeichen hat.

Vorlagen: beispiele/b_spezialmethoden.py und beispiele/b_classmethod.py
Fertig, wenn pytest -k block_b "6 passed" meldet und Ihre Ausgabe so aussieht:
    R-2026-001 (Anna): 250.00 EUR netto
    297.5 267.5
    ['R-2026-002', 'R-2026-001']
    True
    True False
"""


class Rechnung:
    pass  # TODO B1


if __name__ == "__main__":
    # r1 = Rechnung.aus_text("R-2026-001;Anna;250.00")
    # r2 = Rechnung("R-2026-002", "Ben", 99.0)
    # print(r1)
    # print(r1.brutto(), r1.brutto(0.07))
    # print([r.nummer for r in sorted([r1, r2])])
    # print(r1 == Rechnung("R-2026-001", "Anna M.", 1.0))
    # print(Rechnung.ist_gueltige_nummer("R-2026-001"),
    #       Rechnung.ist_gueltige_nummer("2026-1"))
    pass
