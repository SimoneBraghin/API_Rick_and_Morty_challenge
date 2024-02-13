from flask import Flask, render_template
import urllib.request, json

app = Flask (__name__)

@app.route("/") # rota de  URL raiz
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character";
    response = urllib.request.urlopen(url) # envia a req e recebe a res
    data = response.read(); # leitura dos dados vindos da api
    dict = json.loads(data); # transforma esses dados em json p/ python
    
    return render_template("characters.html", characters = dict["results"])

@app.route("/profile/<id>") # obter um personagem

def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/"+id;
    response = urllib.request.urlopen(url) 
    data = response.read(); 
    dict = json.loads(data);
    
    return render_template("profile.html", profile = dict)

@app.route("/lista")

def get_list_characters():
    url = "https://rickandmortyapi.com/api/character";
    response = urllib.request.urlopen(url)
    characters = response.read();
    dict = json.loads(characters);
    
    characters = []
    
    for character in dict["results"]:
        character = {
            "name":character["name"],
            "status":character["status"]
        }
        
        characters.append(character);
    return {"characters":characters}

@app.route("/locations") # rota de locations
def get_list_locations_page():
        url = "https://rickandmortyapi.com/api/location";
        response = urllib.request.urlopen(url) # envia a req e recebe a res
        data = response.read(); # leitura dos dados vindos da api
        locations_data = json.loads(data); # transforma esses dados em json p/ python
    
        locations = [];
    
        #para cada localizacao cria um objeto com id, nome, tipo e dimensao
        for location in locations_data["results"]:
            location = {
                "id":location["id"],
                "name":location["name"],
                "type":location["type"],
                "dimension":location["dimension"]
            }
            # adiciona esse elemento a lista de localizações
            locations.append(location);
        #envia os dados para o template locations.html
        return render_template("locations.html", locations = locations_data["results"]);


@app.route("/location/<id>") # obter uma location
def get_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url) 
    data = response.read(); 
    location_dict = json.loads(data);
    
    return render_template("location.html", location=location_dict);