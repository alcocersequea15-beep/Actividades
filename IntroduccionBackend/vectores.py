from flask import Flask
app = Flask(__name__)

## 3.) programa qur crea arreglos con valores aleatorios
## inportamos la libreria numpy si no existe la intalamos con: pip install numpy
import numpy as np
@app.route ("/arreglos")
@app.route ("/arreglos/<int:valores>/<int:columnas>")
@app.route ("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglos=np.random.randint(valores, size=columnas)
    else:
        arreglos=np.random.randint(valores, size=(filas,columnas))
    return f"<h1>El arreglo aleatorio es: {arreglos} </h1><hr>"
if __name__=='__main__':
    ##El valor True indica que la app se deja en modo debug
    app.run(debug=True)