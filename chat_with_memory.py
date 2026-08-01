import requests

history = []

def ask(user_text):
    history.append({"role": "user", "content": user_text})

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2:latest",
            "messages": history,
            "stream": False
        },
        proxies={"http": None, "https": None}
    )

    data = response.json()
    reply = data["message"]["content"]
    history.append({"role": "assistant", "content": reply})
    return reply

while True:
    user_input = input("You: ")
    if user_input == "bye":
        print("Goodbye!")
        break
    else:
        discusion = ask(user_input)
        print(discusion)



#Коробка 1 (функция ask):
#  вход: один текст от пользователя
 # выход: ответ модели
  #(плюс побочный эффект: обновляет history)

#Коробка 2 (while True снаружи):
#  спрашивает пользователя
#  проверяет "хочет ли выйти"
 # если нет — передаёт вопрос в Коробку 1, печатает результат
 # если да — break