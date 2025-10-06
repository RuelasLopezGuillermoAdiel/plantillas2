from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    arr = ["Guillermo", "miguel", "luis", "diego"]
    autor ="Guillermo Adiel Ruelas Lopez"
    return render_template("index.html", nombre = autor, amigos = arr)

@app.route("/edades")
def años():
    edades=["17", "17", "17", "17"]
    autor = ["los papas"]
    return render_template("index.html", edad = edades, creador = autor)  
    
@app.route("/gatitos")
def cats():
    razas=["persa", "siames", "carey", "azul ruso"]
    autor = ["sus especies"]
    return render_template("index.html", gatos = razas, especie = autor)  

@app.route("/perritos")
def dog():
    perros=["bulldog", "pitbull", "chihuahua", "salchicha"]
    autor = ["los papas"]
    return render_template("index.html", caninos = perros, raza = autor)  

if __name__ == "__main__":
    app.run(debug=True)