# Proyecto Final - Análisis de Coches de Segunda Mano en Wallapop

## Objetivos

El propósito de este proyecto es realizar un análisis detallado de la oferta de coches de segunda mano en la plataforma Wallapop, centrándome en variables clave como el precio, la marca, el modelo, el kilometraje, el tipo de motor, entre otros atributos relevantes. 

Además, se llevará a cabo una prueba de hipótesis para determinar si existe una diferencia significativa en los precios entre los coches con la etiqueta flag_bumped (destacado) y aquellos que no la tienen.

También aplicarán machine learning para analizar la importancia de las diferentes características en las predicciones, para luego poder realizar algunas sugerencias para la mejora de la función Wallapop Pro.

## Datos
El conjunto de datos utilizado en este estudio contiene información detallada sobre más de 100.000 publicaciones de coches de segunda mano en Wallapop. 
Las variables consideradas para el análisis incluyen:

- Precio (price): Precio del vehículo. 
- Marca (marca): Marca del vehículo. 
- Modelo (modelo): Modelo específico del vehículo. 
- Kilometraje (km): Distancia recorrida por el vehículo en kilómetros. 
- Tipo de motor: Tipo de motor (gasolina, diésel, eléctrico, etc.). 
- Tipo de caja de cambios (gearbox): Transmisión del vehículo (manual o automática). 
- Ubicación (ubicación.ciudad, ubicación.código_postal, ubicación.provincia): Ciudad, código postal y provincia donde se encuentra el vehículo.
- Segmento de marca (gama_marca): Segmento al que pertenece la marca (por ejemplo, premium, estándar).
- Segmento de precio (gama_precio): Categoría de precio del vehículo. 
- Año de fabricación (year): Año en que fue fabricado el vehículo. .
- Potencia (horsepower): Potencia del vehículo en caballos de fuerza. 
- Indicador de anuncio destacado (flag_bumped): Indicador que señala si el anuncio ha sido destacado para aumentar su visibilidad.

## Metodología y herramientas
- Realizar scraping web para obtener los datos. (Python)
- Importación de Bibliotecas (Python)
- Carga del Conjunto de Datos: (Python)
- Visión General del Conjunto de Datos: Exploración y comprensión de la estructura de los datos. (Python)
- Limpieza de datos: Procesamiento de datos faltantes, eliminación de columnas no necesarios, mejorar los errores sobre las marcas de los automóviles, manejo de valores atípicos y formato de variables. (Python y Power BI)
- Separación de Datos entre Variables Numéricas y Categóricas: Preparación de los datos para el análisis estadístico y el modelado. (Python)
- Matriz de correlación: Python
- Manipulación de datos: Python y Power BI
- Modelos de Machine Learning: Aplicación y evaluación de modelos predictivos. (Python)
- Visualización: Realizar un dashboard (Power BI)
- Conclusiones: Resumen de los hallazgos más relevantes y su interpretación en el contexto del análisis.

## Exploración de datos

### Análisis Descriptivo de las Variables Clave
Para obtener una comprensión más profunda de la oferta de coches de segunda mano en Wallapop, he realizado un análisis descriptivo de las principales variables incluidas en el conjunto de datos.
Precio: He examinado la distribución de los precios para identificar la media, la mediana y la dispersión de los precios de los coches. Con este análisis he podido encontrar patrones de precios según el segmento de mercado, la antigüedad del vehículo, el precio y otros factores relevantes.

- Kilometraje: He analizado la distribución del kilometraje de los vehículos en venta, lo que permitió comprender mejor la relación entre el kilometraje y el precio, así como la distribución general de esta variable entre los diferentes tipos de vehículos.

- Año de Fabricación: He podido ver cómo la antigüedad del vehículo (año de fabricación) afecta el precio y la demanda. Este análisis ayuda a comprender la depreciación del valor de los coches con el paso del tiempo.

- Potencia (Horsepower): He evaluado la distribución de la potencia de los vehículos en venta y su relación con el precio, identificando si existe una preferencia por vehículos con mayor o menor potencia.

- Tipo de Motor: He analizado la proporción de vehículos con diferentes tipos de motores (gasolina, diésel, eléctrico, etc.) y cómo esta variable impacta el precio y la preferencia de los compradores.

- Tipo de Caja de Cambios: He examinado la preferencia por vehículos con transmisión manual frente a automática y cómo esta elección influye en el precio y la demanda.

- Marca y Modelo: He explorado la frecuencia de las diferentes marcas y modelos presentes en la plataforma, ayudando a identificar las marcas y modelos más populares y su comparación en términos de precio, kilometraje y antigüedad.

- Segmento de Marca y Segmento de Precio: He analizado los segmentos de marca y de precio para entender cómo se agrupan los vehículos en categorías específicas y cómo estas categorías afectan el comportamiento del mercado.
Este análisis descriptivo proporciona una visión general del estado del mercado de coches de segunda mano en Wallapop, permitiendo identificar tendencias claves y preferencias de los consumidores.

