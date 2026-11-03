class Kunde:
    """Verwaltet die gemeinsamen Daten und das Verhalten aller Kunden."""

    def __init__(
        self,
        kundennummer: int,
        name: str,
        email: str,
    ) -> None:
        """Legt einen Kunden mit geprüften Angaben an."""
        if kundennummer < 1000:
            raise ValueError("Kundennummer muss mindestens 1000 sein.")

        self._kundennummer = kundennummer

        # Die Zuweisungen rufen die Setter auf und prüfen die Werte.
        self.name = name
        self.email = email

    @property
    def kundennummer(self) -> int:
        """Liefert die unveränderbare Kundennummer."""
        return self._kundennummer

    @property
    def name(self) -> str:
        """Liefert den Namen."""
        return self._name

    @name.setter
    def name(self, wert: str) -> None:
        """Prüft und speichert den Namen ohne äußere Leerzeichen."""
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
        """Speichert die E-Mail-Adresse nach erfolgreicher Prüfung."""
        if not self.ist_gueltige_email(wert):
            raise ValueError("Ungültige E-Mail-Adresse.")

        self._email = wert

    @staticmethod
    def ist_gueltige_email(email: str) -> bool:
        """Prüft, ob ein @ und danach ein Punkt vorkommen."""
        # partition zerlegt den Text am ersten @ in drei Teile.
        _, trennzeichen, hinterer_teil = email.partition("@")
        return trennzeichen == "@" and "." in hinterer_teil

    def begruessung(self) -> str:
        """Liefert die persönliche Begrüßung."""
        return f"Hallo {self.name}!"

    def rabattsatz(self) -> float:
        """Liefert den Grundrabatt von null Prozent."""
        return 0.0

    def __str__(self) -> str:
        """Liefert die lesbare Kundendarstellung."""
        return f"Kunde {self.kundennummer}: {self.name}"

    def __repr__(self) -> str:
        """Liefert eine technische Darstellung mit dem Klassennamen."""
        # Bei einer Unterklasse erscheint automatisch deren Name.
        return (
            f"{type(self).__name__}"
            f"({self.kundennummer}, {self.name!r})"
        )

    def __eq__(self, other: object) -> bool:
        """Vergleicht Kunden anhand ihrer Kundennummer."""
        if not isinstance(other, Kunde):
            return NotImplemented

        return self.kundennummer == other.kundennummer