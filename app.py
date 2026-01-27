from flask import Flask
app=Flask (__name__)

## Definicion de la ruta principal
@app.route("/ruta1")
def HolaFlask():
    return "<h1>¡Hola Flask¡<h1> <hr>"

## Definicion una segunda ruta
@app.route("/ruta2")
def ruta2():
    return "<strong> Estamos en la segunda ruta </strong> <hr>"

## Definimos una tercera ruta
@app.route("/ruta3")
def ruta3():
    return "<em> Estamos en la tercera ruta </em> <hr>"

if __name__=='__main__':
    ## El valor True indica que la app se deja en modo debug
    app.run(debug=True)