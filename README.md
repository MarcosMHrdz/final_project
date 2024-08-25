# Proyecto Final - Análisis de Coches de Segunda Mano en Wallapop

## Objetivo

    El propósito de este proyecto es realizar un análisis detallado de la oferta de coches de segunda mano en la plataforma Wallapop, centrándose en variables clave como el precio, la marca, el modelo, el kilometraje, el tipo de motor, entre otros atributos relevantes. Adicionalmente, se llevará a cabo una prueba de hipótesis para determinar si existe una diferencia significativa en los precios entre los coches con la etiqueta flag_bumped (destacado) y aquellos que no la tienen, y se aplicarán modelos de aprendizaje automático para analizar la importancia de las diferentes características en las predicciones, para luego poder realizaar algunas sugerencias para la mejorar de la funcion Wallapop Pro .

## Datos
    El conjunto de datos utilizado en este estudio contiene información detallada sobre más de 100,000 publicaciones de coches de segunda mano en Wallapop. Las variables consideradas para el análisis incluyen:

    .Precio (price): Precio del vehículo.
    .Marca (brand): Marca del vehículo.
    .Modelo (model): Modelo específico del vehículo.
    .Kilometraje (km): Distancia recorrida por el vehículo en kilómetros.
    .Tipo de motor (engine): Tipo de motor (gasolina, diésel, eléctrico, etc.).
    .Tipo de caja de cambios (gearbox): Transmisión del vehículo (manual o automática).
    .Ubicación (location.city, location.postal_code, location.province): Ciudad, código postal y provincia donde se encuentra el vehículo.
    .Segmento de marca (gama_marca): Segmento al que pertenece la marca (por ejemplo, premium, estándar).
    .Segmento de precio (gama_precio): Categoría de precio del vehículo.
    .Año de fabricación (year): Año en que fue fabricado el vehículo.
    .Potencia (horsepower): Potencia del vehículo en caballos de fuerza.
    .Indicador de anuncio destacado (flag_bumped): Indicador que señala si el anuncio ha sido destacado  para aumentar su visibilidad.


-
## Exploración de Datos
### Análisis Descriptivo de las Variables Clave

Para obtener una comprensión más profunda de la oferta de coches de segunda mano en Wallapop, se realizó un análisis descriptivo de las .principales variables incluidas en el conjunto de datos.

- Precio: Se examinó la distribución de los precios para identificar la media, la mediana y la dispersión de los precios de los coches. Este análisis permitió detectar patrones de precios según el segmento de mercado, la antigüedad del vehículo y otros factores relevantes.

- Kilometraje: Se analizó la distribución del kilometraje de los vehículos en venta, lo que permitió comprender mejor la relación entre el kilometraje y el precio, así como la distribución general de esta variable entre los diferentes tipos de vehículos.

- Año de Fabricación: Se investigó cómo la antigüedad del vehículo (año de fabricación) afecta el precio y la demanda. Este análisis ayuda a comprender la depreciación del valor de los coches con el paso del tiempo.

- Potencia (Horsepower): Se evaluó la distribución de la potencia de los vehículos en venta y su relación con el precio, identificando si existe una preferencia por vehículos con mayor o menor potencia.

- Tipo de Motor: Se analizó la proporción de vehículos con diferentes tipos de motores (gasolina, diésel, eléctrico, etc.) y cómo esta variable impacta el precio y la preferencia de los compradores.

- Tipo de Caja de Cambios: Se examinó la preferencia por vehículos con transmisión manual frente a automática y cómo esta elección influye en el precio y la demanda.

- Marca y Modelo: Se exploró la frecuencia de las diferentes marcas y modelos presentes en la plataforma, ayudando a identificar las marcas y modelos más populares y su comparación en términos de precio, kilometraje y antigüedad.

- Segmento de Marca y Segmento de Precio: Se analizaron los segmentos de marca y de precio para entender cómo se agrupan los vehículos en categorías específicas y cómo estas categorías afectan el comportamiento del mercado.

