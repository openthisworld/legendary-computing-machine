import openai

openai.api_key = "${{ secrets.API_KEY }}" 


def get_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=1,
    )

    message = completions.choices[0].text
    return message.strip()

while True:
    prompt = input("You: ")
    response = get_response(prompt)
    print("Bot:", response)