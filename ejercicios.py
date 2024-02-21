# ejercicio 1
alumno = "Jordan Hudgens"
age = 21 
# cursos_realizados = ("Python, HTML, SCSS") # tupla
cursos_realizados = ["Python", "HTML", "SCSS"] # lista
estudiante = True

print (alumno, age, cursos_realizados, estudiante)

# ejercicio 2
alumno_nik = alumno[:3]
print (alumno_nik)

# ejercicio 3
print (cursos_realizados[0])

# ejercicio 4
age_final = age + 10
print (age_final)

# ejercicio 5
print (cursos_realizados[2])

# ejercicio 6
nombres = 'harry,alex,susie,jared,gail,conner'
nombres_unicos = nombres.split (",")
print (nombres_unicos)

# ejercicio 7
primer_nombre = nombres.split (",")[0]
print (primer_nombre)
primer_nombre_mayusculas = primer_nombre.upper()
nombres_unicos[0] = primer_nombre_mayusculas
print (nombres_unicos)

# ejercicio 8
bithday = f"Feliz {age} cumpleaños, {alumno} !!!"
print(bithday)

# ejercicio 9
print ("hola mundo")