Este análisis descriptivo proporciona una visión general sólida del estado del mercado de coches de segunda mano en Wallapop, permitiendo identificar tendencias clave y preferencias de los consumidores.

### Análisis de Correlación
En cuanto al análisis de correlación, se observó que:

El precio de un automóvil está fuertemente influenciado por el año de fabricación y el kilometraje. Los autos más nuevos y con menor kilometraje tienden a tener precios más altos. Además, hay una correlación positiva entre el precio y la potencia del motor.

La correlación entre el kilometraje y el año de fabricación es significativa y negativa. Esta fuerte correlación negativa indica que, en general, los automóviles más nuevos tienden a tener un menor kilometraje. Estos patrones son coherentes con lo que se espera en el mercado automotriz, donde la antigüedad, el desgaste y la potencia son factores clave en la determinación del valor de un vehículo.

### Conclusiones generales de las Variables 

- Precio: La mediana del precio es de 14,000 unidades monetarias, con una concentración significativa entre 8,500 y 19,490.

- Kilometraje: La mediana del kilometraje es de 94,549 km, con una concentración significativa en el rango de 55,000 a 150,000 km.

- Año de Fabricación: La mayoría de los coches fueron fabricados entre 2014 y 2021.

- Potencia (Horsepower): La mayoría de los coches tienen entre 100 y 150 caballos de fuerza.

- Tipo de Caja de Cambios: Las cajas de cambios manuales son mucho más comunes que las automáticas, pero los coches con transmisión automática tienden a ser más caros.

- Tipo de Motor: El motor más común es el diésel, seguido por el de gasolina, y por último, los eléctricos y otros tipos. En términos de precio, los motores eléctricos y otros son los más caros, mientras que los motores de gasolina y especialmente los diésel son más baratos. También se observó que los coches con transmisión automática tienden a tener motores eléctricos con mayor frecuencia.

 -  Marcas y Modelos: En cuanto a maras, podemos observar que las marcas más caras son las de gana de lujo (Ferrari, Lamborghini, Porsche, etc), pero en cuanto a la distribucion, las marcas más ofertada son volkswagen, peugeot, bmw, mercedes, respectivamente, lo cual es interesante ya que las primeras marcas exceptp peugeot son marca considerada como gama premium, despues las siguientes marcas son de gama estandar y económica.

 Encuanto al estudio por las gamas tanto de marca como de precio, podemos observar que las gamas de marca mas economicas y estandar desvalanza su precio debido a las furgonetas y a los coches electricos.

## Herramientas Empleadas
Visualización:

Power BI

Análisis Exploratorio de Datos (EDA): Python

Aprendizaje Automático: Python

Manipulación de Datos: Python

Estructura del Proyecto

Importación de Bibliotecas y Carga del Conjunto de Datos: Configuración inicial del entorno de trabajo.

Visión General del Conjunto de Datos: Exploración y comprensión de la estructura de los datos.

impieza de Datos: Procesamiento de datos faltantes, manejo de outliers y formateo de variables.

Separación de Datos entre Variables Numéricas y Categóricas: Preparación de los datos para el análisis estadístico y el modelado.

Modelos de Machine Learning: Aplicación y evaluación de modelos predictivos.

Conclusiones: Resumen de los hallazgos más relevantes y su interpretación en el contexto del análisis.


## Análisis del Indicador flag_bumped 

En Wallapop, flag_bumped es un indicador que señala si un anuncio ha sido renovado o destacado. Esto significa que el anuncio ha sido actualizado para volver a aparecer en la parte superior de los resultados de búsqueda, lo que incrementa su visibilidad ante los potenciales compradores. Este indicador se activa cuando el usuario decide renovar su anuncio, ya sea manualmente o a través de un plan premium. Esta funcionalidad es particularmente útil cuando un anuncio comienza a perder posiciones en las listas de búsqueda debido a la antigüedad, ayudando a mantener el producto destacado sin necesidad de crear un nuevo anuncio.

