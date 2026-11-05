class Kunde:
    def __init__(self, name: str, email: str, kundennummer: int) -> None:
        self.name = name
        self.email = email
        self.kundennummer = kundennummer

    @classmethod
    def aus_csv_zeile(cls, zeile: str) -> "Kunde":
        """Alternativer Konstruktor: '1001;Anna Müller;anna@example.com'."""
        nummer, name, email = zeile.strip().split(";")
        return cls(name, email, int(nummer))

    @classmethod
    def aus_dict(cls, daten: dict) -> "Kunde":
        return cls(daten["name"], daten["email"], daten["kundennummer"])

    @staticmethod
    def ist_gueltige_email(email: str) -> bool:
        """Braucht weder self noch cls – gehört thematisch aber zur Klasse."""
        return "@" in email and "." in email.split("@")[-1]


anna = Kunde.aus_csv_zeile("1001;Anna Müller;anna@example.com")
ben = Kunde.aus_dict({"name": "Ben", "email": "ben@x.de", "kundennummer": 1002})
print(anna.name, anna.kundennummer)
print(ben.email)
print(Kunde.ist_gueltige_email("kein-at-zeichen"))
