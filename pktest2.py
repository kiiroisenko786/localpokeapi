import json
import requests

typeSprites = {
    "normal" : "https://archives.bulbagarden.net/media/upload/0/08/NormalIC_SV.png",
    "fighting" : "https://archives.bulbagarden.net/media/upload/0/0f/FightingIC_SV.png",
    "flying" : "https://archives.bulbagarden.net/media/upload/d/d7/FlyingIC_SV.png",
    "poison" : "https://archives.bulbagarden.net/media/upload/9/9d/PoisonIC_SV.png",
    "ground" : "https://archives.bulbagarden.net/media/upload/f/f8/GroundIC_SV.png",
    "rock" : "https://archives.bulbagarden.net/media/upload/3/32/RockIC_SV.png",
    "bug" : "https://archives.bulbagarden.net/media/upload/d/d1/BugIC_SV.png",
    "ghost" : "https://archives.bulbagarden.net/media/upload/2/2c/GhostIC_SV.png",
    "steel" : "https://archives.bulbagarden.net/media/upload/b/b8/SteelIC_SV.png",
    "fire" : "https://archives.bulbagarden.net/media/upload/a/a2/FireIC_SV.png",
    "water" : "https://archives.bulbagarden.net/media/upload/d/de/WaterIC_SV.png",
    "grass" : "https://archives.bulbagarden.net/media/upload/7/7b/GrassIC_SV.png",
    "electric" : "https://archives.bulbagarden.net/media/upload/7/77/ElectricIC_SV.png",
    "psychic" : "https://archives.bulbagarden.net/media/upload/9/96/PsychicIC_SV.png",
    "ice" : "https://archives.bulbagarden.net/media/upload/1/13/IceIC_SV.png",
    "dragon" : "https://archives.bulbagarden.net/media/upload/7,/7f/DragonIC_SV.png",
    "dark" : "https://archives.bulbagarden.net/media/upload/3/30/DarkIC_SV.png",
    "fairy" : "https://archives.bulbagarden.net/media/upload/c/c6/FairyIC_SV.png"
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
