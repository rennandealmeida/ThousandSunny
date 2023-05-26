from flask import Flask

app = Flask("ThousandSunny")

@app.route("/luffy", methods=["GET"])
def FraseLuffy():

    response = print("Serei o Rei dos Piratas")
    return response

@app.route("/zoro", methods=["GET"])
def FraseZoro():

    response = print("⁠Eu serei o maior espadachim do mundo! Tudo o que me resta é meu destino! Meu nome pode ser infame, mas vai abalar o mundo!")
    return response


@app.route("/sanji", methods=["GET"])
def FraseSanji():

    response = print("Não comece uma luta se você não pode terminá-la")
    return response

@app.route("/usopp", methods=["GET"])
def FraseUsopp():

    response = print("⁠Chega um momento em que um homem deve se manter de pé e lutar. Esse momento é quando alguém ri dos sonhos de seus amigos")
    return response

@app.route("/nami", methods=["GET"])
def FraseNami():

    response = print("Todo mundo é fraco quando hesita.")
    return response

app.run(debug=True, host='0.0.0.0')