# `04` Llamando a una función

Una función podría recibir 0 parámetros y tú puedes devolver algo siempre, incluso si no añades explícitamente el `return`.

:point_up: [Presiona aquí para saber más sobre funciones](https://content.breatheco.de/lesson/working-with-functions-python)

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

Necesitas hacer algo como esto:
```python
area = calculate_area(3,6)
# The value of area will be set to 18
```

# 📝 Instrucciones:

Crea una nueva variable llamada squareArea para cada nueva iteración de la función CalculateArea utilizando las dimensiones de la figura, por ejemplo, para la primera figura,

```python
# For the first figure:
square_area1 = calculate_area(4,4)
```

![img](http://i.imgur.com/VyoJRAL.png)

# 💡 Sugerencia:

- Llama 3 veces a la función `calculate_area`, una por cada cuadrado, pasando la longitud y el borde de cada cuadrado.

:tv: [Video de 9 min sobre funciones en Python](https://www.youtube.com/watch?v=NE97ylAnrz4)
