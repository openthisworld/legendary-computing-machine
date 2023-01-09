import requests
import json
import base64



openai_api_key = "${{ secrets.API_KEY }}"
#openai_api_key = "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"

def generate_image(prompt):
    model_engine = "image-alpha-001"
    prompt = (f"{prompt}")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = """
    {
        """
    data += f'"model": "{model_engine}",'
    data += f'"prompt": "{prompt}",'
    data += """
        "num_images":1,
        "size":"256x256",
        "response_format":"url"
    }
    """

    api_url = "https://api.openai.com/v1/images/generations"

    response = requests.post(api_url, headers=headers, data=data)

    if response.status_code == 200:
        response_text = json.loads(response.text)
        return response_text['data'][0]['url']
    else:
        return None

def save_image(url, file_name):
    response = requests.get(url)
    image_data = response.content

    with open(file_name, "wb") as f:
        f.write(image_data)

prompt = input("Enter a prompt: ")
image_url = generate_image(prompt)

if image_url is not None:
    save_image(image_url, "image.jpg")
    print("Image saved successfully!")
else:
    print("Error generating image")
