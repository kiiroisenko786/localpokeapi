from PIL import Image       
import requests

img = Image.open(requests.get("https://archives.bulbagarden.net/media/upload/0/08/NormalIC_SV.png", stream=True).raw)

img.show()