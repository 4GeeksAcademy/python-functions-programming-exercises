<!-- hide -->
<div align="center">

# Aprende las funciones de Python Interactivamente

![Certificado por 4Geeks Academy](https://img.shields.io/badge/certificado%20por-4Geeks%20Academy-2563eb) ![Autocorregido con LearnPack](https://img.shields.io/badge/autocorregido-LearnPack-2563eb) [![Abrir en GitHub Codespaces](https://img.shields.io/badge/abrir%20en-GitHub%20Codespaces-fb5a1f?logo=github&logoColor=white)](https://codespaces.new/?repo=4GeeksAcademy/python-functions-programming-exercises)

</div>

*Estas instrucciones también están disponibles en [🇺🇸 inglés](https://github.com/4GeeksAcademy/python-functions-programming-exercises/blob/HEAD/README.md).*
<!-- endhide -->

Este tutorial de LearnPack enseña las funciones de Python con 10 ejercicios interactivos: una página de bienvenida y 9 retos autocorregidos. Vas a imprimir tu primera línea en la consola, declarar y llamar funciones, escribir expresiones lambda, encadenar el resultado de una función dentro de otra, construir una función de cinco parámetros y ordenar una lista de nombres. Cada ejercicio corregido trae pruebas con pytest y un vídeo. Duración estimada: 10 horas.

<!-- hide -->
## 📋 Ficha del tutorial

- **Dificultad:** fácil (nivel principiante, justo después de lo básico de Python).
- **Duración estimada:** 10 horas.
- **Ejercicios:** 10 carpetas — 1 de bienvenida y 9 con corrección automática.
- **Tecnologías:** Python 3, pytest y LearnPack.
- **Corrección:** automática, 9 ejercicios con fichero de pruebas y 39 comprobaciones en total.
- **Extras:** un vídeo de YouTube enlazado en cada ejercicio y un `solution.hide.py` de referencia en cada ejercicio corregido.
- **Idiomas:** español e inglés (cada ejercicio tiene `README.es.md` y `README.md`).

![Portada del tutorial de funciones de Python: una tarjeta color crema con el texto PYTHON FUNCTIONS TUTORIAL, el logo azul y amarillo de Python y un pie negro que dice TIME TO CODE](https://raw.githubusercontent.com/4GeeksAcademy/python-functions-programming-exercises/master/python-functions-badge.png)
<!-- endhide -->

## 🎯 ¿Qué vas a aprender?

El tutorial avanza desde el primer `print()` hasta funciones que se alimentan de otras funciones, paso a paso:

- Cómo declarar una función con `def`, ponerle parámetros e indentar bien su cuerpo.
- La diferencia entre **declarar** una función y **llamarla**, y por qué no pasa nada hasta que la llamas.
- Cómo funciona el `return` y por qué una función que devuelve un valor da mucho más juego que una que solo imprime.
- Cómo escribir **funciones lambda**: funciones de una sola línea, sin nombre propio, que guardas en una variable o pasas como argumento.
- Cómo combinar funciones y usar la salida de una como entrada de la siguiente.
- Cómo diseñar una función con varios parámetros y elegir nombres que se expliquen solos.
- Cómo aprovechar utilidades de listas como `sorted()` dentro de tus propias funciones.

## 👀 ¿Qué vas a construir?

Nueve ejercicios corregidos automáticamente; cada uno es un programa pequeñito que completas dentro de `app.py`:

1. **`01` Hello World** — usa `print()` para mostrar exactamente `Hello World` en la consola.
2. **`02` ¿Qué es una función?** — reutiliza la función `sum(number1, number2)` que ya viene escrita para guardar el resultado de `3445324 + 53454423` en una variable llamada `super_duper`.
3. **`03` Llamar a una función** — llama tres veces a la función `calculate_area(length, width)` que ya viene escrita y guarda el área de cada cuadrado en `square_area1`, `square_area2` y `square_area3`: 16, 4 y 25.
4. **`04` Declarar vs. llamar** — declara desde cero la función `multi`, que recibe dos números y devuelve su multiplicación.
5. **`05` Funciones lambda** — asigna a `is_odd` una lambda que devuelva `True` cuando el número sea impar y `False` cuando no lo sea.
6. **`06` Funciones lambda II** — asigna a `rapid` una lambda que devuelva la misma cadena sin su último carácter, de modo que `"maria"` se convierta en `"mari"`.
7. **`07` Funciones que devuelven** — encadena los dos conversores que se te dan, `dollar_to_euro` y `euro_to_yen`, para imprimir cuánto valen 137 dólares en yenes: `20159.139`.
8. **`08` Parámetros de una función** — construye `render_person` con cinco parámetros para que devuelva una frase como `Bob is a 23 years old male born in 05/22/1983 with green eyes`.
9. **`09` Métodos de listas** — escribe `sort_names` para que, dada una lista de nombres, la devuelva ordenada alfabéticamente.

La décima carpeta, `00-Welcome`, es la introducción: sin código ni pruebas, solo el mapa del tutorial y el vídeo de presentación.

## 🎓 ¿Qué necesitas antes de empezar?

- **Solo lo básico de Python.** Con variables, números, cadenas y `print()` te sobra; las funciones son justo lo que vienes a aprender aquí.
- **Un navegador**, si trabajas en GitHub Codespaces o en la plataforma online. No hay nada que instalar.
- **Python 3 y Node.js 14+**, únicamente si prefieres ejecutar los ejercicios en tu propio ordenador con LearnPack.
- **Ninguna experiencia previa con pytest.** Las pruebas ya están escritas; tú solo lees sus mensajes.

## ✅ ¿Cómo funciona la corrección automática?

Cada uno de los 9 ejercicios corregidos incluye un fichero de pruebas hecho con pytest (`test.py` en los ejercicios `01` y `07`, `tests.py` en el resto). Al pulsar el botón de compilar o de probar, LearnPack ejecuta esas comprobaciones contra tu `app.py` y te devuelve una línea verde o roja por cada una, con el mensaje declarado en `@pytest.mark.it(...)`, por ejemplo *"The function multi must receive two numbers and return their multiplication"*.

Las pruebas miran tres cosas distintas, y saber cuál está fallando te ahorra mucho tiempo:

- **El código fuente de `app.py`**, con una expresión regular. El ejercicio `05` busca literalmente `is_odd = lambda`, y el `03` comprueba que en alguna línea escribas `= calculate_area(`.
- **El valor que devuelve tu función**, importándola y llamándola con datos fijos, como `app.multi(3, 4) == 12` o `app.calculate_area(5, 4) == 20`.
- **El texto impreso en la consola**, capturado y comparado carácter a carácter, como `"20159.139\n"` en el ejercicio `07`.

Las pruebas son adrede muy estrictas, así que interpreta una línea roja como una pista sobre la sintaxis o el texto exacto que se te pide, no como un juicio sobre tu lógica.

## 💡 ¿Qué errores conviene evitar?

- **Imprimir cuando lo que se pide es devolver.** En el `08` la prueba llama a `render_person('ax','b','c','d','e')` y compara la cadena devuelta, mientras que `app.py` ya se encarga de imprimirla. Una función que solo hace `print` suspende.
- **Equivocarte con el orden de los parámetros del `08`.** La frase esperada es `ax is a d years old e born in b with c eyes`, así que el orden es: nombre, fecha de nacimiento, color de ojos, edad y género.
- **Usar `def` donde se pide una lambda.** En el `05` y el `06` la prueba lee tu fichero buscando `is_odd = lambda` y `rapid = lambda`. Un `def` normal falla la comprobación aunque el comportamiento sea correcto.
- **Devolver `list.sort()` en el `09`.** El método `sort()` ordena la lista en el sitio y devuelve `None`. Devuelve `sorted(names)` y no borres la línea `print(sort_names(names))`, porque la prueba compara la salida de la consola con `['Bob', 'Dilan', 'John', 'Kenny', 'Tom']`.
- **Formatear o redondear el número del `07`.** La consola tiene que mostrar exactamente `20159.139`: llama primero a `dollar_to_euro(137)` y pasa ese resultado a `euro_to_yen`, sin tocar los decimales.
- **Borrar el código que ya viene escrito.** El `02` necesita la función `sum()` que te dan, porque la prueba la importa. En el `04`, el `06`, el `08` y el `09` las líneas marcadas como "no cambiar" llaman a tu función con valores fijos, y en el `09` la prueba lee exactamente lo que imprime esa línea.

## ❓ Preguntas frecuentes

### ¿Necesito instalar Python para empezar?

No. Abriendo el repositorio en GitHub Codespaces tienes un entorno listo con Python, LearnPack y los ejercicios ya cargados, y el mismo tutorial también se ejecuta en la plataforma online. Instalarlo en local es opcional y solo requiere Python 3 y Node.js 14 o superior.

### ¿En qué se diferencia una función `def` de una función lambda en Python?

Una función declarada con `def` tiene nombre, ocupa las líneas que necesites y solo devuelve un valor cuando escribes `return`. Una [lambda](https://docs.python.org/3/reference/expressions.html#lambda) es una única expresión sin nombre propio, que normalmente guardas en una variable (`is_odd = lambda num: num % 2 != 0`) y que devuelve el resultado de esa expresión automáticamente. Los ejercicios `04` a `06` te hacen escribir los dos estilos para el mismo tipo de problema.

### ¿Cuánto se tarda en terminar el tutorial de funciones?

El paquete está estimado en 10 horas y su dificultad es fácil. Los 9 ejercicios corregidos son cortos, así que mucha gente los termina en un par de sesiones; el tiempo real depende de cuánto experimentes con el código más allá de lo que te pide la prueba.

### ¿Son gratis estos ejercicios? ¿Puedo reutilizarlos?

Acceder no cuesta nada y el código que escribas en `app.py` es tuyo. El contenido del tutorial, en cambio, no es de código abierto: el fichero [LICENSE.md](https://github.com/4GeeksAcademy/python-functions-programming-exercises/blob/HEAD/LICENSE.md) de este tutorial de 4Geeks Academy reserva todos los derechos de propiedad intelectual y no permite republicar, vender, sublicenciar ni redistribuir el material.

### ¿Por qué falla el ejercicio si mi resultado parece correcto?

Porque casi todas las comprobaciones comparan cadenas exactas. Una mayúscula que falta en `Hello World`, un espacio de más, un decimal redondeado o un `def` donde se pedía una lambda bastan para dejar la línea en rojo. Lee la frase que acompaña a la prueba fallida: te dice la función, los datos de entrada y el valor esperado.

### ¿Los ejercicios están también en inglés?

Sí. Las 10 carpetas traen `README.es.md` y `README.md`, así que instrucciones, pistas y ejemplos están completos en los dos idiomas. El código, los nombres de las funciones y los mensajes de las pruebas siguen en inglés, igual que en cualquier proyecto real.

<!-- hide -->
## 📚 Tutoriales relacionados

Si quieres seguir practicando Python con el mismo formato interactivo y autocorregido:

1. [Aprende Python Interactivamente (principiante)](https://4geeks.com/es/interactive-exercise/python-beginner-exercises-es) — variables, condicionales y lo básico previo a este tutorial.
2. [Aprende listas y bucles de Python](https://4geeks.com/es/interactive-exercise/python-loops-lists-exercises-es) — el paso natural después de las funciones.
3. [Aprende Programación Orientada a Objetos con Python](https://4geeks.com/es/interactive-exercise/aprende-programacion-orientada-a-objetos-con-python) — clases, objetos y métodos.
4. [Domina Python Practicando](https://4geeks.com/es/interactive-exercise/master-python-exercises-es) — una tanda más larga de retos para consolidarlo todo.
5. [Trabajando con funciones en Python](https://4geeks.com/lesson/trabajando-con-funciones-en-python) — la lección escrita que hay detrás de estos ejercicios.

## 🚀 ¿Cómo empezar?

Lo más rápido es un clic: [Abrir en Codespaces](https://codespaces.new/?repo=4GeeksAcademy/python-functions-programming-exercises) (recomendado) o [Abrir en Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/python-functions-programming-exercises).

Cuando se abra VS Code, los ejercicios de LearnPack deberían arrancar solos. Si no lo hacen, escribe `learnpack start` en la terminal.

![Vista previa animada del tutorial de LearnPack dentro de VS Code: el editor de código con app.py a la izquierda y las instrucciones del ejercicio con los botones Previous y Next a la derecha](https://raw.githubusercontent.com/4GeeksAcademy/python-functions-programming-exercises/master/preview.gif)

## 💻 Instalación local

1. Instala [LearnPack](https://learnpack.co) y su plugin de Python. Antes necesitas Node.js 14+ y Python 3+.

   ```bash
   npm i -g @learnpack/learnpack@2.1.20 && learnpack plugins:install @learnpack/python@1.0.0
   ```

2. Clona o descarga este repositorio en tu entorno local.

   ```bash
   git clone https://github.com/4GeeksAcademy/python-functions-programming-exercises.git
   cd python-functions-programming-exercises
   ```

3. Instala las dependencias de las pruebas y arranca el tutorial desde la raíz del proyecto.

   ```bash
   pip3 install pytest==6.2.5 pytest-testdox mock
   learnpack start
   ```

Cuando termine la descarga verás una carpeta `exercises` con todos los ejercicios dentro.

## 📝 ¿Cómo están organizados los ejercicios?

Cada ejercicio corregido es una pequeña aplicación de Python con los mismos ficheros:

1. **`app.py`** — el fichero que editas y el que ejecuta el ordenador.
2. **`README.md`** y **`README.es.md`** — las instrucciones, las pistas y el vídeo, en los dos idiomas.
3. **`test.py`** o **`tests.py`** — el script de corrección. No hace falta que lo abras, aunque leerlo es la forma más rápida de entender qué se te está pidiendo.
4. **`solution.hide.py`** — una solución de referencia que LearnPack mantiene oculta mientras trabajas.

## 🤝 Colaboradores

Gracias a estas personas maravillosas ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

1. [Alejandro Sánchez (alesanchezr)](https://github.com/alesanchezr) — programador 💻, idea 🤔, build-tests ⚠️, pull-request-review 👀, build-tutorial ✅, documentación 📖.
2. [Paolo (plucodev)](https://github.com/plucodev) — reporte de errores 🐛, programador 💻, traducción 🌎.
3. [Marco Gómez (marcogonzalo)](https://github.com/marcogonzalo) — reporte de errores 🐛, traducción 🌎.

Este proyecto sigue la especificación [all-contributors](https://github.com/kentcdodds/all-contributors). Toda contribución es bienvenida: si encuentras un error o una falta de ortografía, [abre un issue](https://github.com/learnpack/learnpack/issues/new) o manda un pull request. Consulta [todos los colaboradores](https://github.com/4GeeksAcademy/python-functions-programming-exercises/graphs/contributors).

Este y otros muchos ejercicios los construyen los estudiantes del [Coding Bootcamp](https://4geeksacademy.com/es/coding-bootcamp) de 4Geeks Academy, con [Alejandro Sánchez](https://github.com/alesanchezr) y muchos otros colaboradores. Conoce más sobre nuestro [curso de programación desde cero](https://4geeksacademy.com/es/curso-de-programacion-desde-cero), el bootcamp de [Desarrollador Full Stack](https://4geeksacademy.com/es/coding-bootcamps/desarrollador-full-stack) o el de [Data Science y Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning).
<!-- endhide -->
