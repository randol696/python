import random2

movies_list = ['Ahir Ahir Henil',
'Ahir Ahir Mihir Arvind',
'Ahir Herry Hiteshbhai',
'Armelino Rivera Israel Nicolas',
'Baso Jaen Alex Gabriel',
'Batista Rivera Montserrat Johana',
'Carmona Guillen Maria Gabriela',
'Castillo Diaz Ariel Augusto',
'Chong Feng Ricardo Joe',
'Concepción Macías Diego Alejandro',
'Duran De Gracia Librada Del Carmen',
'Erne Athanasiadis Jorge Alexis',
'Lopez Ledezma Renata Marcela',
'Monterrey Correa Ana Daniela',
'Murillo Quijada Ilzedith Alejandra',
'Pan Luo Daniel Jonathan',
'Polo Arosemena Juan Pablo',
'Pul Liu Terry',
'Reyes Vergara Gabriela Lucia',
'Rodriguez Norato Andre Enrique',
'Sarasqueta Castillo Yanina Yarelis',
'Serrano Diana Rosa',
'Valdivieso Da Silva Paulo Cesar',
'Vera Morales Angelice',
'Villarreal Batista Gustavo Shemuel',
'Villarreal Isabella Nicole',
'Young Parbhu Gabriel Alexander',]
print("--------------------------------------------------")
n1 = int(input("Introduzca la cantidad de estudiantes :"))
print("-------------------Resultado----------------------")
for i in range(n1):
    movie = random2.choice(movies_list)
    print(i,"Estudiante...:",movie)