### Porcentaje de flag bumped(anuncios destacados)

Podemos ver cómo varía la proporción de anuncios destacados según la categoría de marca y precio..

Gama Marca
- Gama de lujo: 21.28%.
- Gama económica: 17.36%.
- Gama premium: 14.91%.
- Gama estándar: 14.07%.

Gama precio
- Gama muy cara: 23.80%
- Gama cara: 21.76%.
- Gama medio alto: 17.12%
- Gama media: 15.77.57%.
- Gama barato:  10.50%.
- Gama muy barato: 4.16%

Conclusiones Basadas en la Gama de Precio como Segmentación

Tras analizar la proporción de anuncios destacados (flag_bumped) en función tanto de la gama de marca como de la gama de precio, he identificado que la gama de precio ofrece una segmentación más efectiva para optimizar el uso de flag_bumped. A continuación, se detallan las conclusiones y razones para priorizar la gama de precio como criterio de segmentación:

Alta Adopción en Segmentos de Precio Alto:
Gama Muy Cara (23.80%) y Gama Cara (21.76%): Los coches en estos segmentos de precio muestran la mayor proporción de anuncios destacados, lo que indica una clara percepción del valor de flag_bumped en estos mercados. Los vendedores en estas gamas comprenden que la visibilidad adicional es crucial para asegurar ventas rápidas y rentables, dado que los compradores en este segmento están dispuestos a invertir en vehículos costosos y, por lo tanto, la competencia puede ser más intensa.

Segmentos de Precio Medio:
Gama Medio Alto (17.12%) y Gama Media (15.77%): Estos segmentos tienen una adopción moderada de flag_bumped, lo que sugiere que, si bien los vendedores reconocen el beneficio de destacar sus anuncios, puede haber una oportunidad para incentivar aún más su uso. Aquí, la empresa podría implementar estrategias de marketing que demuestren cómo flag_bumped puede ser un diferenciador clave en un mercado competitivo de precios medios, donde los compradores comparan múltiples opciones similares.

Baja Adopción en Segmentos de Precio Bajo:

Gama Barato (10.50%) y Gama Muy Barato (4.16%): La baja proporción de uso de flag_bumped en estos segmentos indica que los vendedores perciben un menor valor en destacar anuncios para coches de bajo precio. Sin embargo, esto presenta una oportunidad para ajustar la estrategia de precios de flag_bumped, ofreciendo tarifas reducidas específicamente para las gamas más bajas. Esto podría incentivar a los vendedores de estos segmentos a utilizar la funcionalidad, aumentando la visibilidad de sus anuncios y acelerando el proceso de venta.

###  Prueba de Hipótesis con t-Student

Para determinar si existe una diferencia significativa en los precios de los coches que tienen el flag_bumped activado en comparación con aquellos que no lo tienen, se plantea la siguiente prueba de hipótesis:

- Hipótesis nula (H₀): No existe una diferencia significativa en los precios entre los coches con flag_bumped y los que no lo tienen; cualquier diferencia observada es atribuible al azar.

- Hipótesis alternativa (H₁): Existe una diferencia significativa en los precios entre los coches con flag_bumped y los que no lo tienen; esta diferencia no es aleatoria.

Se tomará una muestra de precios de coches con y sin flag_bumped, se calculará la media de precios en ambos grupos y se utilizará la prueba t-Student para comparar las medias. Este análisis permitirá determinar si la visibilidad adicional proporcionada por flag_bumped está relacionada con un cambio en el precio de venta.

### Conclusiones de Hipótesis con t-Student

El análisis muestra que los coches con el indicador "flag_bumped" tienen precios significativamente más altos que aquellos sin el indicador. La diferencia en los precios es estadísticamente significativa, lo que sugiere que "flag_bumped" es un factor importante que influye en el precio de los coches.

