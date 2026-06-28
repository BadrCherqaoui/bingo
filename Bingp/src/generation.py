import pandas as pd
import random
import json
import string

# ===== 1. Charger données =====
df = pd.read_csv("../data/anecdote.csv", sep=",")  # adapte si besoin
anecdotes = df["Anecdote"].dropna().tolist()

# ===== 2. Générer codes utilisateurs =====
def generate_code(n=5):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

# ===== 3. Créer joueurs fictifs (30-35 grilles) =====
n_grids = 35
codes = [generate_code() for _ in range(n_grids)]

# ===== 4. Génération des grilles =====
grids = {}

for code in codes:
    grid = random.sample(anecdotes, 16)  # 4x4
    grids[code] = grid

# ===== 5. Sauvegarde =====
with open("../data/grid.json", "w", encoding="utf-8") as f:
    json.dump(grids, f, ensure_ascii=False, indent=2)

print("Grilles générées :", len(grids))