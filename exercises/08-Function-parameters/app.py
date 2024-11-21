# Your code goes here:
def render_person(nombre, nacimiento, color, edad, genero):
    return nombre + ' is a ' + str(edad) + ' years old ' + genero + ' born in ' + str(nacimiento) + ' with ' + color + ' eyes '


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))