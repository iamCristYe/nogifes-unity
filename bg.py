# https://v2static.nogifes.jp/resource/Background/Photo/photo_common_11587.png
import requests
import os

for i in range(11300, 11630):
    filename = f"{i}.png"
    filepath = "png/" + filename
    print(filepath)
    if os.path.exists(filepath):
        continue

    url = (
        f"https://v2static.nogifes.jp/resource/Background/Photo/photo_common_{filename}"
    )

    with open(filepath, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
