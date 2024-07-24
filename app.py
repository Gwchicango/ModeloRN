import streamlit as st
import numpy as np
import pickle
import os

#---------------------------------------------------------------------------------------------------------------------------------
# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):
    try:
        # Convertir todas las entradas a números
        x_in = [float(i) if isinstance(i, (int, float)) else 0 for i in x_in]
        x = np.asarray(x_in).reshape(1, -1)
        preds = model.predict(x)
        return preds
    except Exception as e:
        return f"Error en la predicción: {e}"
#---------------------------------------------------------------------------------------------------------------------------------

def main():
    # Inyectar CSS personalizado
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .title-font {
        font-size:30px !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="title-font">Regresión Lineal</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">SISTEMA DE PREDICCION DE INGRESOS - BAJO - ALTO</p>', unsafe_allow_html=True)

    # Cargar el modelo (si es necesario)
    MODEL_PATH = 'models/modeloRN.pkl'
    model = None
    if not os.path.exists(MODEL_PATH):
        st.error(f"El archivo del modelo no se encuentra en la ruta: {MODEL_PATH}")
        return

    try:
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        st.info("Intenta actualizar numpy y scikit-learn a las versiones más recientes.")
        return

    # Formulario para ingresar los datos
    with st.form("prediction_form"):
        edad = st.number_input("Edad del individuo", min_value=0, format="%d")
        estado_laboral = st.selectbox("Tipo de Empleador", ["State-gov", "Self-emp-not-inc", "Private", "Federal-gov", "Local-gov", "Self-emp-inc", "Without-pay", "Never-worked", "?"])
        educacion = st.selectbox("Educación", [
            "HS-grad", "Some-college", "Bachelors", "Masters", "Assoc-voc", "11th", 
            "Assoc-acdm", "10th", "7th-8th", "Prof-school", "9th", "12th", 
            "Doctorate", "5th-6th", "1st-4th", "Preschool"
        ])
        anos_educacion = st.number_input("Años de educación completados", min_value=0, format="%d")
        estado_civil = st.selectbox("Estado civil", ["Married-civ-spouse", "Never-married", "Divorced", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"])
        ocupacion = st.selectbox("Ocupación", [
            "Prof-specialty", 
            "Craft-repair", 
            "Exec-managerial", 
            "Adm-clerical", 
            "Sales", 
            "Other-service", 
            "Machine-op-inspct", 
            "?", 
            "Transport-moving", 
            "Handlers-cleaners", 
            "Farming-fishing", 
            "Tech-support", 
            "Protective-serv", 
            "Priv-house-serv", 
            "Armed-Forces"
        ])
        relacion = st.selectbox("Relación", [
            "Husband", 
            "Not-in-family", 
            "Own-child", 
            "Unmarried", 
            "Wife", 
            "Other-relative"
        ])
        raza = st.selectbox("Raza", [
            "White", 
            "Black", 
            "Asian-Pac-Islander", 
            "Amer-Indian-Eskimo", 
            "Other"
        ])
        genero = st.selectbox("Género", ["Male", "Female"])
        ganancias = st.number_input("Ganancias adicionales", min_value=0, format="%d")
        perdidas = st.number_input("Pérdidas financieras", min_value=0, format="%d")
        horas_trabajadas = st.number_input("Horas trabajadas por semana", min_value=0, format="%d")
        pais_origen = st.selectbox("País de origen", [
            "United-States", 
            "Mexico", 
            "?", 
            "Philippines", 
            "Germany", 
            "Puerto-Rico", 
            "Canada", 
            "El-Salvador", 
            "India", 
            "Cuba", 
            "England", 
            "China", 
            "South", 
            "Jamaica", 
            "Italy", 
            "Dominican-Republic", 
            "Japan", 
            "Guatemala", 
            "Poland", 
            "Vietnam", 
            "Columbia", 
            "Haiti", 
            "Portugal", 
            "Taiwan", 
            "Iran", 
            "Greece", 
            "Nicaragua", 
            "Peru", 
            "Ecuador", 
            "France", 
            "Ireland", 
            "Hong", 
            "Thailand", 
            "Cambodia", 
            "Trinadad&Tobago", 
            "Laos", 
            "Yugoslavia", 
            "Outlying-US(Guam-USVI-etc)", 
            "Scotland", 
            "Honduras", 
            "Hungary", 
            "Holand-Netherlands"
        ])

        # Botón de predicción con estilo
        submit_button = st.form_submit_button("🏠 Predicción")

        if submit_button:
            # Preparar los datos de entrada para el modelo
            x_in = [edad, estado_laboral, educacion, anos_educacion, estado_civil, ocupacion, relacion, raza, genero, ganancias, perdidas, horas_trabajadas, pais_origen]
            predictS = model_prediction(x_in, model)
            
            # Interpretar la predicción
            if predictS[0] == 1:
                st.success('📈 EL INGRESO ES: ALTO')
            else:
                st.success('📈 EL INGRESO ES: BAJO')

if __name__ == "__main__":
    main()
