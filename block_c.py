"""Übung C1 – Lagerartikel (15 Min., zu zweit, ohne KI)

Ausgangslage:
    Ein Lager verwaltet Artikel. Der Bestand darf nur über Zu- und Abgänge verändert
    werden – nie direkt. Fällt er unter den Mindestbestand, muss nachbestellt werden.

Ihre Aufgabe – Schritt für Schritt:
    1. Klasse Lagerartikel: Konstruktor __init__(self, bezeichnung, mindestbestand=0);
       der Bestand startet bei 0 (intern self._bestand).
    2. Property bestand: nur lesend – KEIN Setter.
    3. Property mindestbestand MIT Setter: negativer Wert -> ValueError.
       Im Konstruktor self.mindestbestand = ... schreiben (läuft durch den Setter).
    4. Berechnete Property muss_nachbestellt_werden: True, wenn Bestand < Mindestbestand.
    5. zugang(menge) und abgang(menge): Menge <= 0 -> ValueError;
       Abgang größer als Bestand -> ValueError.

Vorlage: beispiele/konto.py (gleicher Aufbau: saldo ~ bestand, dispo ~ mindestbestand,
verfuegbar ~ muss_nachbestellt_werden)
Fertig, wenn pytest -k block_c "6 passed" meldet und Ihre Ausgabe so aussieht:
    7 True
    bestand ist schreibgeschützt
"""


class Lagerartikel:
    """Verwaltet einen Lagerartikel mit Bestand und Mindestbestand."""

    def __init__(
        self, bezeichnung: str, mindestbestand: int = 0
    ) -> None:
        self.bezeichnung = bezeichnung
        self._bestand = 0
        self.mindestbestand = mindestbestand

    @property
    def bestand(self) -> int:
        """Liefert den aktuellen Bestand."""
        return self._bestand

    @property
    def mindestbestand(self) -> int:
        """Liefert den Mindestbestand."""
        return self._mindestbestand

    @mindestbestand.setter
    def mindestbestand(self, wert: int) -> None:
        if wert < 0:
            raise ValueError("Mindestbestand darf nicht negativ sein.")
        self._mindestbestand = wert

    @property
    def muss_nachbestellt_werden(self) -> bool:
        """Zeigt an, ob der Bestand unter dem Mindestbestand liegt."""
        return self._bestand < self.mindestbestand

    def zugang(self, menge: int) -> None:
        """Erhöht den Bestand um eine positive Menge."""
        if menge <= 0:
            raise ValueError("Die Menge muss größer als 0 sein.")
        self._bestand += menge

    def abgang(self, menge: int) -> None:
        """Verringert den Bestand um eine verfügbare positive Menge."""
        if menge <= 0:
            raise ValueError("Die Menge muss größer als 0 sein.")
        if menge > self._bestand:
            raise ValueError("Nicht genügend Bestand vorhanden.")
        self._bestand -= menge
