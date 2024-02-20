# ejercicio 1
alumno = "Jordan Hudgens"
age = 21 
cursos_realizados = ("Python, HTML, SCSS")
estudiante = True

print (alumno, age, cursos_realizados, estudiante)

# ejercicio 2
alumno_nik = alumno[:3]
print (alumno_nik)

# ejercicio 3
primer_curso = cursos_realizados.find(",")
print (primer_curso)
primer_curso = cursos_realizados[:6]
print (primer_curso)

# ejercicio 4
age_final = age + 10
print (age_final)

# ejercicio 5
ultimo_curso = cursos_realizados[-4:]
print (ultimo_curso)

# ejercicio 6
nombres = 'harry,alex,susie,jared,gail,conner'
nombres_unicos = nombres.split (",")
print (nombres_unicos)

# ejercicio 7
primer_palabra = nombres_unicos[0].upper()
print (primer_palabra)
nombre_mayusculas = nombres.replace("harry", primer_palabra)
print (nombre_mayusculas)

# ejercicio 8
bithday = f"Feliz {age} cumpleaños, {alumno} !!!"
print(bithday)

# ejercicio 9
print ("hola mundo")