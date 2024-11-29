# Taller 2 - MLOps

- Santiago Fernandez
- Juan Camilo Ramirez
- Sofía Restrepo

Este repositorio contiene el desarrollo del Taller 2 de la materia MLOps con la metodología CRISP-DM utilizando el siguiente dataset: **[Data Science Salaries 2023](https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023)**

1. **Entendimiento de Negocio**

   - **Objetivo de Negocio:**
     Evaluar factores que afectan los salarios en roles relacionados con ciencia de datos y predecir el valor estimado del salario según las carácteristicas del empleado.
   - **Objetivo Analítico:**
     Predecir el salario esperado en función de características como experiencia, región del empleado y de la empresa y rol a través de diferentes modelos de Machine Learning.

2. **Entendimiento de los Datos**

   - Se realizó un análisis exploratorio de los datos en el archivo **EDA.ipynb** para entender los datos y determinar las transformaciones necesarias.

3. **Preparación de Datos**
   El dataset no incluía ningun dato nulo, por lo que no fue necesario realizar una imputación.

   El manejo de datos atípicos se hizo a través de la creación de un umbral con el percentil 90. Solo se mantuvieron los datos de salario cuyo valor sea inferior al valor al que pertenecen el 90% de los datos. Esto permite reducir los sesgos debido a valores atípicos.

   A través del análisis exploratorio, se optó por utilizar los datos de las 5 regiones de empresa con la mayor cantidad de registros, además de los trabajos que cuenten con un tipo de contratación a tiempo completo. Se filtró tambien el dataset para incluir unicamente los registros de los años 2022 y 2023, ya que la cantidad de datos era mayor y estos eran más actualizados respecto al año actual. Se eliminó las columnas 'work_year' y 'employment_type' ya que los datos fueron filtrados previamente.

   Adicionalmente, las columnas 'salary' y 'salary_currency' tambien fueron eliminadas, ya que solo se realizarán predicciones sobre el salario en dolares (USD).

   Se realizó una codificación One Hot para todas las columnas categoricas, y se utilizó un LabelEncoder para codificar la columna 'job_title' obteniendo un valor númerico para cada una de las posibles posiciones de trabajo.

   **Transformaciones frecuentemente utilizadas en la etapa de preparación de datos:**

   - **Escalar los datos:** Permite tener una escala homogenea para que el modelo no dé más peso a ciertas variables unicamente por la diferencia de escala. Uno de los métodos que se utiliza es el Standard Scaling. En nuestro caso, este no fue necesario ya que la única variable númerica además del salario era el año de trabajo, y esta fue eliminada después de la exploración de los datos.
   - **Codificación:** Se utiliza para convertir variables categóricas en variables númericas o binarias, esto permite que los modelos interpreten los datos; Tanto el One Hot Encoding como el Label Encoding fueron utilizados para nuestro proyecto.
   - **PCA:** Reduce la dimensionalidad de los datos según las caracteristicas con mayor importancia. Esto permite reducir la dimensión de los datos manteniendo el contexto.
   - **Manejo de datos nulos:** Rellena los valores vacios con diferentes posibilidades, ya sea con medidas de tendencia central como la media o la mediana o con métodos mas avanzados según el caso. Esto no fue necesario en nuestro proyecto ya que el dataset no contenía datos nulos.
   - **Manejo de valores atípicos:** Limita los valores extremos para que no afecten demasiado al modelo y no tengan un peso mayor que los demás datos.

4. **Modelación**
   Se realizó una busqueda de hiperparámetros para optimizar cada modelo desarrollado en el proyecto, y se utilizó la herramienta PyCaret para determinar el modelo más apropiado para este caso de estudio.
   Los modelos utilizados fueron:

   - Regresión Lineal
   - Árbol de Decisión
   - KNN
   - Random Forest
   - AdaBoost
   - Gradient Boosting

5. **Evaluación**
   Para nuestro caso de estudio, la métrica más relevante es el **Mean Average Error (MAE)**.

   Dado que los datos provienen de diferentes ubicaciones geograficas, el modelo se puede ver afectado a causa de la diferencia salarial entre un país y otro, además del cambio de moneda. El MAE permite tener una medida más balanceada a pesar de los posibles sesgos en la distribución del salario.

   Aunque los valores atipícos fueron tratados previamente en la transformación de los datos, el MAE no es muy sensible a estos y trata todos los errores por igual lo cual puede ser una ventaja para evaluar el desempeño general del modelo sin dar un peso desproporcionado a errores grandes.

   Además, si este modelo llegase a ser utilizado en una organización, el MAE permitiría una interpretación directa en dolares, permitiendo tener mas claridad en los errores del modelo respecto al salario real.

   El modelo que mejor se ajusta a nuestros datos es el **GradientBoostingRegressor** optimizado a través de la busqueda de hiperparametros con GridSearchCV.

   Este modelo obtuvo las siguientes métricas, haciendo enfásis en el MAE, la métrica de evaluación de mayor importancia para nuestro estudio:

   - Gradient Boosting MAE: 28699.119485597774
   - Gradient Boosting RMSE: 35798.404504122234
   - Gradient Boosting R2 Score: 0.38188008439877064

   Un modelo que permita predecir el salario de un empleado según sus carácteristicas es una herramienta muy útil para una organización. A través de las métricas de evaluación de nuestro modelo, podemos notar que para ser utilizado en producción requeriría modificaciones adicionales que permitan reducir el error, pues esta cifra es alta especialmente en casos con salarios relativamente bajos que no presenten un margen de error tan grande. Además, el R2 de nuestro modelo no es muy alto, lo que significa que hay un bajo porcentaje de los datos que están siendo explicados por las variables independientes incluidas en el modelo.

6. **Despliegue**

   El archivo **pipeline.ipynb** incluye el desarrollo del pipeline con el modelo Gradient Boosting.

   El endpoint desplegado está disponible en la URL pública generada por la instancia EC2. Para esto, se debe correr la API de FastAPI en la instancia, acceder a los grupos de seguridad y agregar una regla con el puerto donde se correrá la API. A través de los detalles de la instancia en AWS se consulta la dirección IPv4 pública que puede ser compartida y consultada para acceder al endpoint de predicción de salario mientras la instancia este activa y en ejecución. Las capturas de pantalla de la API corriendo en la instancia de EC2 se adjuntaron en la carpeta **'multimedia'** de este repositorio.

   PD. Se agregó el diccionario de mapeo a la documentación del endpoint en FastAPI debido a las limitaciones para ejecutar el LabelEncoder en el pipeline. Por lo tanto, aunque no es optimo, se guardó el nuevo dataset con la codificación realizada en el EDA y se trató en el pipeline con los datos codificados.
