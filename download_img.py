import requests
import os


def send_file_to_channel(bot_token, channel_username, file_path, caption=""):
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"

    try:
        # Open the file in binary mode
        with open(file_path, "rb") as file:
            # Prepare the request payload
            data = {"chat_id": channel_username, "caption": caption}
            files = {"document": file}

            # Send the POST request to Telegram API
            response = requests.post(url, data=data, files=files)

            # Check if the request was successful
            if response.status_code == 200:
                print("File sent successfully!")
            else:
                print(f"Failed to send file: {response.status_code}")
                print("Response:", response.json())

    except Exception as e:
        print("Error:", e)


# Set the range of image IDs you want to download
for i in range(7, 999999, 1):
    bot_token = os.environ["bot_token"]
    chat_id = "-1002165985535"
    url = f"https://v2static.nogifes.jp/resource/Background/Photo/photo_common_{i:05d}.png"
    file_name = f"photo_common_{i:05d}.png"

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

            send_file_to_channel(bot_token, chat_id, "png/" + file_name)
        else:
            print(f"Image not found for ID {i}, skipping.")

    except requests.RequestException as e:
        print(f"An error occurred while downloading ID {i}: {e}")
