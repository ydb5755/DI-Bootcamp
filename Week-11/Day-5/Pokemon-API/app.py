from flask import Flask, render_template
from requests import request, get

app = Flask(__name__)

# something = get('https://pokeapi.co/api/v2/pokemon').json()
# print(something)

@app.route('/pokemon/<id>')
def pokemon_by_id(id):
    something = get('https://pokeapi.co/api/v2/pokemon/{{id}}').json()['name']
    return render_template('pokemon_by_id.html', id=id, something=something)

@app.route('/pokemons/by_type/<type>')
def pokemon_by_type(type):
    return render_template('pokemon_by_type.html', type=type)

@app.route('/pokemons/by_name/<name>')
def pokemon_by_name(name):
    something = get('https://pokeapi.co/api/v2/pokemon/{{name}}').json()['name']
    return render_template('pokemon_by_name.html', name=name, something=something)

@app.route('/')
def main():
    return render_template('base.html')

@app.route('/pokemons/all')
def all_pokemon():
    all=get('https://pokeapi.co/api/v2/pokemon/').json()
    next=get(all['next']).json()
    if all['previous'] == None:
        previous = '#'
    else:
        previous=get(all['previous']).json()
    previous=get(all['next'])
    return render_template('all_pokemon.html', all=all, next=next, previous=previous)

if __name__ == '__main__':
    app.run(debug=True)

# all=get('https://pokeapi.co/api/v2/pokemon/').json()
# previous=all['next']
# next=get(next['next']).json()
# print(previous)