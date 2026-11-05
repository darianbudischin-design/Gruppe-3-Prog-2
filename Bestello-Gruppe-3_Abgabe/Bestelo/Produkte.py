from pathlib import Path


class Produkt:
    """Beschreibt einen Artikel mit Nettopreis und Kategorie."""

    KATEGORIEN = (
        "Lebensmittel",
        "Getränke",
        "Bücher",
        "Haushalt",
        "Elektronik",
        "Sonstiges",
    )
    ERMAESSIGTE_KATEGORIEN = ("Lebensmittel", "Bücher")
    MWST_ERMAESSIGT = 0.07
    MWST_REGULAER = 0.19

    def __init__(
        self,
        artikelnummer: str,
        bezeichnung: str,
        nettopreis: float,
        kategorie: str = "Sonstiges",
    ) -> None:
        """Legt ein Produkt mit geprüften Angaben an."""
        if (
            len(artikelnummer) != 6
            or not artikelnummer.startswith("P-")
            or not artikelnummer[2:].isdigit()
        ):
            raise ValueError("Artikelnummer muss aus P- und vier Ziffern bestehen.")

        self._artikelnummer = artikelnummer
        self.bezeichnung = bezeichnung
        self.nettopreis = nettopreis
        self.kategorie = kategorie

    @property
    def artikelnummer(self) -> str:
        """Liefert die nur lesbare Artikelnummer."""
        return self._artikelnummer

    @property
    def bezeichnung(self) -> str:
        """Liefert die Produktbezeichnung."""
        return self._bezeichnung

    @bezeichnung.setter
    def bezeichnung(self, wert: str) -> None:
        """Prüft und speichert die Produktbezeichnung."""
        wert = wert.strip()

        if not wert:
            raise ValueError("Bezeichnung darf nicht leer sein.")

        self._bezeichnung = wert

    @property
    def nettopreis(self) -> float:
        """Liefert den Nettopreis."""
        return self._nettopreis

    @nettopreis.setter
    def nettopreis(self, wert: float) -> None:
        """Prüft den positiven Preis und rundet ihn auf Cent."""
        if wert <= 0:
            raise ValueError("Nettopreis muss größer als null sein.")

        self._nettopreis = round(float(wert), 2)

    @property
    def kategorie(self) -> str:
        """Liefert die Produktkategorie."""
        return self._kategorie

    @kategorie.setter
    def kategorie(self, wert: str) -> None:
        """Prüft, ob die Kategorie erlaubt ist."""
        if wert not in self.KATEGORIEN:
            raise ValueError("Unbekannte Kategorie.")

        self._kategorie = wert

    @property
    def mwst_satz(self) -> float:
        """Ermittelt den Mehrwertsteuersatz aus der Kategorie."""
        if self.kategorie in self.ERMAESSIGTE_KATEGORIEN:
            return self.MWST_ERMAESSIGT

        return self.MWST_REGULAER

    @property
    def bruttopreis(self) -> float:
        """Berechnet den Einzelpreis einschließlich Mehrwertsteuer."""
        return round(self.nettopreis * (1 + self.mwst_satz), 2)

    @classmethod
    def aus_csv_zeile(cls, zeile: str) -> "Produkt":
        """Erzeugt ein Produkt aus einer CSV-Datenzeile."""
        artikelnummer, bezeichnung, preis, kategorie = zeile.strip().split(";")

        # cls erzeugt ein Objekt der aufrufenden Klasse.
        return cls(artikelnummer, bezeichnung, float(preis), kategorie)

    @classmethod
    def aus_csv_datei(cls, pfad: str | Path) -> list["Produkt"]:
        """Liest Produkte aus einer UTF-8-Datei mit Kopfzeile."""
        produkte = []

        with open(pfad, encoding="utf-8") as datei:
            next(datei, None)  # Kopfzeile überspringen.

            for zeile in datei:
                if zeile.strip():  # Leere Zeilen überspringen.
                    produkte.append(cls.aus_csv_zeile(zeile))

        return produkte

    def __str__(self) -> str:
        """Liefert Artikelnummer, Bezeichnung und Nettopreis."""
        return (
            f"{self.artikelnummer} {self.bezeichnung} "
            f"– {self.nettopreis:.2f} € netto"
        )

    def __repr__(self) -> str:
        """Liefert eine technische Darstellung des Produkts."""
        return (
            f"Produkt({self.artikelnummer!r}, {self.bezeichnung!r}, "
            f"{self.nettopreis!r}, {self.kategorie!r})"
        )

    def __eq__(self, other: object) -> bool:
        """Vergleicht Produkte anhand der Artikelnummer."""
        if not isinstance(other, Produkt):
            return NotImplemented

        return self.artikelnummer == other.artikelnummer

    def __lt__(self, other: object) -> bool:
        """Vergleicht die Nettopreise zum Sortieren."""
        if not isinstance(other, Produkt):
            return NotImplemented

        return self.nettopreis < other.nettopreis