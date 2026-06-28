import pandas as pd
import random
import json
import string
import csv

# ===== DATA =====
df = pd.read_csv("../data/anecdote.csv", sep=",")

anecdotes = df["Anecdote"].dropna().tolist()
noms = df["Nom"].dropna().tolist()

# ===== CONFIG =====
N_GRIDS_TOTAL = 40
N_ANON = N_GRIDS_TOTAL - len(noms)  # nombre de grilles sans nom

def gen_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

grids = {}
users = []
anon_users = []

# ===== 1. Grilles avec noms =====
for _ in range(N_GRIDS_TOTAL - N_ANON):

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

# ===== 2. Grilles anonymes =====
for i in range(N_ANON):

    code = gen_code()
    while code in grids:
        code = gen_code()

    name = f"Participant_{i+1}"

    grids[code] = {
        "name": name,
        "grid": random.sample(anecdotes, 16)
    }

    anon_users.append({
        "name": name,
        "code": code
    })

# ===== SAVE GRID JSON =====
with open("../data/grid.json", "w", encoding="utf-8") as f:
    json.dump(grids, f, ensure_ascii=False, indent=2)

# ===== SAVE USERS =====
with open("../data/users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "code"])
    writer.writeheader()
    writer.writerows(users)

# ===== SAVE ANON USERS =====
with open("../data/authors_codes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "code"])
    writer.writeheader()
    writer.writerows(anon_users)

print("OK total:", len(grids))