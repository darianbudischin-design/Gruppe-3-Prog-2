"""Bestellpositionen und Berechnung der Bestellsummen."""
from bestelo.kunden import Kunde
from bestelo.produkte import Produkt


class Bestellposition:
    """Verbindet ein Produkt mit einer positiven Stückzahl."""

    def __init__(self, produkt: Produkt, menge: int = 1) -> None:
        """Legt ein geprüftes Objekt mit den übergebenen Werten an."""
        self._produkt = produkt
        # Der Setter prüft die Menge schon beim Erstellen der Position.
        self.menge = menge

    @property
    def produkt(self) -> Produkt:
        """Liefert das bestellte Produkt."""
        return self._produkt

    @property
    def menge(self) -> int:
        """Liefert die Stückzahl."""
        return self._menge

    @menge.setter
    def menge(self, wert: int) -> None:
        """Prüft den neuen Wert vor dem Speichern."""
        if type(wert) is not int or wert < 1:
            raise ValueError("Menge muss eine positive ganze Zahl sein")
        self._menge = wert

    @property
    def netto(self) -> float:
        """Berechnet den Nettobetrag für alle Stücke."""
        return round(self.produkt.nettopreis * self.menge, 2)

    @property
    def mwst(self) -> float:
        """Berechnet die Steuer auf den Positionsnettobetrag."""
        # Zuerst wird die Positionssteuer gerundet; die Bestellung summiert diese Werte.
        return round(self.netto * self.produkt.mwst_satz, 2)

    @property
    def brutto(self) -> float:
        """Addiert den Nettobetrag und die gerundete Steuer."""
        return round(self.netto + self.mwst, 2)

    def __str__(self) -> str:
        """Liefert die lesbare Darstellung gemäß Aufgabenbeschreibung."""
        return (f"{self.menge} × {self.produkt.bezeichnung} "
                f"à {self.produkt.nettopreis:.2f} € = {self.netto:.2f} €")


class Bestellung:
    """Sammelt Bestellpositionen für einen Kunden."""

    # Ein gemeinsamer Zähler vergibt Nummern über alle Bestellobjekte hinweg.
    _naechste_nummer = 1

    def __init__(self, kunde: Kunde) -> None:
        """Legt ein geprüftes Objekt mit den übergebenen Werten an."""
        self._kunde = kunde
        self._bestellnummer = f"B-{Bestellung._naechste_nummer:04d}"
        # Über den Klassennamen erhöhen, damit alle Bestellungen denselben Zähler nutzen.
        Bestellung._naechste_nummer += 1
        self._status = "offen"
        # Jede Bestellung erhält eine eigene leere Liste.
        self._positionen: list[Bestellposition] = []

    @property
    def bestellnummer(self) -> str:
        """Liefert die beim Anlegen vergebene Nummer."""
        return self._bestellnummer

    @property
    def kunde(self) -> Kunde:
        """Liefert den bestellenden Kunden."""
        return self._kunde

    @property
    def status(self) -> str:
        """Liefert den aktuellen Bestellstatus."""
        return self._status

    @property
    def positionen(self) -> list[Bestellposition]:
        """Gibt eine Kopie der Positionsliste zurück."""
        # Die Listenkopie schützt vor append/clear von außen. Die Objekte darin sind dieselben.
        return list(self._positionen)

    def hinzufuegen(self, produkt: Produkt, menge: int = 1) -> None:
        """Fügt eine Position hinzu oder erhöht die Menge eines vorhandenen Artikels."""
        if self.status != "offen":
            raise ValueError("Bestellung ist bereits abgeschlossen")
        # Vor jeder Änderung die hinzugefügte Menge prüfen, auch bei vorhandenen Artikeln.
        neu = Bestellposition(produkt, menge)
        for position in self._positionen:
            # Produkt.__eq__ erkennt gleiche Artikel an ihrer Nummer.
            if position.produkt == produkt:
                position.menge += neu.menge
                return
        self._positionen.append(neu)

    def abschliessen(self) -> None:
        """Schließt eine nicht leere Bestellung ab."""
        if not self._positionen:
            raise ValueError("Leere Bestellung kann nicht abgeschlossen werden")
        # Derselbe Status kann erneut gesetzt werden, ohne etwas weiter zu ändern.
        self._status = "abgeschlossen"

    @property
    def netto_summe(self) -> float:
        """Addiert die Nettobeträge aller Positionen."""
        return round(sum((p.netto for p in self._positionen), 0.0), 2)

    @property
    def rabatt_betrag(self) -> float:
        """Berechnet den Nachlass für diesen Kunden."""
        # Polymorphie: Jeder Kundentyp liefert seinen Rabatt über dieselbe Methode.
        return round(self.netto_summe * self.kunde.rabattsatz(), 2)

    @property
    def netto_nach_rabatt(self) -> float:
        """Zieht den gerundeten Rabatt vom Nettobetrag ab."""
        return round(self.netto_summe - self.rabatt_betrag, 2)

    @property
    def mwst_betrag(self) -> float:
        """Reduziert auch die summierte Positionssteuer um den Kundenrabatt."""
        # Auch die bereits summierte Steuer wird anteilig um den Rabatt reduziert.
        steuer = sum(p.mwst for p in self._positionen)
        return round(steuer * (1 - self.kunde.rabattsatz()), 2)

    @property
    def brutto_summe(self) -> float:
        """Berechnet den Rechnungsbetrag inklusive Steuer."""
        return round(self.netto_nach_rabatt + self.mwst_betrag, 2)

    def __len__(self) -> int:
        """Liefert die Anzahl unterschiedlicher Bestellpositionen."""
        # Zwei verschiedene Artikel sind zwei Positionen, unabhängig von den Stückzahlen.
        return len(self._positionen)

    def __str__(self) -> str:
        """Liefert die lesbare Darstellung gemäß Aufgabenbeschreibung."""
        return (f"Bestellung {self.bestellnummer} ({self.status}) für {self.kunde.name}: "
                f"{len(self)} Position(en), {self.brutto_summe:.2f} € brutto")
