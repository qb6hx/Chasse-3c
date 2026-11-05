import argparse
import itertools
import string
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=int, default=400)
    args = parser.parse_args()

    caracteres = string.ascii_lowercase + string.digits
    resultats = []

    for longueur in (3,):
        for combinaison in itertools.islice(
            itertools.product(caracteres, repeat=longueur),
            args.batch
        ):
            resultats.append("".join(combinaison))

    with open("trouves.txt", "a", encoding="utf-8") as fichier:
        fichier.write("\n".join(resultats) + "\n")

    print(f"{len(resultats)} combinaisons générées.")

if __name__ == "__main__":
    main()