### Análisis de correlación
El precio de un automóvil está fuertemente correlacionado por el año de fabricación y el kilometraje. Los autos más nuevos y con menor kilometraje tienden a tener precios más altos. Además, hay una correlación positiva entre el precio y la potencia del motor.

La evaluación entre el kilometraje y el año de fabricación es significativa y negativa, lo que quiere decir, en general, los automóviles más nuevos tienden a tener un menor kilometraje. Estos patrones son coherentes con lo que se espera en el mercado automotriz, donde la antigüedad, el desgaste y la potencia son factores clave en la determinación del valor de un vehículo.

## Análisis del indicador de destacados (flag_bumped)
En Wallapop, flag_bumped es un indicador que señala si un anuncio ha sido destacado. Esto significa que el anuncio ha sido actualizado para volver a aparecer en la parte superior de los resultados de búsqueda, lo que incrementa su visibilidad ante los potenciales compradores. 
Este indicador se activa cuando el usuario decide renovar su anuncio, a través de un plan Premium (Wallapop Pro), o pagando solo por destacar el anuncio dependiendo de cuantos días (7,15,30 días) y en qué lugar (zona, ciudad, país)
Porcentaje de bandera anuncios destacados (flag_bumped)
Podemos ver cómo varía la proporción de anuncios destacados según la categoría de marca y precio.

Gama Marca
- Gama de lujo: 21,28%.
- Gama económica: 15,65%.
- Prima Gama: 14,91%.
- Gama estándar: 14,83%.

Gama de Precios
- Gama muy cara: 22,82%
- Gama cara: 20,24%.
- Gama media alta: 16,76%
- Gama media: 15,59%.-
- Gama barata: 14,65%.
- Gama muy barata: 5,20%

## Test de Hipótesis con t-Student

También he realizado una prueba de hipótesis para determinar si existe una diferencia significativa en los precios de los coches que tienen el flag_bumped (anuncios destacados) activado en comparación con aquellos que no lo tienen, se plantea la siguiente prueba de hipótesis:

- Hipótesis nula (H₀): No existe una diferencia significativa en los precios entre los coches con flag_bumped (anuncios destacados) y los que no lo tienen; cualquier diferencia observada es atribuible al azar.
- Hipótesis alternativa (H₁): Existe una diferencia significativa en los precios entre los coches con flag_bumped (anuncios destacados) y los que no lo tienen; esta diferencia no es aleatoria.

Se tomará una muestra de precios de coches con y sin flag_bumped (anuncios destacados), se calculará la media y la mediana de los precios en ambos grupos y se utilizará la prueba t-Student para comparar las medias. Este análisis permitirá determinar si la visibilidad adicional proporcionada por flag_bumped(anuncios destacados) está relacionada con un cambio en el precio de venta.

## Modelos de machine learning

He utilizado diferentes modelos de clasificación con regresión logística, incluyendo KNN y Random Forest, aplicando técnicas como SMOTE para equilibrar las clases. Además, se ha realizado un análisis de la importancia de las características (Feature Importance) en el modelo de Random Forest para identificar qué variables tienen un mayor impacto en las predicciones. Esto proporciona información sobre los factores que más influyen en la decisión de renovar o destacar un anuncio (bumping)

## Conclusiones:

### Conclusiones generales de las Variables

- La media del precio es de 14.400 unidades, con una concentración significativa entre 8.500 y 19.500

- En cuanto a la correlación, podemos decir que el precio de los automóviles aumenta cuando sea más nuevo, menos kilómetros tenga y tenga mas potencia.

- Las cajas de cambios manuales son mucho más comunes que las automáticas, pero los coches con transmisión automática tienden a ser más caros.

- El motor más común es el diésel, seguido por el de gasolina, y, por último, los eléctricos y otros tipos. En cuanto al precio, los motores eléctricos y otros son los más caros, mientras que los motores de gasolina y especialmente los de diésel son más baratos. 
Los coches con transmisión automática tienden a tener motores eléctricos.

- La cantidad de oferta de coches segunda mano, está en Madrid, Barelona y la costa en general.

- En cuanto a maras, podemos observar que las marcas más caras son las de gana de lujo (Ferrari, Lamborghini, Porsche, etc.), pero en cuanto a la cantidad de vehículos, las marcas más ofertadas son Volkswagen, Peugeot, bum, Mercedes, respectivamente, lo cual es interesante ya que las primeras marcas excepto Peugeot son marca considerada como gama Premium.

- En cuanto a la gama de marcas, puedo decir que la mayoría de las ofertas son de coches de gama ¨estándar¨ y gama ¨Premium¨. 