Para realizar un estudio más detallado sobre el efecto del precio en relación con "flag_bumped", hemos formulado la hipótesis desde dos perspectivas diferentes: la gama de marca y la gama de precio.

Gama de Marca:
En todas las categorías de coches (económicos, estándar, premium y de lujo), el indicador "flag_bumped" está asociado con precios más altos. Esta tendencia es estadísticamente significativa, lo que indica que "flag_bumped" es un factor clave en la determinación de precios, siendo especialmente influyente en las categorías económicas y estándar, y menos en las categorías premium y de lujo.

Gama de Precio:
En general, el "flag_bumped" tiende a aumentar los precios en la mayoría de las categorías de coches. Sin embargo, en la categoría de coches muy baratos, parece tener el efecto contrario, posiblemente debido a una mayor urgencia de venta.


##  Modelos de Machine Learning
Se han utilizado diferentes modelos de clasificacion con regresion logistica, incluyendo KNN y Random Forest, aplicando técnicas como SMOTE para balancear las clases. Además, se ha realizado un análisis de la importancia de las características (Feature Importance) en el modelo de Random Forest para identificar cuáles variables tienen un mayor impacto en las predicciones. Esto proporciona insights sobre los factores que más influyen en la decisión de renovar o destacar un anuncio (bumping).

### Conclusiones del modelo

- El modelo Random Forest con SMOTE ha mostrado un bueb rendimiento en términos de precisión y recall, manejando bien el desequilibrio en las clases.
- La validación cruzada confirma la robustez del modelo, con un rendimiento estable a través de distintos conjuntos de datos.
- La importancia de las características sugiere que "location.postal_code", "km", y "price" son los atributos más importantes para el modelo. Esto implica que la ubicación, el kilometraje y el precio del vehículo son los factores más determinantes en la predicción.
Otras características como "location.city", "model", y "horsepower" también tienen importancia, aunque en menor medida.

## Sugerencias

- Ofertas Personalizadas: 
En las gamas altas, combinar flag_bumped con servicios que potencien la visibilidad, como la ampliación del tiempo de anuncio destacado, puede ser efectivo. 
Para las gamas bajas, promociones específicas podrían mejorar la adopción de flag_bumped.

- Posicionamiento Prioritario en Resultados de Búsqueda: 
Ofrecer a los vendedores la opción de que sus anuncios aparezcan en las primeras posiciones de los resultados de búsqueda dentro de su categoría de precio. Esto aumentaría significativamente la visibilidad de sus coches frente a otros, captando la atención de compradores interesados en vehículos de alto valor.

- Pruebas A/B: 
Implementar pruebas que consideren tanto la gama de precio como características clave como la localización y el kilometraje, permitirá optimizar las estrategias de marketing y maximizar el retorno de inversión.


Conclusión:
Integrando los análisis realizados sobre las proporciones de uso de flag_bumped por gama de precio y marca, junto con estrategias de segmentación, promociones, y educación del cliente, se pueden crear campañas de marketing más efectivas que no solo incrementen el uso de flag_bumped, sino que también mejoren la satisfacción del cliente al permitirles aprovechar al máximo la visibilidad adicional que esta funcionalidad proporciona. Esto, en última instancia, ayudará a la empresa a incrementar sus ingresos y fortalecer su posición en el mercado de coches de segunda mano.

## Conclusiones:

Integrar la importancia de las características clave en el análisis de la gama de precios proporciona una segmentación más rica y matizada. Al centrar las estrategias de marketing en cómo estas características influyen en la percepción del valor de flag_bumped, la empresa puede crear campañas más efectivas, que no solo incrementen el uso de flag_bumped, sino que también optimicen la satisfacción del cliente y los ingresos. Esto fortalecerá la posición de la empresa en el mercado de coches de segunda mano, asegurando que tanto los vendedores como los compradores vean un valor claro en la plataforma.