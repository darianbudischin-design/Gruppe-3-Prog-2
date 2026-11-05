class Mitarbeiter:
    """Verwaltet Mitarbeiterdaten für Block A."""

    def __init__(self, name: str, personalnummer: int, stundenlohn: float) -> None:
        self.name = name
        self.personalnummer = personalnummer
        self.stundenlohn = stundenlohn

    def monatsgehalt(self, stunden: float) -> float:
        return round(self.stundenlohn * stunden, 2)

    def __str__(self) -> str:
        return f"{self.personalnummer} {self.name} ({self.stundenlohn:.2f} EUR/h)"


def lohnsumme(team_liste: list[Mitarbeiter], stunden: float) -> float:
    return round(sum(m.monatsgehalt(stunden) for m in team_liste), 2)


def teuerste_person(team_liste: list[Mitarbeiter]) -> Mitarbeiter | None:
    return max(team_liste, key=lambda m: m.stundenlohn, default=None)