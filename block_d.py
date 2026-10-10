"""Übung D1 – Verein als dritte Kundenart (10 Min., zu zweit, ohne KI)

Ausgangslage:
    Bestelo kennt schon Privat- und Geschäftskunden (Datei kunden.py). Jetzt kommen
    Vereine dazu – ohne dass bestehender Code geändert werden muss.

Ihre Aufgabe – Schritt für Schritt:
    1. class Verein(Kunde); Konstruktor mit name, email, kundennummer,
       vereinsregisternummer – zuerst super().__init__(...).
    2. begruessung() überschreiben -> "An den Vorstand des Vereins TSG Haßloch"
    3. rabattsatz() überschreiben -> Vereine bekommen 0.05 (5 %).
    4. Im __main__-Block: je ein Privatkunde, Geschäftskunde und Verein in einer Liste –
       in einer Schleife Begrüßung und Rabatt ausgeben.
    5. Zu Hause: Mermaid-Diagramm um Verein ergänzen.
       Bonus: umsatzsteuer_pflichtig() erst mit isinstance, dann polymorph lösen.

Vorlage: Geschaeftskunde in kunden.py
Fertig, wenn pytest -k block_d "4 passed" meldet und Ihre Ausgabe so aussieht:
    Hallo Anna Müller! – 0% Rabatt
    Sehr geehrte Damen und Herren der Schmidt IT GmbH, – 3% Rabatt
    An den Vorstand des Vereins TSG Haßloch – 5% Rabatt
"""
from kunden import Geschaeftskunde, Kunde, Privatkunde  # noqa: F401


class Verein(Kunde):
    pass  # TODO D1


if __name__ == "__main__":
    # kunden: list[Kunde] = [
    #     Privatkunde("Anna Müller", "anna@example.com", 1001, 1995),
    #     Geschaeftskunde("Ben Schmidt", "ben@schmidt-it.de", 1002,
    #                     "Schmidt IT GmbH", "DE123456789"),
    #     Verein("TSG Haßloch", "info@tsg.de", 1003, "VR 1234"),
    # ]
    # for k in kunden:
    #     print(f"{k.begruessung()} – {k.rabattsatz():.0%} Rabatt")
    pass
