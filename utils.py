import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        candidates = {}
        for i in data:
            candidates[i['id']] = i
        return candidates
