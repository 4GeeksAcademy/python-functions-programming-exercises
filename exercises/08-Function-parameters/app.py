# Your code goes here:
def render_person(name,fecha_nacimiento,color_ojos,age,sex):
    return name+ " is a "+ str(age) + " years old " + sex + " born in " + str(fecha_nacimiento) + " with "+ color_ojos+ " eyes"

# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))