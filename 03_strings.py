### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Beni", "Estévez", 20

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)

# División

language_slice = language[1:3] # se empiezan a contar las letras en 0
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2] # empezando por el final
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize()) # escribe la primera letra en mayúsucla
print(language.upper()) # escribe toda la cadena en mayúsculas
print(language.count("t")) # cuenta el número de letras indicadas que hay en la cadena
print(language.isnumeric()) # nos indica si la cadena es un número
print("1".isnumeric())
print(language.lower()) # escribe toda la cadena en minúsculas
print(language.lower().isupper()) # ponemos la cadena a minúsculas y comprobamos si está en mayúscula
print(language.startswith("py")) # nos dice si la cadena empieza por las letras que le indico (distingue mayúsculas de minúsculas)

