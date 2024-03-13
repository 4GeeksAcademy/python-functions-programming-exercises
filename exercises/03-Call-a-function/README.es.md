---
tutorial: "https://www.youtube.com/watch?v=F7_I8PD38ZQ"
---
# `03` Calling a Function

Una función podría recibir 0 parámetros y devolverá algo siempre, incluso si no añades explícitamente el `return`.

👉 [Clic aquí para saber más sobre funciones](https://4geeks.com/es/lesson/working-with-functions-python-es).

Por ejemplo, una función que calcula el área de un cuadrado sería algo como esto:

```python
def calculate_area(length, width):
    return length * width
```

Si deseas usar esa función para calcular el área de un cuadrado con:

```python
length = 3
width = 6
```

Tendrías que hacer algo como esto:

```python
area = calculate_area(3,6)
# El valor de 'area' sería 18
```

## 📝 Instrucciones:

1. Crea nuevas variables llamadas `square_area1`, `square_area2`, `square_area3` y llama a la función `calculate_area` 3 veces, una por cada cuadrado en la foto, utilizando las dimensiones de la figura, por ejemplo:

```python
# Para la primera figura:
square_area1 = calculate_area(4,4)
```

![Cuadrados](http://i.imgur.com/VyoJRAL.png)

## 💡 Pistas:

- Llama 3 veces a la función `calculate_area`, una por cada cuadrado, pasando la longitud y el ancho de cada cuadrado.

+ 📹 [Video de 9 min sobre funciones en Python](https://www.youtube.com/watch?v=NE97ylAnrz4).