- La mayoría de los vehículos de la gama ¨estándar¨ con precios elevevados son vehículos con pocos años, y motores eléctricos, además de furgonetas. 

### Conclusiones Basadas en las Gamas como Segmentación

He analizado la proporción de anuncios destacados (flag_bumped) tanto por gama de marca como por gama de precio, y puedo observar que, en cuanto a la gama de marcas, la gama de lujo tiene el mayor porcentaje de uso del flag_bumped. Esto se debe a que los coches de esta gama suelen ser muy caros, y tanto los vendedores como los compradores en este segmento suelen tener un alto poder adquisitivo. Dado el alto valor de estos coches, los vendedores están dispuestos a invertir más en destacar sus anuncios para maximizar la visibilidad y atraer a compradores específicos que buscan productos exclusivos. Las otras gamas de marcas tienen un porcentaje de uso del flag_bumped más parecido entre sí.
La segmentación por gama de precio proporciona una guía más clara y efectiva para entender y optimizar el uso del flag_bumped. Existe una correlación positiva entre el precio de la gama y el uso de esta funcionalidad: los anuncios en gamas de precios más altos tienden a utilizar flag_bumped con mayor frecuencia para aumentar la visibilidad y atraer a compradores con mayor poder adquisitivo.
Conclusiones de Hipótesis con t-Student

El análisis muestra que los coches con el indicador "flag_bumped" tienen precios significativamente más altos que aquellos sin el indicador.
Para realizar un estudio más detallado sobre el efecto del precio en relación con "flag_bumped", hemos formulado la hipótesis desde dos perspectivas diferentes: la gama de marca y la gama de precio.
Como conclusión puedo decir que en general, el efecto del flag_bumped en los precios de coches de segunda mano es significativo en la mayoría de las gamas tanto por marca, como por precios, donde se observa que destacar un coche puede aumentar su precio de venta. No obstante, para coches de la gama por marca de “lujo” y en la gama por precio "muy caro," el flag_bumped no tiene un impacto perceptible en el precio, probablemente debido a diferentes factores de comportamiento del consumidor en este segmento de lujo, como por ejemplo un mayor poder adquisitivo, y enoicarse  más en la exclusividad.

### Conclusiones del modelo

El modelo Random Forest con SMOTE ha mostrado un buen rendimiento en términos de precisión y recuperación, manejando bien el desequilibrio en las clases.

La validación cruzada confirma la robustez del modelo, con un rendimiento estable a través de distintos conjuntos de datos.

La importancia de las características sugiere que "location.postal_code", "km", y "price" son los atributos más importantes para el modelo. Esto implica que la ubicación, el kilometraje y el precio del vehículo son los factores más determinantes en la predicción. Otras características como "ubicación.ciudad", "modelo" y "caballos de fuerza" también tienen importancia, aunque en menor medida.

## Sugerencias

### Wallapop

- Alertas Personalizadas: Envía notificaciones personalizadas cuando los anuncios de los usuarios están perdiendo visibilidad o cuando hay un aumento en la demanda de coches similares en su área.

- Sistema de Puntos o Recompensas: Implementa un sistema de puntos o recompensas donde los usuarios ganan puntos por destacar anuncios o realizar otras acciones en la plataforma. Estos puntos pueden canjearse por descuentos en futuros anuncios destacados.

- Mostrar Impacto en Visibilidad y Ventas: Utiliza estadísticas claras en la plataforma para mostrar cómo los anuncios destacados mejoran la visibilidad y las tasas de venta. Por ejemplo, mostrar datos como “Los anuncios destacados se ven X veces más que los no destacados.”

- Casos de Éxito: Comparte historias de éxito de otros usuarios que vendieron sus coches rápidamente usando anuncios destacados. Esto puede motivar a otros a invertir en la destacación de sus anuncios.

### Wallapop PRO.

- Segmentación por Ubicación: Identifica concesionarios en zonas con alta competencia o demanda y ofrece promociones o descuentos en Wallapop PRO, destacando cómo pueden mejorar su visibilidad en mercados competitivos.

- Análisis y Optimización de Precios: Ofrece a los concesionarios informes personalizados y herramientas dentro de Wallapop PRO para ajustar estrategias de venta basadas en tendencias de precios y características específicas de los coches en su área. Incluye algoritmos que recomienden rangos de precios óptimos para maximizar ventas, aprovechando el historial de datos para destacar anuncios de manera más efectiva.

- Casos de Éxito Localizados: Comparte casos de éxito de concesionarios similares que han mejorado sus ventas con Wallapop PRO.

- Crea un programa de lealtad con bonificaciones por uso frecuente de Wallapop PRO.

- Ofrece períodos de prueba gratuitos o tarifas iniciales reducidas para nuevos concesionarios

- Implementa alertas automatizadas para sugerir ajustes de precios y destacar anuncios basados en datos recientes.

