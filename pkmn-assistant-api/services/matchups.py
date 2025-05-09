import json
with open('models/type_chart.json') as f:
    TYPE_CHART = json.load(f)

def compute_team_weaknesses(pokemon_names):
    types = [TYPE_CHART['pokemon'][name] for name in pokemon_names]
    # Flatten and count resistances/weaknesses
    counter = {'weak': {}, 'resist': {}, 'immune': {}}
    for t in types:
      for attack, multiplier in t.items():
        if multiplier > 1:
           counter['weak'][attack] = counter['weak'].get(attack, 0) + 1
        elif 0 < multiplier < 1:
           counter['resist'][attack] = counter['resist'].get(attack, 0) + 1
        elif multiplier == 0:
           counter['immune'][attack] = counter['immune'].get(attack, 0) + 1
    return counter
