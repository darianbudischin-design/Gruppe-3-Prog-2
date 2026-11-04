from datetime import date


class Kunde:
    """Verwaltet die gemeinsamen Angaben aller Kunden."""

    def __init__(
        self,
        kundennummer: int,
        name: str,
        email: str,
    ) -> None:
        """Legt einen Kunden mit geprüften Angaben an."""
        if type(kundennummer) is not int or kundennummer < 1000:
            raise ValueError("Kundennummer muss eine ganze Zahl ab 1000 sein.")

        self._kundennummer = kundennummer

        # Diese Zuweisungen verwenden die Setter zur Prüfung.
        self.name = name
        self.email = email

    @property
    def kundennummer(self) -> int:
        """Liefert die nur lesbare Kundennummer."""
        return self._kundennummer

    @property
    def name(self) -> str:
        """Liefert den Namen."""
        return self._name

    @name.setter
    def name(self, wert: str) -> None:
        """Prüft und speichert den Namen."""
        wert = wert.strip()

        if not wert:
            raise ValueError("Name darf nicht leer sein.")

        self._name = wert

    @property
    def email(self) -> str:
        """Liefert die E-Mail-Adresse."""
        return self._email

    @email.setter
    def email(self, wert: str) -> None:
        """Prüft und speichert die E-Mail-Adresse."""
        if not self.ist_gueltige_email(wert):
            raise ValueError("Ungültige E-Mail-Adresse.")

        self._email = wert

    @staticmethod
    def ist_gueltige_email(email: str) -> bool:
        """Prüft, ob ein @ und danach ein Punkt vorkommen."""
        _, trennzeichen, hinterer_teil = email.partition("@")
        return trennzeichen == "@" and "." in hinterer_teil

    def begruessung(self) -> str:
        """Liefert eine persönliche Begrüßung."""
        return f"Hallo {self.name}!"

    def rabattsatz(self) -> float:
        """Liefert den Grundrabatt von null Prozent."""
        return 0.0

    def __str__(self) -> str:
        """Liefert eine lesbare Kundendarstellung."""
        return f"Kunde {self.kundennummer}: {self.name}"

    def __repr__(self) -> str:
        """Liefert eine technische Darstellung des Kunden."""
        return (
            f"{type(self).__name__}"
            f"({self.kundennummer}, {self.name!r})"
        )

    def __eq__(self, other: object) -> bool:
        """Vergleicht Kunden anhand ihrer Kundennummer."""
        if not isinstance(other, Kunde):
            return NotImplemented

        return self.kundennummer == other.kundennummer


class Privatkunde(Kunde):
    """Ergänzt einen Kunden um Geburtsjahr und Stammkundenstatus."""

    def __init__(
        self,
        kundennummer: int,
        name: str,
        email: str,
        geburtsjahr: int,
        stammkunde: bool = False,
    ) -> None:
        """Legt einen Privatkunden an."""
        # Die gemeinsamen Angaben übernimmt die Basisklasse.
        super().__init__(kundennummer, name, email)

        self.geburtsjahr = geburtsjahr
        self.stammkunde = stammkunde

    @property
    def geburtsjahr(self) -> int:
        """Liefert das Geburtsjahr."""
        return self._geburtsjahr

    @geburtsjahr.setter
    def geburtsjahr(self, wert: int) -> None:
        """Prüft und speichert das Geburtsjahr."""
        if type(wert) is not int or not 1900 <= wert <= date.today().year:
            raise ValueError(
                "Geburtsjahr muss zwischen 1900 und dem aktuellen Jahr liegen."
            )

        self._geburtsjahr = wert

    def alter(self, stichjahr: int | None = None) -> int:
        """Berechnet die Differenz zwischen Stichjahr und Geburtsjahr."""
        if stichjahr is None:
            stichjahr = date.today().year

        return stichjahr - self.geburtsjahr

    def rabattsatz(self) -> float:
        """Liefert zwei Prozent für Stammkunden, sonst null Prozent."""
        return 0.02 if self.stammkunde else 0.0


class Geschaeftskunde(Kunde):
    """Ergänzt einen Kunden um Firmendaten und Zahlungsfrist."""

    def __init__(
        self,
        kundennummer: int,
        name: str,
        email: str,
        firmenname: str,
        ust_id: str,
        zahlungsziel_tage: int = 14,
    ) -> None:
        """Legt einen Geschäftskunden an."""
        super().__init__(kundennummer, name, email)

        self.firmenname = firmenname
        self.ust_id = ust_id
        self.zahlungsziel_tage = zahlungsziel_tage

    @property
    def firmenname(self) -> str:
        """Liefert den Firmennamen."""
        return self._firmenname

    @firmenname.setter
    def firmenname(self, wert: str) -> None:
        """Prüft und speichert den Firmennamen."""
        wert = wert.strip()

        if not wert:
            raise ValueError("Firmenname darf nicht leer sein.")

        self._firmenname = wert

    @property
    def ust_id(self) -> str:
        """Liefert die normalisierte Umsatzsteuer-ID."""
        return self._ust_id

    @ust_id.setter
    def ust_id(self, wert: str) -> None:
        """Normalisiert und prüft die Umsatzsteuer-ID."""
        wert = wert.replace(" ", "").upper()

        if (
            len(wert) != 11
            or not wert.startswith("DE")
            or not wert[2:].isdigit()
        ):
            raise ValueError("Umsatzsteuer-ID muss DE und neun Ziffern enthalten.")

        self._ust_id = wert

    @property
    def zahlungsziel_tage(self) -> int:
        """Liefert die Zahlungsfrist in Tagen."""
        return self._zahlungsziel_tage

    @zahlungsziel_tage.setter
    def zahlungsziel_tage(self, wert: int) -> None:
        """Prüft und speichert die Zahlungsfrist."""
        if type(wert) is not int or not 0 <= wert <= 60:
            raise ValueError("Zahlungsziel muss zwischen 0 und 60 Tagen liegen.")

        self._zahlungsziel_tage = wert

    def begruessung(self) -> str:
        """Liefert eine förmliche Begrüßung der Firma."""
        return f"Sehr geehrte Damen und Herren der {self.firmenname},"

    def rabattsatz(self) -> float:
        """Liefert drei Prozent Geschäftskundenrabatt."""
        return 0.03

    def __str__(self) -> str:
        """Zeigt die Firma und ihren Ansprechpartner."""
        return (
            f"Kunde {self.kundennummer}: {self.firmenname} "
            f"(Ansprechpartner: {self.name})"
        )