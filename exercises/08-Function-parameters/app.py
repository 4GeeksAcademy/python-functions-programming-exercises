# Your code goes here:
def render_person(name, birth, eyes, age, gender):
    param = f"{name} is a {age} years old {gender} born in {birth} with {eyes} eyes"
    return param


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))