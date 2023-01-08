import requests
import json

# Замените YOUR_API_KEY на свой реальный API ключ
api_key = "YOUR_API_KEY"

# Задайте запрос для DALL·E
prompt = "Generate a picture of a cat wearing a hat"

# Отправьте запрос к DALL·E
response = requests.post(
    "https://api.openai.com/v1/images/generations",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    json={
        "prompt": prompt
    }
)

# Парсим ответ от DALL·E
response_json = response.json()

# Получаем URL изображения
image_url = response_json["data"][0]["url"]

# Скачиваем изображение по URL
response = requests.get(image_url)

# Сохраняем изображение в текущую директорию
open("image.jpg", "wb").write(response.content)

print("Изображение сохранено в текущей директории")