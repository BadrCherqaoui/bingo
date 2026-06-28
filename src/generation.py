import pandas as pd
import random
import json
import string
import csv

df = pd.read_csv("../data/anecdote.csv", sep=",")

anecdotes = df["Anecdote"].dropna().tolist()

# IMPORTANT : liste UNIQUE des personnes
noms = df["Nom"].dropna().unique().tolist()

def gen_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

grids = {}
users = []

# ===== 1. 1 code par personne =====
for name in noms:

    code = gen_code()
    while code in grids:
        code = gen_code()

    grids[code] = {
        "name": name,
        "grid": random.sample(anecdotes, 16)
    }

    users.append({
        "name": name,
        "code": code
    })

# ===== 2. (optionnel) grilles anonymes =====
for i in range(40 - len(noms)):

    code = gen_code()
    while code in grids:
        code = gen_code()

    name = f"Participant_{i+1}"

    grids[code] = {
        "name": name,
        "grid": random.sample(anecdotes, 16)
    }

    users.append({
        "name": name,
        "code": code
    })

# ===== SAVE JSON =====
with open("../data/grid.json", "w", encoding="utf-8") as f:
    json.dump(grids, f, ensure_ascii=False, indent=2)

# ===== SAVE CSV =====
with open("../data/users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "code"])
    writer.writeheader()
    writer.writerows(users)

print("OK :", len(users))