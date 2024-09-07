# Traducir PDF que tienen imágenes

Levantar el enviroment:
```source translate-env/bin/activate```

Instalar todas las dependencias necesarias:
```pip install -r requirements.txt```


## IMPORTANTE - NO SALTEAR

Cambio por seguridad, si no desactivas esto puede permitir ejecución de código:

1. Ir a la carpeta de la librería que tiene el archivo `recognition.py`, en mi caso es:

```
/<ruta-a-la-carpeta-del-pryecto>/<enviroment>/lib64/python3.11/site-packages/easyocr/recognition.py
```

2. En la línea `182` agregar el parámetro `weights_only` quedando de la siquiente manera:

```
model.load_state_dict(torch.load(model_path, map_location=device, weights_only=True))
```
El motivo es el siguiente:

```
You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. 
```



https://github.com/tesseract-ocr/tessdata/blob/main/spa.traineddata