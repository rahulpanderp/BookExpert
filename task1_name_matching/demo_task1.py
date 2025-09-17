from names_list import NAMES
from name_matcher import find_similar_names

def main():
    q = input("Enter name to match: ").strip()
    best, matches = find_similar_names(q, NAMES, limit=8)
    if best[0]:
        print(f"\nBest match: {best[0]}  (score: {best[1]:.1f})\n")
        print("Top matches:")
        for name, score, _ in matches:
            print(f"{name:25s}  {score:.1f}")
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()