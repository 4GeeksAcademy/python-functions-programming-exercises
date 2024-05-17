rapid = lambda myStr: myStr[:-1]

# Your code above, please do not change code below
print(rapid("bob")) # Should print "bo"

# [n1:n2:n3] 
# n1 --> donde empezamos a contar, si no ponemos nada empezamos desde el 0
# n2 --> hasta donde contamos. Será hasta el número anterior al que le digamos.
# Si el número es -1 nos referimos hasta el último elemento que haya.
#n3 --> cada cuanto contamos, cada numero, cada 2, cada 3, etc. 

# [1:40:2] Empezamos a contar desde el número 1 hasta el número 39, y contaremos de 2 en 2

