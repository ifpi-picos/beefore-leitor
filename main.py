import keyboard, requests
from decouple import config

cardIdArray = []
def setCardId(event):
    try:
        if int(event.name) or event.name == "0":
            cardIdArray.append(event.name)
            
    except ValueError:
        if event.name == "enter":
            cardId = ""
            for n in range(len(cardIdArray)):
                cardId += cardIdArray[n]

            cardIdArray.clear()

            try:
                requests.post(config("API_URL") + "/relatory", json={"cardid": cardId}, headers={"Authorization": config("API_TOKEN")})
                print("Cartão {} enviado com sucesso".format(cardId))
            except:
                print("Erro ao enviar cartão")
                pass
        else:
            pass

keyboard.on_press(setCardId)
keyboard.wait()