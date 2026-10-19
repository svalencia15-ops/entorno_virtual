import requests
from flask import Flask

# Crear la aplicación web
app = Flask(__name__)


# Definir la ruta principal (página de inicio)
@app.route("/")
def inicio():
  # Usamos la librería 'requests' para obtener un dato curioso/frase aleatoria desde una API web
  respuesta = requests.get("https://catfact.ninja/fact")
  dato_gato = respuesta.json().get("fact", "No se pudo obtener el dato")

  # Retornamos el contenido HTML que se verá en el navegador
  return f"""
    <h1>¡Mi primera página Web con Python en GitHub Codespaces! 🚀</h1>
    <p><strong>Dato curioso del día (obtenido con la librería requests):</strong></p>
    <blockquote style="background: #f0f0f0; padding: 10px; border-left: 5px solid #007acc;">
        {dato_gato}
    </blockquote>
    """


# Ejecutar el servidor web
if __name__ == "__main__":
  app.run(debug=True, port=5000)