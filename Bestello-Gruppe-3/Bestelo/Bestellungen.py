from Bestelo.Kunden import Kunde
from Bestelo.Produkte import Produkt


class Bestellposition:
    """Verbindet ein Produkt mit einer bestellten Menge."""

    def __init__(self, produkt: Produkt, menge: int = 1) -> None:
        """Legt eine Position mit geprüfter Menge an."""
        self._produkt = produkt
        self.menge = menge

    @property
    def produkt(self) -> Produkt:
        """Liefert das zugeordnete Produkt."""
        return self._produkt

    @property
    def menge(self) -> int:
        """Liefert die bestellte Menge."""
        return self._menge

    @menge.setter
    def menge(self, wert: int) -> None:
        """Prüft und speichert eine ganze Menge von mindestens eins."""
        if type(wert) is not int or wert < 1:
            raise ValueError("Menge muss eine ganze Zahl von mindestens 1 sein.")

        self._menge = wert

    @property
    def netto(self) -> float:
        """Berechnet den Nettobetrag der Position."""
        return round(self.produkt.nettopreis * self.menge, 2)

    @property
    def mwst(self) -> float:
        """Berechnet die Mehrwertsteuer vor dem Bestellrabatt."""
        return round(self.netto * self.produkt.mwst_satz, 2)

    @property
    def brutto(self) -> float:
        """Berechnet den Bruttobetrag vor dem Bestellrabatt."""
        return round(self.netto + self.mwst, 2)

    def __str__(self) -> str:
        """Liefert eine lesbare Bestellzeile."""
        return (
            f"{self.menge} × {self.produkt.bezeichnung} "
            f"à {self.produkt.nettopreis:.2f} € = {self.netto:.2f} €"
        )


class Bestellung:
    """Verwaltet die Positionen und Beträge einer Kundenbestellung."""

    # Dieser Zähler gehört zur Klasse, nicht zu einem einzelnen Objekt.
    _naechste_nummer = 1

    def __init__(self, kunde: Kunde) -> None:
        """Legt eine offene Bestellung mit fortlaufender Nummer an."""
        self._bestellnummer = f"B-{Bestellung._naechste_nummer:04d}"
        Bestellung._naechste_nummer += 1

        self._kunde = kunde
        self._status = "offen"
        self._positionen: list[Bestellposition] = []

    @property
    def bestellnummer(self) -> str:
        """Liefert die Bestellnummer."""
        return self._bestellnummer

    @property
    def kunde(self) -> Kunde:
        """Liefert den zugeordneten Kunden."""
        return self._kunde

    @property
    def status(self) -> str:
        """Liefert den aktuellen Bestellstatus."""
        return self._status

    @property
    def positionen(self) -> list[Bestellposition]:
        """Liefert eine flache Kopie der Positionsliste."""
        return list(self._positionen)

    @property
    def netto_summe(self) -> float:
        """Berechnet die Nettosumme aller Positionen."""
        return round(sum(position.netto for position in self._positionen), 2)

    @property
    def rabatt_betrag(self) -> float:
        """Berechnet den Rabatt anhand des Kundentyps."""
        # Der Kunde bestimmt seinen Rabatt selbst: Polymorphie.
        return round(self.netto_summe * self.kunde.rabattsatz(), 2)

    @property
    def netto_nach_rabatt(self) -> float:
        """Berechnet den Nettobetrag nach Rabatt."""
        return round(self.netto_summe - self.rabatt_betrag, 2)

    @property
    def mwst_betrag(self) -> float:
        """Berechnet die Mehrwertsteuer nach Rabatt."""
        steuer_vor_rabatt = sum(
            position.mwst for position in self._positionen
        )

        return round(
            steuer_vor_rabatt * (1 - self.kunde.rabattsatz()),
            2,
        )

    @property
    def brutto_summe(self) -> float:
        """Berechnet den endgültigen Gesamtbetrag."""
        return round(self.netto_nach_rabatt + self.mwst_betrag, 2)

    def hinzufuegen(self, produkt: Produkt, menge: int = 1) -> None:
        """Ergänzt ein Produkt oder erhöht dessen vorhandene Menge."""
        if self.status != "offen":
            raise ValueError("Bestellung ist bereits abgeschlossen.")

        if type(menge) is not int or menge < 1:
            raise ValueError("Menge muss eine ganze Zahl von mindestens 1 sein.")

        for position in self._positionen:
            # Produkt.__eq__ vergleicht die Artikelnummer.
            if position.produkt == produkt:
                position.menge += menge
                return

        self._positionen.append(Bestellposition(produkt, menge))

    def abschliessen(self) -> None:
        """Schließt eine nicht leere Bestellung ab."""
        if not self._positionen:
            raise ValueError("Eine leere Bestellung kann nicht abgeschlossen werden.")

        # Wiederholtes Abschließen verändert den Status nicht weiter.
        self._status = "abgeschlossen"

    def __len__(self) -> int:
        """Liefert die Anzahl unterschiedlicher Positionen."""
        return len(self._positionen)

    def __str__(self) -> str:
        """Liefert eine kurze Zusammenfassung der Bestellung."""
        return (
            f"Bestellung {self.bestellnummer} ({self.status}) "
            f"für {self.kunde.name}: {len(self)} Position(en), "
            f"{self.brutto_summe:.2f} € brutto"
        )