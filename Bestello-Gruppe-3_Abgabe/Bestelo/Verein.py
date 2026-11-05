from Bestelo.Kunden import Kunde


class Verein(Kunde):
    """Ergänzt einen Kunden um Vereinsregister und Gemeinnützigkeit."""

    def __init__(
        self,
        kundennummer: int,
        name: str,
        email: str,
        registernummer: str,
        gemeinnuetzig: bool = True,
    ) -> None:
        """Legt einen Verein mit geprüfter Registernummer an."""
        super().__init__(kundennummer, name, email)

        self.registernummer = registernummer
        self.gemeinnuetzig = gemeinnuetzig

    @property
    def registernummer(self) -> str:
        """Liefert die Vereinsregisternummer."""
        return self._registernummer

    @registernummer.setter
    def registernummer(self, wert: str) -> None:
        """Prüft das Format VR mit Leerzeichen und anschließenden Ziffern."""
        if not wert.startswith("VR ") or not wert[3:].isdigit():
            raise ValueError(
                "Registernummer muss mit 'VR ' beginnen, gefolgt von Ziffern."
            )

        self._registernummer = wert

    def begruessung(self) -> str:
        """Liefert die Begrüßung des Vereinsvorstands."""
        return f"An den Vorstand des Vereins {self.name}"

    def rabattsatz(self) -> float:
        """Liefert fünf Prozent bei Gemeinnützigkeit, sonst zwei Prozent."""
        return 0.05 if self.gemeinnuetzig else 0.02