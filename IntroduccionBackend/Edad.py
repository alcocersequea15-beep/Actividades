from flask import Flask
app=Flask(__name__)
## Tomamos la tercera ruta y la reemplazamos por el siguirnte ejemplo
## 2.) un programa que al capturar la edad de una persona diga si es:
## Menor de Edad (Menor a 18 años)
## Adulto (Mayor o igual a 18 años y menor a 60 años)
## Adulto mayor (Mayor o igual a 60 años)
@app.route("/edad")
@app.route("/edad/<int:edad>")
def edades(edad=0):
    if edad<18:
        R="Menor de edad"
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto Mayor"
    return f"<h1>La persona es: {R} </h1> <hr>"

if __name__=='__main__':
    ## El valor True significa que la qpp se deja en modo debug
    app.run(debug=True)