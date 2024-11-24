
# Taller 2 - MLOps (UNIVERSIDAD EIA)

Este repositorio contiene el desarrollo del Taller 2 del curso de MLOps de la Universidad EIA, 2024. En este proyecto se aplica la metodología **CRISP-DM** utilizando el dataset seleccionado: **[Data Science Salaries 2023](https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023)**. El objetivo principal es explorar, modelar y desplegar un modelo de Machine Learning que cumpla con las especificaciones del taller.

---

## Contenido

1. **Entendimiento de Negocio**
   - **Objetivo de Negocio:** 
     Evaluar factores que afectan los salarios en roles relacionados con ciencia de datos y proporcionar insights que puedan guiar decisiones estratégicas para empleadores y empleados.
   - **Objetivo Analítico:** 
     Predecir el salario esperado en función de características como experiencia, región, rol y habilidades técnicas.

2. **Entendimiento de los Datos**
   - Exploración inicial del dataset.
   - Análisis univariado, bivariado y generación de visualizaciones para identificar patrones y relaciones.

3. **Preparación de Datos**
   - Transformaciones realizadas para variables de entrada y salida.
   - Proceso detallado de limpieza y tratamiento de datos faltantes o atípicos.

4. **Modelación**
   - Implementación de al menos 5 modelos de Machine Learning, incluyendo un método de ensamble.
   - Búsqueda de hiperparámetros para optimizar cada modelo.
   - Se incluye el uso recomendado de la librería PyCaret para la comparación de modelos.

5. **Evaluación**
   - Selección de la métrica de evaluación más relevante (ej. RMSE, MAE, R²) y justificación.
   - Identificación del mejor modelo y análisis de su aplicabilidad práctica.

6. **Despliegue**
   - Creación de un pipeline para el mejor modelo utilizando **FastAPI**.
   - Despliegue del endpoint en una instancia de **AWS EC2** con una URL pública para realizar predicciones.

---

## Requisitos

- **Python 3.9+**
- Librerías principales: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `PyCaret`, `FastAPI`, `uvicorn`, `boto3`.
- Configuración de una cuenta de **AWS** para la instancia EC2.

---

## Ejecución del Proyecto

1. **Exploración y Análisis de Datos**
   - Código: `notebooks/exploration_and_analysis.ipynb`
   - Descripción: Análisis exploratorio y gráficos.

2. **Modelación**
   - Código: `models/model_training.py`
   - Descripción: Entrenamiento de modelos y búsqueda de hiperparámetros.

3. **API**
   - Código: `api/app.py`
   - Descripción: FastAPI para predicción del modelo.

4. **Despliegue**
   - Detalles: Guía paso a paso en `deployment/deployment_guide.md`.

---

## Uso del Endpoint

El endpoint desplegado está disponible en la URL pública generada por la instancia EC2. Ejemplo de petición:

**Método:** `POST`  
**Endpoint:** `http://<ec2-public-url>/predict`  
**Body (JSON):**
```json
{
    "experience_level": "SE",
    "job_title": "Data Scientist",
    "region": "US",
    "skills": ["Python", "SQL", "Machine Learning"],
    "remote_ratio": 100
}
```

**Respuesta (JSON):**
```json
{
    "predicted_salary": 125000
}
```

---

## Autor

- Nombre: [Tu Nombre]
- Universidad: Universidad EIA
- Año: 2024
