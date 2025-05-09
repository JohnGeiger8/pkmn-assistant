from flask import Flask, request, jsonify
from services.vision import identify_pokemon
from services.matchups import compute_team_weaknesses

app = Flask(__name__)

@app.route('/api/teams/analyze', methods=['POST'])
def analyze_team():
    img = request.files['image'].read()
    pokemon_list = identify_pokemon(img)        # e.g. ["Pikachu", "Charizard", ...]
    analysis = compute_team_weaknesses(pokemon_list)
    return jsonify({ "team": pokemon_list, **analysis })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
