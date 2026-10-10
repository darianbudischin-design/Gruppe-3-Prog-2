class Konto:
    def __init__(self, inhaber: str, dispo: float = 0.0) -> None:
        self.inhaber = inhaber
        self.dispo = dispo            # nutzt bereits den Setter unten!
        self._saldo = 0.0

    @property
    def saldo(self) -> float:         # nur lesend: es gibt keinen Setter
        return self._saldo

    @property
    def dispo(self) -> float:
        return self._dispo

    @dispo.setter
    def dispo(self, wert: float) -> None:
        if wert < 0:
            raise ValueError("Dispo darf nicht negativ sein")
        self._dispo = wert

    @property
    def verfuegbar(self) -> float:    # berechnete Eigenschaft
        return self._saldo + self._dispo

    def einzahlen(self, betrag: float) -> None:
        if betrag <= 0:
            raise ValueError("Betrag muss positiv sein")
        self._saldo += betrag

    def abheben(self, betrag: float) -> None:
        if betrag > self.verfuegbar:
            raise ValueError("Nicht genug Deckung")
        self._saldo -= betrag


konto = Konto("Anna", dispo=200)
konto.einzahlen(100)
konto.abheben(250)
print(konto.saldo, konto.verfuegbar)

try:
    konto.saldo = 1_000_000
except AttributeError as e:
    print("AttributeError:", e)

try:
    konto.dispo = -50
except ValueError as e:
    print("ValueError:", e)
