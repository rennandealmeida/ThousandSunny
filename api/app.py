from flask import Flask, render_template

app = Flask("ThousandSunny",static_folder="api/images",template_folder="api/templates")

@app.route("/", methods=["GET"])
def Home():
    return render_template('thousandsunny.html')

@app.route("/luffy")
def FraseLuffy():
    return render_template('luffy.html')

@app.route("/zoro", methods=["GET"])
def FraseZoro():
    return render_template('zoro.html')

@app.route("/sanji", methods=["GET"])
def FraseSanji():
    return render_template('sanji.html')

@app.route("/usopp", methods=["GET"])
def FraseUsopp():
    return render_template('usopp.html')

@app.route("/nami", methods=["GET"])
def FraseNami():
    return render_template('nami.html')

app.run(debug=True, host='0.0.0.0')