

from rapidfuzz import process, fuzz

def find_similar_names(input_name, names_list, limit=10):
    matches = process.extract(input_name, names_list, scorer=fuzz.WRatio, limit=limit)
    best = matches[0] if matches else (None, 0, None)
    return best, matches