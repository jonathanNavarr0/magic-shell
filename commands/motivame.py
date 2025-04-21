import random
import os

def run():
    frases_path = os.path.join("data", "frases.txt")

    try:
        with open(frases_path, "r", encoding="utf-8") as f:
            frases = f.readlines()
        print("\n✨ " + random.choice(frases).strip() + "\n")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo de frases.")
