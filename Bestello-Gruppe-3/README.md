# Bestelo – Gruppe 3

Bestelo zeigt Kunden, Produkte und Bestellungen eines allgemeinen Shopsystems.

Diese Fassung ist eine KI-generierte Lernlösung.

## Team

| Rolle | Name | GitHub-Name | Zuständigkeit | Teamleitung |

|Person 1 | eintragen | eintragen | Kunde, Privatkunde, test_kunde.py | eintragen |
|Person 2 | eintragen | eintragen | Geschaeftskunde, Verein, test_kundentypen.py | eintragen |
|Person 3 | eintragen | eintragen | Produkt, CSV-Datei, test_produkt.py | eintragen |
|Person 4 | eintragen | eintragen | Bestellposition, Bestellung, test_bestellung.py | eintragen |
|Person 5 | eintragen | eintragen | Demo, README, UML, test_integration.py | eintragen |

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