class Kunde:
    def __init__(self, name: str, email: str, kundennummer: int) -> None:
        self.name = name
        self.email = email
        self.kundennummer = kundennummer

    def begruessung(self) -> str:
        return f"Hallo {self.name}!"


anna = Kunde("Anna Müller", "anna@example.com", 1001)
ben = Kunde(name="Ben Schmidt", email="ben@example.com", kundennummer=1002)

print(anna.name)
print(ben.begruessung())
print(type(anna))
