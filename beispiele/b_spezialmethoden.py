class Kunde:
    def __init__(self, name: str, kundennummer: int, umsatz: float = 0.0) -> None:
        self.name = name
        self.kundennummer = kundennummer
        self.umsatz = umsatz

    def __str__(self) -> str:                      # für Menschen
        return f"Kunde {self.kundennummer}: {self.name}"

    def __repr__(self) -> str:                     # für Entwickler
        return f"Kunde(name={self.name!r}, kundennummer={self.kundennummer}, umsatz={self.umsatz})"

    def __eq__(self, other: object) -> bool:       # Gleichheit
        if not isinstance(other, Kunde):
            return NotImplemented
        return self.kundennummer == other.kundennummer

    def __lt__(self, other: "Kunde") -> bool:      # "kleiner als" -> sortierbar
        return self.umsatz < other.umsatz


anna = Kunde("Anna", 1001, 1500.0)
ben = Kunde("Ben", 1002, 300.0)
anna_doppelt = Kunde("Anna M.", 1001)

print(anna)
print(repr(anna))
print([anna, ben])
print(anna == anna_doppelt, anna is anna_doppelt)
print([k.name for k in sorted([anna, ben])])
