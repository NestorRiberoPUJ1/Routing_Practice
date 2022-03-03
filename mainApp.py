from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def root():
    return "¡Hola Mundo!"

@app.route('/<path:path>')
def catch_all(path):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez"

@app.route("/dojo")
def dojo():
    return "¡Dojo!"


@app.route("/say/<name>")
def say(name):
    return f"¡Hola {name}!"

@app.route("/repeat/<num>/<word>")
def repeat(num,word):

    result=""
    for x in range(int(num)):
        result +=f"<p>{x+1}. {word}</p>"
    return result





if(__name__=="__main__"):

    app.run(debug=True)

