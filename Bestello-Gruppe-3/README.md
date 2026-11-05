# Bestelo – Gruppe 3

Bestelo zeigt Kunden, Produkte und Bestellungen eines allgemeinen Shopsystems.

## Starten

Voraussetzungen: Python ab 3.10 und pytest.

Alle Befehle im Ordner ausführen, der Bestelo, Tests und pytest.ini enthält.

python -m pip install pytest
python -m Bestelo
python -m pytest -v (alle tests gleichzeitig)

- Beispiel: Nur die Kundentests im Terminal starten

python -m pytest Tests/test_kunde.py -v


Die Demo enthält eine Firmenbestellung über 79,66 € und eine
Vereinsbestellung über 75,97 €.

## Dateien

- Bestelo/Kunden.py: Kunde, Privatkunde und Geschäftskunde
- Bestelo/Verein.py: Verein
- Bestelo/Produkte.py: Produkt und CSV-Import
- Bestelo/Bestellungen.py: Bestellposition und Bestellung
- Bestelo/__main__.py: Konsolen-Demo
- Bestelo/Daten/Produkte.csv: sechs vorgegebene Produkte
- Tests: 18 Tests, verteilt auf fünf Dateien


## UML-Klassendiagramm

```mermaid
classDiagram
    direction TB

    class Kunde {
        +kundennummer : int
        +name : str
        +email : str
        +__init__(kundennummer, name, email)
        +ist_gueltige_email(email) bool$
        +begruessung() str
        +rabattsatz() float
        +__str__() str
        +__repr__() str
        +__eq__(other) bool
    }

    class Privatkunde {
        +geburtsjahr : int
        +stammkunde : bool
        +__init__(kundennummer, name, email, geburtsjahr, stammkunde=False)
        +alter(stichjahr=None) int
        +rabattsatz() float
    }

    class Geschaeftskunde {
        +firmenname : str
        +ust_id : str
        +zahlungsziel_tage : int
        +__init__(kundennummer, name, email, firmenname, ust_id, zahlungsziel_tage=14)
        +begruessung() str
        +rabattsatz() float
        +__str__() str
    }

    class Verein {
        +registernummer : str
        +gemeinnuetzig : bool
        +__init__(kundennummer, name, email, registernummer, gemeinnuetzig=True)
        +begruessung() str
        +rabattsatz() float
    }

    class Produkt {
        +KATEGORIEN : tuple$
        +ERMAESSIGTE_KATEGORIEN : tuple$
        +MWST_ERMAESSIGT : float$
        +MWST_REGULAER : float$
        +artikelnummer : str
        +bezeichnung : str
        +nettopreis : float
        +kategorie : str
        +mwst_satz : float
        +bruttopreis : float
        +__init__(artikelnummer, bezeichnung, nettopreis, kategorie="Sonstiges")
        +aus_csv_zeile(zeile) Produkt$
        +aus_csv_datei(pfad) list~Produkt~$
        +__str__() str
        +__repr__() str
        +__eq__(other) bool
        +__lt__(other) bool
    }

    class Bestellposition {
        +produkt : Produkt
        +menge : int
        +netto : float
        +mwst : float
        +brutto : float
        +__init__(produkt, menge=1)
        +__str__() str
    }

    class Bestellung {
        -_naechste_nummer : int$
        +bestellnummer : str
        +kunde : Kunde
        +status : str
        +positionen : list~Bestellposition~
        +netto_summe : float
        +rabatt_betrag : float
        +netto_nach_rabatt : float
        +mwst_betrag : float
        +brutto_summe : float
        +__init__(kunde)
        +hinzufuegen(produkt, menge=1) None
        +abschliessen() None
        +__len__() int
        +__str__() str
    }

    Kunde <|-- Privatkunde
    Kunde <|-- Geschaeftskunde
    Kunde <|-- Verein

    Bestellung "0..*" --> "1" Kunde : gehört zu
    Bestellung "1" *-- "0..*" Bestellposition : enthält
    Bestellposition "0..*" --> "1" Produkt : verweist auf

    note for Kunde "kundennummer: nur lesbar\nname und email: prüfende Setter"
    note for Privatkunde "geburtsjahr: prüfender Setter\nstammkunde: bool, Standard False"
    note for Geschaeftskunde "firmenname, ust_id und zahlungsziel_tage:\nprüfende Setter"
    note for Verein "registernummer: prüfender Setter\ngemeinnuetzig: bool, Standard True"
    note for Produkt "artikelnummer: nur lesbar\nbezeichnung, nettopreis, kategorie: prüfende Setter\nmwst_satz und bruttopreis: berechnet"
    note for Bestellposition "produkt: nur lesbar\nmenge: prüfender Setter\nnetto, mwst und brutto: berechnet"
    note for Bestellung "bestellnummer, kunde und status: nur lesbar\npositionen: flache Listenkopie\nalle fünf Geldbeträge: berechnet"
```

### Legende

- `+` bedeutet öffentlich; `-` kennzeichnet interne Elemente.
- `$` kennzeichnet klassenbezogene Attribute und Methoden.
- `<|--` bedeutet Vererbung.
- `-->` bedeutet eine Beziehung zu einem anderen Objekt.
- `*--` bedeutet Komposition: Die Positionen gehören zur Bestellung.
- `1` bedeutet genau ein Objekt.
- `0..*` bedeutet beliebig viele Objekte, einschließlich keines.
- Geerbte Eigenschaften und Methoden werden in Unterklassen nicht erneut aufgeführt.