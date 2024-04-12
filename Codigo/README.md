 ## Código del algoritmo de reconocimiento facial que se implementará.
El lenguaje de programación que será utilizado es **Python** 

Se planean utilizar las siguientes librerias:
- Cmake
- dlib
- face-recognition
- numpy
- opencv-python

En cuanto al algoritmo de reconocimiento facial que estaremos utilizando, será un modelo pre-entrenado que proporciona la librería de face recognition. El algoritmo utiliza la metodología Haar Cascades o  técnica de clasificación de cascada la cual se basa en la concatenación de varios clasificadores débiles, cada uno analizando una porción diferente de una imagen o frame en el caso de vídeo. Se consideran débiles porque tienen alta probabilidad de dar falso positivo, pero cuando se combinan los resultados, enconjunto, por el contrario, son muy potentes. 

Además, face recognition es utilizada para casi todas las funciones que se necesitan utilizar para manejar rostros. Desde la codificación de la imagen, detectar rostros dentro del módulo de cámara, comparar los rostros que existen entre distintas bases de datos con imágenes, calcular el porcentaje de similitud entre dos rostros, etc. 
