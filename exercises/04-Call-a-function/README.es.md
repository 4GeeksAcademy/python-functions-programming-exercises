---
tutorial: "https://www.youtube.com/watch?v=NU5iW_bWwmY"
---
# `04` Llamando a una función

Una función podría recibir 0 parámetros y tú puedes devolver algo siempre, incluso si no añades explícitamente el `return`.

:point_up: [Presiona aquí para saber más sobre funciones](https://content.breatheco.de/es/lesson/working-with-functions-python/)

Por ejemplo, una función que calcula el área de un cuadrado sería algo como esto:

```python
def calculate_area(length, edge):
    return length * edge
```

Si deseas usar esa función para calcular el área de un cuadrado con

```python
length = 3
edge = 6
```

Tendrías que hacer algo como esto:

```python
area = calculate_area(3,6)
# El valor del área es 18
```

## 📝 Instrucciones:

1. Crea nuevas variables llamadas `squareArea1`, `square_area2`, `square_area3` y llama a la función `CalculateArea` 3 veces, un por cada cuadrado en la foto, utilizando las dimensiones de la figura, por ejemplo:

```python
# para la primera figura:
square_area1 = calculate_area(4,4)
```

![img](http://i.imgur.com/VyoJRAL.png)

## 💡 Pista:

- Llama 3 veces a la función `calculate_area`, una por cada cuadrado, pasando la longitud y el borde de cada cuadrado.

+ :video_camera: [Video de 9 min sobre funciones en Python](https://www.youtube.com/watch?v=NE97ylAnrz4)
