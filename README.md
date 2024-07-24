# API_Gcloud_Streamlit
Generaremos un modelo RM y lo pondremos en producción usando Streamlit. El modelo RM permitirá recomendar si el ingreso de una persona es alto o bajo

## 1. Entrenamiento del modelo
Crea un cuaderno de Jupyter o Colab llamado RN.ipynb y entrena tu modelo de Red Neuronal. Guarda el modelo entrenado en un archivo, por ejemplo, modeloRN.pkl

## 2. Producción en servidor local - preparación del entorno
a. Crear y activar el entorno.

    $   conda create -n ApiCrop
    $   conda activate ApiCrop
    $   conda install python=3.8
    $   pip install -r requirements.txt
    $   pip install --upgrade numpy
    $   streamlit run app.py
    
## NOTA
1. Si no se puede ejecutar el comando streamlit run app.py, se debe instalar el paquete streamlit con el comando pip install streamlit
2. No te olvides ubicarte en tu carpeta donde tienes tu archvio app.py
3. Debes tener instalando miniconda, todo el proceso 2 se realiza en el termial del mismo.

