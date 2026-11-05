"""Kunden und ihre unterschiedlichen Rabattregeln."""
# Das aktuelle Jahr wird für die Prüfung des Geburtsjahrs gebraucht.
from datetime import date


class Kunde:
    """Verwaltet die gemeinsamen Kundendaten."""

    def __init__(self, kundennummer: int, name: str, email: str) -> None:
        """Legt ein geprüftes Objekt mit den übergebenen Werten an."""
        if type(kundennummer) is not int or kundennummer < 1000:
            raise ValueError("Kundennummer muss eine ganze Zahl ab 1000 sein")
        # Der Unterstrich markiert interne Daten. Die Property hat keinen Setter.
        self._kundennummer = kundennummer
        # Ohne Unterstrich läuft die Zuweisung durch den Setter und seine Prüfung.
        self.name = name
        self.email = email

    @property
    def kundennummer(self) -> int:
        """Liefert die feste Kundennummer."""
        return self._kundennummer

    @property
    def name(self) -> str:
        """Liefert den bereinigten Namen."""
        return self._name

    # Dieser Setter wird auch bei späterem kunde.name = ... ausgeführt.
    @name.setter
    def name(self, wert: str) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if not isinstance(wert, str) or not wert.strip():
            raise ValueError("Name darf nicht leer sein")
        self._name = wert.strip()

    @property
    def email(self) -> str:
        """Liefert die geprüfte E-Mail-Adresse."""
        return self._email

    @email.setter
    def email(self, wert: str) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if not self.ist_gueltige_email(wert):
            raise ValueError("Ungültige E-Mail-Adresse")
        self._email = wert

    # Diese Prüfung benötigt kein Kundenobjekt und deshalb kein self.
    @staticmethod
    def ist_gueltige_email(email: str) -> bool:
        """Prüft die Kursregel: Hinter dem @ muss ein Punkt vorkommen."""
        # partition liefert den Text vor @, das @ selbst und den Text dahinter.
        return isinstance(email, str) and "." in email.partition("@")[2]

    def begruessung(self) -> str:
        """Begrüßt den Kunden mit Namen."""
        return f"Hallo {self.name}!"

    def rabattsatz(self) -> float:
        """Liefert den Basisrabatt."""
        return 0.0

    def __str__(self) -> str:
        """Liefert die lesbare Darstellung gemäß Aufgabenbeschreibung."""
        return f"Kunde {self.kundennummer}: {self.name}"

    def __repr__(self) -> str:
        """Liefert die technische Darstellung des Objekts."""
        # type(self) zeigt auch bei Unterklassen den richtigen Namen. !r setzt Anführungszeichen.
        return f"{type(self).__name__}({self.kundennummer}, {self.name!r})"

    def __eq__(self, other: object) -> bool:
        """Vergleicht die fachliche Identität anhand der Nummer."""
        # Fremde Typen dürfen Python mitteilen, wie ein Vergleich behandelt wird.
        if not isinstance(other, Kunde):
            return NotImplemented
        return self.kundennummer == other.kundennummer


# Die Klammern bedeuten: Privatkunde erbt die gemeinsamen Methoden von Kunde.
class Privatkunde(Kunde):
    """Ergänzt Alter und Stammkundenrabatt."""

    def __init__(self, kundennummer: int, name: str, email: str,
                 geburtsjahr: int, stammkunde: bool = False) -> None:
        """Legt ein geprüftes Objekt mit den übergebenen Werten an."""
        # Zuerst legt die Basisklasse die gemeinsamen Kundendaten an.
        super().__init__(kundennummer, name, email)
        self.geburtsjahr = geburtsjahr
        self.stammkunde = stammkunde

    @property
    def geburtsjahr(self) -> int:
        """Liefert das Geburtsjahr."""
        return self._geburtsjahr

    @geburtsjahr.setter
    def geburtsjahr(self, wert: int) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if type(wert) is not int or not 1900 <= wert <= date.today().year:
            raise ValueError("Geburtsjahr außerhalb des erlaubten Bereichs")
        self._geburtsjahr = wert

    def alter(self, stichjahr: int | None = None) -> int:
        """Berechnet den Altersunterschied in Kalenderjahren."""
        if stichjahr is None:
            stichjahr = date.today().year
        return stichjahr - self.geburtsjahr

    def rabattsatz(self) -> float:
        """Stammkunden erhalten zwei Prozent."""
        # Rabattsätze sind Dezimalzahlen: 0.02 entspricht zwei Prozent.
        return 0.02 if self.stammkunde else 0.0


