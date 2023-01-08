from openai import ChatGPT


model = ChatGPT()


response = model.get_response("Ты здесь?")
print(response)