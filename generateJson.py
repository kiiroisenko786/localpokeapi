import json
import requests

typeSprites = {
    "normal" : "NormalIC_SV.png",
    "fighting" : "FightingIC_SV.png",
    "flying" : "FlyingIC_SV.png",
    "poison" : "PoisonIC_SV.png",
    "ground" : "GroundIC_SV.png",
    "rock" : "RockIC_SV.png",
    "bug" : "BugIC_SV.png",
    "ghost" : "GhostIC_SV.png",
    "steel" : "SteelIC_SV.png",
    "fire" : "FireIC_SV.png",
    "water" : "WaterIC_SV.png",
    "grass" : "GrassIC_SV.png",
    "electric" : "ElectricIC_SV.png",
    "psychic" : "PsychicIC_SV.png",
    "ice" : "IceIC_SV.png",
    "dragon" : "DragonIC_SV.png",
    "dark" : "DarkIC_SV.png",
    "fairy" : "FairyIC_SV.png"
}

pkDict = {
    "pokemon" : [

    ]
}

for num in range(1,152):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{num}/")
    resp = response.json()
    pkID = resp["id"]
    name = resp["name"]
    nameSplit = list(name)
    nameSplit[0] = nameSplit[0].upper()
    pkName = "".join(nameSplit)
    pkType1 = typeSprites[resp["types"][0]["type"]["name"]]
    pkType2 = ""
    try:
        pkType2 = typeSprites[resp["types"][1]["type"]["name"]]
    except Exception as e:
        pass
    pkSprite = resp["sprites"]["other"]["official-artwork"]["front_default"]
    pkDict["pokemon"].append({
        "id" : pkID,
        "name" : pkName,
        "type1" : pkType1,
        "type2" : pkType2,
        "sprite" : pkSprite
    })

with open('db.json', 'w', encoding='utf-8') as f:
    json.dump(pkDict, f, ensure_ascii=False, indent=4)
