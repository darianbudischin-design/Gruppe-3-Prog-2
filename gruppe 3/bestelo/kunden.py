from datetime import date


class Kunde:
    """Verwaltet die gemeinsamen Kundendaten."""

    def __init__(self, name: str, email: str, kundennummer: int) -> None:
        if type(kundennummer) is not int or kundennummer < 1:
            raise ValueError("Kundennummer muss eine positive ganze Zahl sein")
        self._kundennummer = kundennummer
        self.name = name
        self.email = email

    @property
    def kundennummer(self) -> int:
        return self._kundennummer

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, wert: str) -> None:
        if not isinstance(wert, str) or not wert.strip():
            raise ValueError("Name darf nicht leer sein")
        self._name = wert.strip()

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, wert: str) -> None:
        if not self.ist_gueltige_email(wert):
            raise ValueError("Ungültige E-Mail-Adresse")
        self._email = wert

    @staticmethod
    def ist_gueltige_email(email: str) -> bool:
        return isinstance(email, str) and "." in email.partition("@")[2]

    def begruessung(self) -> str:
        return f"Hallo {self.name}!"

    def rabattsatz(self) -> float:
        return 0.0

    def __str__(self) -> str:
        return f"Kunde {self.kundennummer}: {self.name}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.kundennummer}, {self.name!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Kunde):
            return NotImplemented
        return self.kundennummer == other.kundennummer


class Privatkunde(Kunde):
    """Ergänzt Alter und Stammkundenrabatt."""

    def __init__(self, name: str, email: str, kundennummer: int,
                 geburtsjahr: int, stammkunde: bool = False) -> None:
        super().__init__(name, email, kundennummer)
        self.geburtsjahr = geburtsjahr
        self.stammkunde = stammkunde

    @property
    def geburtsjahr(self) -> int:
        return self._geburtsjahr

    @geburtsjahr.setter
    def geburtsjahr(self, wert: int) -> None:
        if type(wert) is not int or not 1900 <= wert <= date.today().year:
            raise ValueError("Geburtsjahr außerhalb des erlaubten Bereichs")
        self._geburtsjahr = wert

    def alter(self, stichjahr: int | None = None) -> int:
        if stichjahr is None:
            stichjahr = date.today().year
        return stichjahr - self.geburtsjahr

    def rabattsatz(self) -> float:
        return 0.02 if self.stammkunde else 0.0


class Geschaeftskunde(Kunde):
    """Verwaltet Firma, Umsatzsteuer-ID und Zahlungsziel."""

    def __init__(self, name: str, email: str, kundennummer: int, firmenname: str,
                 ust_id: str, zahlungsziel_tage: int = 14) -> None:
        super().__init__(name, email, kundennummer)
        self.firmenname = firmenname
        self.ust_id = ust_id
        self.zahlungsziel_tage = zahlungsziel_tage

    @property
    def firmenname(self) -> str:
        return self._firmenname

    @firmenname.setter
    def firmenname(self, wert: str) -> None:
        if not isinstance(wert, str) or not wert.strip():
            raise ValueError("Firmenname darf nicht leer sein")
        self._firmenname = wert.strip()

    @property
    def ust_id(self) -> str:
        return self._ust_id

    @ust_id.setter
    def ust_id(self, wert: str) -> None:
        if not isinstance(wert, str):
            raise ValueError("USt-ID muss Text sein")
        wert = wert.replace(" ", "").upper()
        if len(wert) != 11 or not wert.startswith("DE") or not wert[2:].isdigit():
            raise ValueError("USt-ID muss aus DE und neun Ziffern bestehen")
        self._ust_id = wert

    @property
    def zahlungsziel_tage(self) -> int:
        return self._zahlungsziel_tage

    @zahlungsziel_tage.setter
    def zahlungsziel_tage(self, wert: int) -> None:
        if type(wert) is not int or not 0 <= wert <= 60:
            raise ValueError("Zahlungsziel muss zwischen 0 und 60 Tagen liegen")
        self._zahlungsziel_tage = wert

    def begruessung(self) -> str:
        return f"Sehr geehrte Damen und Herren der {self.firmenname},"

    def rabattsatz(self) -> float:
        return 0.03


class Verein(Kunde):
    """Verwaltet einen Verein und seinen Rabatt."""

    def __init__(self, name: str, email: str, kundennummer: int,
                 registernummer: str, gemeinnuetzig: bool = True) -> None:
        super().__init__(name, email, kundennummer)
        self.registernummer = registernummer
        self.gemeinnuetzig = gemeinnuetzig

    @property
    def registernummer(self) -> str:
        return self._registernummer

    @registernummer.setter
    def registernummer(self, wert: str) -> None:
        if not isinstance(wert, str) or not wert.startswith("VR ") or not wert[3:].isdigit():
            raise ValueError("Registernummer muss mit VR und einem Leerzeichen beginnen, gefolgt von Ziffern")
        self._registernummer = wert

    def begruessung(self) -> str:
        return f"An den Vorstand des Vereins {self.name}"

    def rabattsatz(self) -> float:
        return 0.05 if self.gemeinnuetzig else 0.02