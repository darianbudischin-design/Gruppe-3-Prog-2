from pathlib import Path

from Bestelo.Bestellungen import Bestellung
from Bestelo.Kunden import Geschaeftskunde, Kunde, Privatkunde
from Bestelo.Produkte import Produkt
from Bestelo.Verein import Verein


# Der Pfad wird relativ zu dieser Datei aufgebaut.
CSV_PFAD = Path(__file__).parent / "Daten" / "Produkte.csv"


def beleg_drucken(bestellung: Bestellung) -> None:
    """Gibt einen vollständigen Bestellbeleg aus."""
    print("=" * 50)
    print(
        f"Bestellung {bestellung.bestellnummer} "
        f"({bestellung.status})"
    )
    print(bestellung.kunde.begruessung())
    print("-" * 50)

    for position in bestellung.positionen:
        print(position)

    print("-" * 50)
    print(f"Netto: {bestellung.netto_summe:.2f} €")
    print(
        f"Rabatt {bestellung.kunde.rabattsatz():.0%}: "
        f"-{bestellung.rabatt_betrag:.2f} €"
    )
    print(f"MwSt.: {bestellung.mwst_betrag:.2f} €")
    print(f"Brutto: {bestellung.brutto_summe:.2f} €")


def main() -> None:
    """Zeigt Sortiment, Kundentypen und zwei Beispielbestellungen."""
    produkte = Produkt.aus_csv_datei(CSV_PFAD)

    print("Sortiment (nach Preis):")
    for produkt in sorted(produkte):
        print(produkt)

    anna = Privatkunde(
        1001,
        "Anna Müller",
        "anna@example.com",
        1995,
        stammkunde=True,
    )
    ben = Geschaeftskunde(
        1002,
        "Ben Schmidt",
        "ben@schmidt-it.de",
        "Schmidt IT GmbH",
        "DE123456789",
    )
    verein = Verein(
        1003,
        "SV Musterstadt",
        "info@sv-musterstadt.de",
        "VR 1234",
    )

    kunden: list[Kunde] = [anna, ben, verein]

    for kunde in kunden:
        print(f"{kunde} – {kunde.rabattsatz():.0%} Rabatt")

    # Das Wörterbuch ermöglicht den Zugriff über die Artikelnummer.
    artikel = {
        produkt.artikelnummer: produkt
        for produkt in produkte
    }

    firmenbestellung = Bestellung(ben)
    firmenbestellung.hinzufuegen(artikel["P-1001"], 3)
    firmenbestellung.hinzufuegen(artikel["P-1002"], 6)
    firmenbestellung.abschliessen()
    beleg_drucken(firmenbestellung)

    vereinsbestellung = Bestellung(verein)
    vereinsbestellung.hinzufuegen(artikel["P-1003"], 24)
    print(vereinsbestellung)


if __name__ == "__main__":
    main()