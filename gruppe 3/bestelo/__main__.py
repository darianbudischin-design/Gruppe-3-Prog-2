"""Startet die Konsolen-Demo mit python -m bestelo."""
from pathlib import Path

from bestelo.bestellungen import Bestellung
from bestelo.kunden import Geschaeftskunde, Kunde, Privatkunde, Verein
from bestelo.produkte import Produkt

# __file__ ist diese Python-Datei. Dadurch ist der Datenpfad stabil.
CSV_PFAD = Path(__file__).parent / "daten" / "produkte.csv"


def beleg_drucken(bestellung: Bestellung) -> None:
    """Gibt Positionen, Rabatt und Endbetrag als Beleg aus."""
    print("=" * 50)
    print(f"Bestellung {bestellung.bestellnummer} ({bestellung.status})")
    print(bestellung.kunde.begruessung())
    print("-" * 50)
    for position in bestellung.positionen:
        print(position)
    print("-" * 50)
    print(f"Netto: {bestellung.netto_summe:.2f} €")
    print(f"Rabatt {bestellung.kunde.rabattsatz():.0%}: -{bestellung.rabatt_betrag:.2f} €")
    print(f"MwSt.: {bestellung.mwst_betrag:.2f} €")
    print(f"Brutto: {bestellung.brutto_summe:.2f} €")


def main() -> None:
    """Zeigt Sortiment, Kundentypen und zwei Beispielbestellungen."""
    produkte = Produkt.aus_csv_datei(CSV_PFAD)
    # Das Wörterbuch findet Produkte direkt über ihre Artikelnummer.
    artikel = {p.artikelnummer: p for p in produkte}
    print("Sortiment (nach Preis):")
    # sorted verwendet den Preisvergleich Produkt.__lt__.
    for produkt in sorted(produkte):
        print(produkt)

        anna = Privatkunde("Anna Müller", "anna@example.com", 1001, 1995, stammkunde=True)
    ben = Geschaeftskunde("Ben Schmidt", "ben@schmidt-it.de", 1002,
                          "Schmidt IT GmbH", "DE123456789")
    verein = Verein("SV Musterstadt", "info@sv-musterstadt.de", 1003, "VR 1234")
    kunden: list[Kunde] = [anna, ben, verein]
    # In einer gemeinsamen Liste können unterschiedliche Kundentypen stehen.
    for kunde in kunden:
        print(f"{kunde} – {kunde.rabattsatz():.0%} Rabatt")

    firma = Bestellung(ben)
    firma.hinzufuegen(artikel["P-1001"], 3)
    firma.hinzufuegen(artikel["P-1002"], 6)
    # Nach dem Abschluss lehnt hinzufuegen weitere Änderungen ab.
    firma.abschliessen()
    beleg_drucken(firma)

    saft = Bestellung(verein)
    saft.hinzufuegen(artikel["P-1003"], 24)
    print(saft)


# Beim Import in Tests startet die Demo nicht automatisch.
if __name__ == "__main__":
    main()
