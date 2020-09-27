#proyecto: quiz
#autor: ricardo nistch - meliza asucena ajtzij escobar 
#carnet: 1618720 - 1640220
#este programa sera para ver que personaje eres de disney
marcador = 0
from time import sleep
from screen import clear
from random import randint
print("hola hoy veremos  que personaje eres de disney al responder estas preguntas")
sleep(7)
clear()

usuario = input("ingresa tu nombre: ")
usuario = str(usuario)
sleep(1)
clear()

#muestro las opciones al usuario
genero = input("preciona ENTER para ingresa tu genero:")
print("""
1. masculino
2. femenino
""")
eleccion_usuario = input("selecciona el numero: ")
eleccion_usuario = str(eleccion_usuario)
sleep(1)
clear()

nacionalidad = input("¿De que pais eres?: ")
nacionalidad = str(nacionalidad)
sleep(1)
clear()

inicio = input("suerte empezaremos con el Quizz")
sleep(1)
clear()

inicio = str("preciona enter para comenzar")
sleep(4)
clear()

pregunta_1 = input("¿cual de los siguientes no es uno de los 7 enanitos de blanca nieves?")
print("""
1. gruñon
2. enamorado
3. tontin
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("incorrecto sacaste 0")
elif eleccion_usuario == 2:
    print("correcto ganaste 5 puntos")
    marcador += 5
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

pregunta_2 = input("¿que color de piel tenia pocahontas?")
print("""
1. morena
2. amarilla
3. blanca
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("correcto ganaste 5 puntos")
    marcador += 5
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_3 = input("¿que animla era cri-keen en mulan?")
print("""
1. dragon
2. grillo
3. perro
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("incorecto sacaste 0")
elif eleccion_usuario == 2:
    print("correcto ganaste 5 puntos")
    marcador += 5
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_4 = input("¿como se llama el hermano de Remy en ratatouille?")
print("""
1. erick
2. ellie
3. emile
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("incorecto sacaste 0")
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("correcto ganaste 5 puntos")
    marcador += 5
sleep(2)
clear()

regunta_5 = input("¿a cuantos perritos da a luz en la pelicula de dalmatas?")
print("""
1. 101
2. 100
3. 200
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("correcto ganaste 5 puntos")
    marcador += 5
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("incorecto sacaste 0")
sleep(2)
clear()


regunta_6 = input("¿que nombre de las princesas significa mar?")
print("""
1. ariel
2. mohana
3. sirenita
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("incorecto sacaste 0")
elif eleccion_usuario == 2:
    print("correcto ganaste 5 puntos")
    marcador += 5
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_7 = input("¿como se llama el reino de frozen?")
print("""
1. andalacia
2. friolandia
3. arendelle
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("incorecto sacaste 0")
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("correcto ganaste 5 puntos")
    marcador += 5
sleep(2)
clear()

regunta_8 = input("¿de que material estaba hecho pinocho?")
print("""
1. madera
2. metal
3. algodon
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("correcto ganaste 5 puntos")
    marcador += 5
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_9 = input("¿que fruta enveneno a blancanieves?")
print("""
1. manzana
2. pera
3. uva
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("correcto ganaste 5 puntos")
    marcador += 5
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_10 = input("¿de que color es el rayo Mc-Queen?")
print("""
1. verde
2. rojo
3. asul
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("incorecto sacaste 0")
elif eleccion_usuario == 2:
    print("correcto ganaste 5 puntos")
    marcador += 5
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_11 = input("¿como se llama la deseñadora de moda de los increibles?")
print("""
1. Elena moda
2. Edna moda
3. Ela moda
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("incorecto sacaste 0")
elif eleccion_usuario == 2:
    print("correcto ganaste 5 puntos")
    marcador += 5
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_12 = input("¿de que color es el cabello de la princesa Merida en valiente?")
print("""
1. rojizo
2. dorado
3. negro
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("correcto ganaste 5 puntos")
    marcador += 5
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_13 = input("¿que tipo de pez es nemo?")
print("""
1. payaso
2. espada
3. globo
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("correcto ganaste 5 puntos")
    marcador += 5
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_14 = input("¿cual es el tema de los tiburones vejetarianos de buscando a nemo?")
print("""
1. comeremos algas sin parar
2. nadaremos nadaremos en el mar
3. los peses son amigos no comida
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("incorecto sacaste 0")
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("correcto ganaste 5 puntos")
    marcador += 5
sleep(2)
clear()

regunta_15 = input("¿cuantas emociones existen en intensamente ?")
print("""
1. 6
2. 5
3. 8
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("correcto ganaste 5 puntos")
    marcador += 5
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_16 = input("¿como se llama la amiga de sulliban en mosnter inc.?")
print("""
1. boo
2. blu
3. bou
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("correcto ganaste 5 puntos")
    marcador += 5
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_17 = input("¿que animal es el mejor amigo de Wall-e?")
print("""
1. planta
2. cucaracha
3. mosquito
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("incorecto sacaste 0")
elif eleccion_usuario == 2:
    print("correcto ganaste 5 puntos")
    marcador += 5
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_18 = input("¿como se llama el perro de Migue en la pelicula coco?")
print("""
1. Ernesto
2. Dante
3. Coco
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("incorecto sacaste 0")
elif eleccion_usuario == 2:
    print("correcto ganaste 5 puntos")
    marcador += 5
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_19 = input("¿que animal es Mickey y Minnie Mouse?")
print("""
1. ratones
2. perros
3. osos
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("correcto ganaste 5 puntos")
    marcador += 5
elif eleccion_usuario == 2:
    print("isncorecto sacaste 0")
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

regunta_20 = input("¿cual de las princesas tenia metros de largo de cabellera?")
print("""
1. Rapunzel
2. Cenicienta
3. Valiente
""")
elecion_usuario = input("elige una: ")
elecion_usuario = int(elecion_usuario)

if elecion_usuario == 1:
    print("correcto ganaste 5 puntos")
    marcador += 5
elif eleccion_usuario == 2:
    print("incorecto sacaste 0")
else:
    print("incorecto sacaste 0")
sleep(2)
clear()

fin = input("genial has terminado este Quizz")
sleep(1)
clear()
fin = input("preciona enter para ver tus resultados")
print("felicidades lo has logrado este es tu punteo", marcador, "puntaje", "exelente bro")
