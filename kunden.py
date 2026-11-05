class Kunde:
    def __init__(self, name: str, email: str, kundennummer: int) -> None:
        self.name = name
        self.email = email
        self.kundennummer = kundennummer

    def begruessung(self) -> str:
        return f"Hallo {self.name}!"

    def rabattsatz(self) -> float:
        return 0.0


class Privatkunde(Kunde):
    def __init__(self, name: str, email: str, kundennummer: int, geburtsjahr: int) -> None:
        super().__init__(name, email, kundennummer)      # Basis zuerst
        self.geburtsjahr = geburtsjahr


class Geschaeftskunde(Kunde):
    def __init__(self, name: str, email: str, kundennummer: int,
                 firmenname: str, ust_id: str) -> None:
        super().__init__(name, email, kundennummer)
        self.firmenname = firmenname
        self.ust_id = ust_id

    def begruessung(self) -> str:                         # überschreiben
        return f"Sehr geehrte Damen und Herren der {self.firmenname},"

    def rabattsatz(self) -> float:                        # überschreiben + erweitern
        return super().rabattsatz() + 0.03


if __name__ == "__main__":
    anna = Privatkunde("Anna Müller", "anna@example.com", 1001, 1995)
    ben = Geschaeftskunde("Ben Schmidt", "ben@schmidt-it.de", 1002,
                          "Schmidt IT GmbH", "DE123456789")

    print(anna.begruessung(), anna.geburtsjahr)     # geerbt + eigen
    print(ben.begruessung())                        # überschrieben
    print(isinstance(ben, Kunde), isinstance(ben, Privatkunde))

    kunden: list[Kunde] = [anna, ben]
    for kunde in kunden:                            # Polymorphie
        print(f"{kunde.name}: {kunde.rabattsatz():.0%} Rabatt")

class Verein(Kunde):
    """Verwaltet einen Verein und seinen Rabatt."""

    def __init__(self, name: str, email: str, kundennummer: int,
                 vereinsregisternummer: str, gemeinnuetzig: bool = True) -> None:
        super().__init__(name, email, kundennummer)
        self.vereinsregisternummer = vereinsregisternummer
        self.gemeinnuetzig = gemeinnuetzig

    @property
    def vereinsregisternummer(self) -> str:
        return self._vereinsregisternummer

    @vereinsregisternummer.setter
    def vereinsregisternummer(self, wert: str) -> None:
        if not isinstance(wert, str) or not wert.startswith("VR ") or not wert[3:].isdigit():
            raise ValueError("Registernummer muss mit VR und einem Leerzeichen beginnen, gefolgt von Ziffern")
        self._vereinsregisternummer = wert

    def begruessung(self) -> str:
        return f"An den Vorstand des Vereins {self.name}"

    def rabattsatz(self) -> float:
        return 0.05 if self.gemeinnuetzig else 0.02