import requests

# Day 13: Web Scraping and APIs
# Concept 05: REST API Integration (Fetching JSON data)

def fetch_pokemon_data(pokemon_name):
    # Public API: PokeAPI (No authentication required)
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    print(f"--- Fetching Data for: {pokemon_name} ---")
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extracting specific fields from the complex JSON response
            name = data['name'].capitalize()
            id = data['id']
            height = data['height']
            weight = data['weight']
            types = [t['type']['name'] for t in data['types']]
            
            print(f"Pokemon: {name} (ID: {id})")
            print(f"Height: {height} | Weight: {weight}")
            print(f"Types: {', '.join(types)}")
            
            # Listing some abilities
            abilities = [a['ability']['name'] for a in data['abilities']]
            print(f"Abilities: {', '.join(abilities)}")
            
        elif response.status_code == 404:
            print(f"Error: Pokemon '{pokemon_name}' not found.")
        else:
            print(f"Request failed with status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    # Test with a few Pokemon
    fetch_pokemon_data("Pikachu")
    print("\n")
    fetch_pokemon_data("Charizard")
