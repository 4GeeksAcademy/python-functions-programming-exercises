def render_person(nombre, lugar_nacimiento, color_ojos, edad, sexo):
    return nombre + ' is a ' + str(edad) + ' years old ' + sexo + ' born in ' + lugar_nacimiento + ' with ' + color_ojos + ' eyes'

# No editar debajo de esta línea
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))
