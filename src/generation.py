import pandas as pd
import random
import json
import string
import csv

df = pd.read_csv("../data/anecdote.csv", sep=",")

anecdotes = df["Anecdote"].dropna().tolist()
noms = df["Nom"].dropna().tolist()

def gen_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

N_GRIDS = 40

grids = {}
users = []

for _ in range(N_GRIDS):

    code = gen_code()
    while code in grids:
        code = gen_code()

    name = random.choice(noms)

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

print("OK généré :", len(users))