# `08` Funciones que devuelven

Es una muy buena práctica que las funciones devuelvan algo, incluso si es `None`. 

Si tus funciones devuelven algo, puedes crear algoritmos que usen muchas funciones al mismo tiempo. Por ejemplo, en este caso en particular tenemos dos funciones disponibles:

+ `dollar_to_euro`: que calcula el valor en euros de un valor dado en dólares.

+ `euro_to_yen`: calcula el valor en yenes de un valor dado en euros.

## 📝 Instrucciones:

1. Utilizando las dos funciones disponibles, imprime en la consola el valor de **137** dólares en yenes.

## 💡 Pista:

Trabajando al revés:

- Nuestro valor esperado está en yenes.

- Nuestra función disponible `euro_to_yen` proporcionará eso.

- Para llegar al euro utilizaremos la función disponible `dollar_to_euro`.