# `06` Funciones Lambda en Python

Una **función lambda** es una función con solo una línea de código y sin nombre.

Es un tipo de función muy especial en el mundo Python porque puedes usarla como una 'pequeña utilidad' para una programación muy ágil:

```python
# declarando una función normal para una multiplicación
def multiply(p1, p2):
    return p1 * p2

# declarándola en una línea como una función lambda
multiply = lambda p1,p2: p1 * p2
```

1. Las **funciones lambda** tiene que ser siempre muy pequeñas.

2. Las **funciones lambda** pueden tener únicamente una línea.

3. Las **funciones lambda** no necesitan un `return`, se asume que lo que haya en esa línea devolverá un valor.

4. Las **funciones lambda** pueden almacenarse en variables o ser pasadas como parámetro a otra función.


## 📝 Instrucciones:

1. Crea una variable llamada `is_odd`.

2. Asígnale una función lambda que devuelva `True` o `False` dependiendo de si un número dado es impar o no.

## 💡 Pista:

+ Así es como declararías una función normal:

```python
# Esta función retorna `True` si el número es impar
def is_odd(num):
    return (num % 2) != 0
```
