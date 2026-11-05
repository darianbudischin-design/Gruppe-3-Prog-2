import re



class Rechnung:
    """Verwaltet Rechnungen für Block B."""

    MWST_SATZ = 0.19

    def __init__(self, nummer: str, kunde: str, netto: float) -> None:
        self.nummer = nummer
        self.kunde = kunde
        self.netto = netto

    def brutto(self, satz: float | None = None) -> float:
        if satz is None:
            satz = self.MWST_SATZ
        return round(self.netto * (1 + satz), 2)

    @classmethod
    def aus_text(cls, text: str) -> "Rechnung":
        nummer, kunde, netto = text.strip().split(";")
        return cls(nummer, kunde, float(netto))

    @staticmethod
    def ist_gueltige_nummer(nummer: str) -> bool:
        return re.fullmatch(r"R-\d{4}-\d{3}", nummer) is not None

    def __str__(self) -> str:
        return f"{self.nummer} ({self.kunde}): {self.netto:.2f} EUR netto"

    def __repr__(self) -> str:
        return f"Rechnung(nummer={self.nummer!r}, kunde={self.kunde!r}, netto={self.netto!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rechnung):
            return NotImplemented
        return self.nummer == other.nummer

    def __hash__(self) -> int:
        return hash(self.nummer)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Rechnung):
            return NotImplemented
        return self.netto < other.netto


class Lagerartikel:
    def __init__(self, bezeichnung, mindestbestand=0):
        self.bezeichnung = bezeichnung
        self._bestand = 0
        self._mindestbestand = 0
        self.mindestbestand = mindestbestand  # läuft durch die Prüfung unten

    @property
    def bestand(self):
        return self._bestand

    @property
    def mindestbestand(self):
        return self._mindestbestand

    @mindestbestand.setter
    def mindestbestand(self, wert):
        if wert < 0:
            raise ValueError("Mindestbestand darf nicht negativ sein")
        self._mindestbestand = wert

    def zugang(self, menge):
        if menge <= 0:
            raise ValueError("Menge muss größer als 0 sein")
        self._bestand += menge

    def abgang(self, menge):
        if menge <= 0:
            raise ValueError("Menge muss größer als 0 sein")
        if menge > self._bestand:
            raise ValueError("Nicht genug Bestand vorhanden")
        self._bestand -= menge

    @property
    def muss_nachbestellt_werden(self):
        return self._bestand < self._mindestbestand