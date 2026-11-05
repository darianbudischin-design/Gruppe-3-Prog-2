# Programmieren 2 – Fokus-Tag 1 (Sa 10.10.2026, 14:15–19:00 Uhr)

Übungs-Repository für den Fokus-Tag. **KI-Ampel: ROT** – wir coden heute zu zweit und ohne KI.
Alle Infos zum Semester (Termine, Fristen, Online-Termine): **OLAT**.

| Datei | Aufgabe (Beschreibung steht oben in der Datei) | Zeit | Prüfen mit |
|---|---|---|---|
| `block_a.py` | A1/A2: Mitarbeiter | 20 Min. | `pytest -k block_a` (5 Tests) |
| `block_b.py` | B1: Rechnung | 20 Min. | `pytest -k block_b` (6 Tests) |
| `block_c.py` | C1: Lagerartikel | 15 Min. | `pytest -k block_c` (6 Tests) |
| `block_d.py` | D1: Verein (nutzt `kunden.py`) | 10 Min. | `pytest -k block_d` (4 Tests) |
| `ki_fehlerjagd.py` | KI-Fehlerjagd: drei Fehler finden | 8 Min. | Testaufruf im Dateikopf |
| `beispiele/` | Code aus den Folien zum Ausprobieren und als Vorlage | – | – |

## Setup-Check

1. `python --version` → 3.12 oder höher (macOS: `python3`, Windows ggf. `py`)
2. `pytest` → startet; zu Beginn sind alle 21 Tests rot – das ist richtig so.

## Neuen Code holen

Nach jedem Fokus-Tag kommt neuer Code dazu. Vorher eigene Änderungen sichern:

```bash
git add .
git commit -m "Meine Lösungen"
git pull
```
