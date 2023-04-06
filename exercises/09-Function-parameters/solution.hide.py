# Your code goes here:
def render_person(name, birthdate, eye_color, age, sex):
    return name +" is a "+ str(age) +" years old " + sex +" born in " + birthdate + " with "+eye_color +" eyes"


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))