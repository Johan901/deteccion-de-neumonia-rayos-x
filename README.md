# Diagnóstico de Neumonía con Flask y Red Neuronal Convolucional (CNN)
# Proyecto de Diagnóstico de Neumonía con Flask y CNN

Este proyecto consiste en una aplicación web que utiliza un modelo de red neuronal convolucional (CNN) para detectar neumonía a partir de imágenes de rayos X de tórax. La aplicación está construida con **Flask** y se integra con un modelo previamente entrenado utilizando **TensorFlow**. 

## Tecnologías Utilizadas

- **Flask**: Framework web ligero en Python.
- **TensorFlow / Keras**: Biblioteca para construir y entrenar redes neuronales profundas.
- **HTML5, CSS3**: Para la estructura y el diseño de la interfaz web.
- **NumPy**: Para la manipulación de matrices y arrays en las predicciones.
- **Jinja2**: Motor de plantillas para renderizar resultados en el frontend.
- **Python**: Lenguaje de programación principal.

## Funcionalidades

1. **Cargar imagen**: El usuario puede cargar una imagen de rayos X de tórax en formato JPG o PNG.
2. **Predicción**: El modelo realiza una predicción sobre la imagen cargada, determinando si el paciente tiene neumonía o si es normal.
3. **Mostrar resultados**: Después de realizar la predicción, se muestra un mensaje indicando si el paciente tiene neumonía o está sano, junto con la imagen cargada.
4. **Interfaz visual**: La interfaz de usuario tiene un diseño simple con un formulario de carga y una sección de resultados.

## Estructura del Proyecto

/diagnostico-neumonia
    ├── /static
    │   ├── /css
    │   │   └── styles.css
    ├── /templates
    │   └── index.html
    ├── app.py
    ├── modelo_neumonia.keras
    ├── requirements.txt
    └── README.md

# Funcionamiento del Modelo
El modelo de neumonía está basado en una red neuronal convolucional (CNN) entrenada en un conjunto de datos de imágenes de rayos X de tórax. El modelo utiliza capas de convolución para detectar patrones en las imágenes y determinar si el paciente tiene neumonía o está sano.

# Preprocesamiento de Imágenes
El modelo requiere imágenes de entrada con un tamaño de 224x224 píxeles. Por lo tanto, antes de pasar la imagen cargada al modelo, se realiza el siguiente preprocesamiento:

La imagen se redimensiona a 224x224 píxeles.
Se convierte a un array y se normaliza (valores entre 0 y 1).
Se ajusta la forma de la imagen para que sea compatible con la entrada del modelo.
Predicción
El modelo devuelve un valor de probabilidad entre 0 y 1. Si la probabilidad es mayor que 0.9, se considera que el paciente tiene neumonía. Si es menor, el paciente es considerado sano.
