from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Cargamos el modelo previamente entrenado
model = load_model('modelo_neumonia.keras')

# Iniciamos  Flask
app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar la imagen subida
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        # Procesamos la imagen
        img_path = 'static/uploaded_image.jpg'  
        file.save(img_path)  
        
        # Preprocesar la imagen
        img = image.load_img(img_path, target_size=(224, 224))  # Ajustamos al tamaño del modelo
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # ¿ predicción
        prediccion = model.predict(img_array)
        probabilidad_neumonia = prediccion[0][0]  # Probabilidad de neumonía (0 - 1)
        
        # resultado
        if probabilidad_neumonia > 0.9:
            resultado = f"Paciente con neumonía detectada (Precisión: {probabilidad_neumonia*100:.2f}%)"
        else:
            resultado = f"Paciente normal (Precisión: {(1 - probabilidad_neumonia)*100:.2f}%)"
        
        # Renderizar la plantilla con los resultados
        return render_template('index.html', img_path=img_path, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