class Geschaeftskunde(Kunde):
    """Verwaltet Firma, Umsatzsteuer-ID und Zahlungsziel."""

    def __init__(self, kundennummer: int, name: str, email: str, firmenname: str,
                 ust_id: str, zahlungsziel_tage: int = 14) -> None:
        """Legt ein geprüftes Objekt mit den übergebenen Werten an."""
        # Zuerst legt die Basisklasse die gemeinsamen Kundendaten an.
        super().__init__(kundennummer, name, email)
        self.firmenname = firmenname
        self.ust_id = ust_id
        self.zahlungsziel_tage = zahlungsziel_tage

    @property
    def firmenname(self) -> str:
        """Liefert den Namen der Firma."""
        return self._firmenname

    @firmenname.setter
    def firmenname(self, wert: str) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if not isinstance(wert, str) or not wert.strip():
            raise ValueError("Firmenname darf nicht leer sein")
        self._firmenname = wert.strip()

    @property
    def ust_id(self) -> str:
        """Liefert die normalisierte Umsatzsteuer-ID."""
        return self._ust_id

    @ust_id.setter
    def ust_id(self, wert: str) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if not isinstance(wert, str):
            raise ValueError("USt-ID muss Text sein")
        # Schreibweisen wie de 123 456 789 werden vor der Prüfung vereinheitlicht.
        wert = wert.replace(" ", "").upper()
        if len(wert) != 11 or not wert.startswith("DE") or not wert[2:].isdigit():
            raise ValueError("USt-ID muss aus DE und neun Ziffern bestehen")
        # Erst nach erfolgreicher Prüfung wird der bisherige Wert ersetzt.
        self._ust_id = wert

    @property
    def zahlungsziel_tage(self) -> int:
        """Liefert die Zahlungsfrist in Tagen."""
        return self._zahlungsziel_tage

    @zahlungsziel_tage.setter
    def zahlungsziel_tage(self, wert: int) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if type(wert) is not int or not 0 <= wert <= 60:
            raise ValueError("Zahlungsziel muss zwischen 0 und 60 Tagen liegen")
        self._zahlungsziel_tage = wert

    def begruessung(self) -> str:
        """Begrüßt die Firma förmlich."""
        return f"Sehr geehrte Damen und Herren der {self.firmenname},"

    def rabattsatz(self) -> float:
        """Liefert drei Prozent Firmenrabatt."""
        return 0.03

    def __str__(self) -> str:
        """Liefert die lesbare Darstellung gemäß Aufgabenbeschreibung."""
        return f"Kunde {self.kundennummer}: {self.firmenname} (Ansprechpartner: {self.name})"


class Verein(Kunde):
    """Verwaltet einen Verein und seinen Rabatt."""

    def __init__(self, kundennummer: int, name: str, email: str,
                 registernummer: str, gemeinnuetzig: bool = True) -> None:
        """Legt ein geprüftes Objekt mit den übergebenen Werten an."""
        # Zuerst legt die Basisklasse die gemeinsamen Kundendaten an.
        super().__init__(kundennummer, name, email)
        self.registernummer = registernummer
        self.gemeinnuetzig = gemeinnuetzig

    @property
    def registernummer(self) -> str:
        """Liefert die Vereinsregisternummer."""
        return self._registernummer

    @registernummer.setter
    def registernummer(self, wert: str) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if not isinstance(wert, str) or not wert.startswith("VR ") or not wert[3:].isdigit():
            raise ValueError("Registernummer muss mit VR und einem Leerzeichen beginnen, gefolgt von Ziffern")
        self._registernummer = wert

    def begruessung(self) -> str:
        """Richtet die Begrüßung an den Vorstand."""
        return f"An den Vorstand des Vereins {self.name}"

    def rabattsatz(self) -> float:
        """Gemeinnützige Vereine erhalten fünf Prozent, andere zwei."""
        return 0.05 if self.gemeinnuetzig else 0.02
