"""Produkte und CSV-Import."""
from __future__ import annotations

from math import isfinite
from pathlib import Path


class Produkt:
    """Beschreibt einen Artikel mit Netto- und Bruttopreis."""

    # Klassenattribute gelten gemeinsam für alle Produkte.
    KATEGORIEN = ("Lebensmittel", "Getränke", "Bücher", "Haushalt", "Elektronik", "Sonstiges")
    ERMAESSIGTE_KATEGORIEN = ("Lebensmittel", "Bücher")
    MWST_ERMAESSIGT = 0.07
    MWST_REGULAER = 0.19

    def __init__(self, artikelnummer: str, bezeichnung: str, nettopreis: float,
                 kategorie: str = "Sonstiges") -> None:
        """Legt ein geprüftes Objekt mit den übergebenen Werten an."""
        if (not isinstance(artikelnummer, str) or len(artikelnummer) != 6
                or not artikelnummer.startswith("P-") or not artikelnummer[2:].isdigit()):
            raise ValueError("Artikelnummer muss dem Muster P-1234 entsprechen")
        self._artikelnummer = artikelnummer
        # Diese drei Zuweisungen verwenden die prüfenden Setter.
        self.bezeichnung = bezeichnung
        self.nettopreis = nettopreis
        self.kategorie = kategorie

    @property
    def artikelnummer(self) -> str:
        """Liefert die feste Artikelnummer."""
        return self._artikelnummer

    @property
    def bezeichnung(self) -> str:
        """Liefert den Artikelnamen."""
        return self._bezeichnung

    @bezeichnung.setter
    def bezeichnung(self, wert: str) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if not isinstance(wert, str) or not wert.strip():
            raise ValueError("Bezeichnung darf nicht leer sein")
        self._bezeichnung = wert.strip()

    @property
    def nettopreis(self) -> float:
        """Liefert den Nettopreis pro Stück."""
        return self._nettopreis

    @nettopreis.setter
    def nettopreis(self, wert: float) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if type(wert) not in (int, float) or not isfinite(wert) or wert <= 0:
            raise ValueError("Nettopreis muss eine positive endliche Zahl sein")
        # Die Aufgabe verwendet float und rundet Geldbeträge auf Cent.
        self._nettopreis = round(float(wert), 2)

    @property
    def kategorie(self) -> str:
        """Liefert die Produktkategorie."""
        return self._kategorie

    @kategorie.setter
    def kategorie(self, wert: str) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if wert not in self.KATEGORIEN:
            raise ValueError("Unbekannte Kategorie")
        self._kategorie = wert

    # Berechnete Properties werden beim Zugriff aus den aktuellen Daten ermittelt.
    @property
    def mwst_satz(self) -> float:
        """Bestimmt den Steuersatz aus der aktuellen Kategorie."""
        if self.kategorie in self.ERMAESSIGTE_KATEGORIEN:
            return self.MWST_ERMAESSIGT
        return self.MWST_REGULAER

    @property
    def bruttopreis(self) -> float:
        """Berechnet den Bruttopreis pro Stück."""
        return round(self.nettopreis * (1 + self.mwst_satz), 2)

    # cls bezeichnet die aufgerufene Klasse und ermöglicht einen alternativen Konstruktor.
    @classmethod
    def aus_csv_zeile(cls, zeile: str) -> Produkt:
        """Liest einen Artikel aus vier durch Semikolon getrennten Feldern."""
        # Eine CSV-Zeile enthält vier Felder, getrennt durch Semikolon.
        nummer, name, preis, kategorie = zeile.strip().split(";")
        return cls(nummer, name, float(preis), kategorie)

    @classmethod
    def aus_csv_datei(cls, pfad: str | Path) -> list[Produkt]:
        """Liest alle Datenzeilen nach der Kopfzeile."""
        with open(pfad, encoding="utf-8") as datei:
            # Die erste Zeile enthält die Spaltennamen und kein Produkt.
            next(datei, None)
            # Leerzeilen überspringen; die übrigen Zeilen in Objekte umwandeln.
            return [cls.aus_csv_zeile(zeile) for zeile in datei if zeile.strip()]

    def __str__(self) -> str:
        """Liefert die lesbare Darstellung gemäß Aufgabenbeschreibung."""
        return f"{self.artikelnummer} {self.bezeichnung} – {self.nettopreis:.2f} € netto"

    def __repr__(self) -> str:
        """Liefert die technische Darstellung des Objekts."""
        return (f"Produkt({self.artikelnummer!r}, {self.bezeichnung!r}, "
                f"{self.nettopreis!r}, {self.kategorie!r})")

    def __eq__(self, other: object) -> bool:
        """Vergleicht die fachliche Identität anhand der Nummer."""
        if not isinstance(other, Produkt):
            return NotImplemented
        # Fachlich zählt die Artikelnummer, unabhängig von Name oder Preis.
        return self.artikelnummer == other.artikelnummer

    def __lt__(self, other: object) -> bool:
        """Vergleicht die Nettopreise zweier Produkte."""
        if not isinstance(other, Produkt):
            return NotImplemented
        # sorted(), min() und max() können damit Preise vergleichen.
        return self.nettopreis < other.nettopreis
