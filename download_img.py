import requests

# Set the range of image IDs you want to download
for i in range(11820, 999999, 1):
    url = f"https://v2static.nogifes.jp/resource/Background/Photo/photo_common_{i}.png"
    file_name = f"photo_common_{i}.png"

    try:
        # Send a request to download the image
        headers = {
            "Host": "v1static.nogifes.jp",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "User-Agent": "nogifes/2.12.0.0 CFNetwork/1494.0.7 Darwin/23.4.0",
            "Accept-Language": "ja",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Unity-Version": "2022.3.34f1",
        }
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Save the image to a local file
            with open("png/" + file_name, "wb") as file:
                file.write(response.content)
            print(f"Downloaded {file_name}")
        else:
            print(f"Image not found for ID {i}, skipping.")

    except requests.RequestException as e:
        print(f"An error occurred while downloading ID {i}: {e}")
