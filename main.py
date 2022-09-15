import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
RESET_BOLD = '\033[0m'
BOLD = '\033[1m'

puntaje = random.randint(0, 10)
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
cadena = "Bienvenido a mi trivia"
print(cadena.center(50, '='))

print(BLUE + "Pondremos a prueba tus conocimientos".center(50, '-') + RESET)

  
#Lista para puntaje totales por cada intento
puntajes_totales = []

while iniciar_trivia == True:
    lista_puntaje = []
    lista_puntaje_adicional=[]

  
    intentos += 1
    puntaje = random.randint(0, 10)
    print("\nIntento número\t", intentos)
    # Instrucciones sobre cómo jugar:
    print("\nComenzarás con: ", puntaje, "\tpuntos" + RESET)
    nombre = input("\n✏️\tIngrese su nombre:\t")
    numero_suerte = input("✏️\tIngrese su nº suerte:\t")
    while not numero_suerte.isnumeric():
        numero_suerte = input("Ingrese un numero valido: ")

    numero_suerte = int(numero_suerte)

    print(
        BLUE + "\n Hola", BOLD + nombre.upper() + RESET_BOLD,
        "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
    )

    print("🎆\tAdemás tu", BLUE+"Nº SUERTE", BOLD+str(numero_suerte)+RESET_BOLD,
          "cambiará tu puntaje.\n"+RESET)

    print(
        "🎆\tSi respondes las 3 preguntas correctamente, recibiras puntos extras.\n"
        + RESET)

    contador_preguntas_correctas = 0
    print(BOLD+"Empezaremos en ...".center(50,' '))
    for numero_carga in range(5, 0, -1):
        print(numero_carga)
        time.sleep(1)
    print(RESET_BOLD)

    alternativas = ['a)','b)','c)','d)']
    
  
    # Pregunta 1
    print(MAGENTA + "\n1) ¿Cuál es la ciudad de los rascacielos?" + RESET)
    alternativas_preguna_1 = ['Barcelona', 'Miami', 'New York', 'Los Angeles']
    for indice in range(0,4):
      print(alternativas[indice]+' '+alternativas_preguna_1[indice])
    respuesta_1 = input(BOLD+"\nTu respuesta: "+RESET_BOLD)

    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_1 == 'c':
        lista_puntaje.append(random.randint(1, 10))
        contador_preguntas_correctas += 1
        print(GREEN + "Muy bien! Sigue así" + RESET)
    else:
        lista_puntaje.append(random.randint(-15,-5))
        print(RED + "Incorrecto!. La respuesta correcta es: c" + RESET)

    print("\n","El puntaje de esta pregunta es: \t", lista_puntaje[0], "puntos")
    print(BLUE + "Respira ...".center(50,"-") + RESET)
    time.sleep(2)



    # Pregunta 2
    print(MAGENTA + "\n2) ¿Qué país del mundo produce más vino?" + RESET)
    alternativas_preguna_2 = ['Chile','Egipto','Austria','Italia']
    for indice in range(0,4):
      print(alternativas[indice]+' '+alternativas_preguna_2[indice])
    respuesta_2 = input(BOLD+"\nTu respuesta: "+RESET_BOLD)

    while respuesta_2 not in ("a", "b", "c", "d", "x"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_2 == 'b':
        lista_puntaje.append(random.randint(-15,-5))
        print(
            RED +
            "Incorrecto!. Egipto tiene como principales productos de exportación el algodón y el arroz.  La respuesta correcta es: d) Italia"
        +RESET)
    elif respuesta_2 == 'c':
        lista_puntaje.append(random.randint(-15,-5))
        print(
            RED +
            "Incorrecto!. Austria exporta principalmente madera.  La respuesta correcta es: d) Italia"
            + RESET)
    elif respuesta_2 == 'a':
        lista_puntaje.append(random.randint(-15,-5))
        print(
            RED +
            "Incorrecto!. Chile exporta principalmente cobre.  La respuesta correcta es: d) Italia"
            + RESET)
    elif respuesta_2 == 'x':
        lista_puntaje.append(100000000)
        print(YELLOW +
              "Descubriste el mensaje secreto! Ganaste: 100000000 puntos" +
              RESET)
    else:
        lista_puntaje.append(random.randint(1, 30))
        contador_preguntas_correctas += 1
        print(
            GREEN +
            "Correcto!. Según la Organización Internacional de la Viña y el Vino (OIV), Italia es el primer productor de vino."
            + RESET)

    print("\n","El puntaje de esta pregunta es: \t", lista_puntaje[1], "puntos")
    print(BLUE + "Respira ...".center(50,"-") + RESET)
    time.sleep(2)

  
    # Pregunta 3
    print(MAGENTA + "\n3) ¿Cuánto es 10-2*3?" + RESET)
    alternativas_preguna_3 = ['4','24','5','10']
    for indice in range(0,4):
      print(alternativas[indice]+' '+alternativas_preguna_3[indice])
    respuesta_3 = input(BOLD+"\nTu respuesta: "+RESET_BOLD)

    while respuesta_3 not in ("a", "b", "c", "d", "x"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta_3 == 'b':
        lista_puntaje.append(random.randint(-10, -5) / 2)
        print(
            RED +
            "Totalmente incorrecto! El operador multiplicación tiene mayor prioridad que el operador resta. La respuesta correcta es: a) 4"
            + RESET)
    elif respuesta_3 == 'c':
      lista_puntaje.append(random.randint(-10, -5) + 5)
      print(YELLOW +
        "Estuviste muy cerca de la respuesta. La respuesta correcta es: a) 4"+RESET
        )
    elif respuesta_3 == 'd':
        lista_puntaje.append(random.randint(-10, -5) - 5)
        print(
            RED +
            "Incorrecto!. Primero se resuelve la multiplicación y luego la resta. La respuesta correcta es: a) 4"
            + RESET)
    elif respuesta_3 == 'x':
        lista_puntaje.append(100000000)
        print(
            YELLOW +
            "Sorpresa, encontraste la alternativa sorpresa, ganaras 100000000"
            + RESET)
    else:
        contador_preguntas_correctas += 1
        lista_puntaje.append(random.randint(1, 5) * 2)
        print(GREEN + "Correcto! Priorizaste correctamente las operaciones." +
              RESET)

    print("\n","El puntaje de esta pregunta es: \t", lista_puntaje[2], "puntos")
    print(BLUE + "Respira ...".center(50,"-") + RESET)
    time.sleep(2)

  #Puntajes
    print(" ")
    print("RESUMEN DE LOS PUNTAJES".center(50,'-'))

    for index, puntaje in enumerate(lista_puntaje):
        print("{:<8} {:<15}".format("✏️ \tPregunta "+str(index+1)+": ", puntaje, " puntos"))
    puntaje_total = sum(lista_puntaje)
    print(("PUNTAJE TOTAL:\t"+str(puntaje_total)).center(50,'='))

    time.sleep(2)

    print(BLUE+"\nEspera, tenemos sorpresas..."+RESET)

    time.sleep(2)

    print("\n🎉\tSorpresa nº 1:\t Tu puntaje se sumara por el puntaje que te de la RULETA")

    numero_aleatorio = 0
    for num_ruleta in range(5, 0, -1):
        numero_aleatorio = random.randint(20, 100)
        print(numero_aleatorio)
        time.sleep(2)

    lista_puntaje_adicional.append(numero_aleatorio)
    puntaje_total+=numero_aleatorio
    print("Tu numero de la ruleta es:", numero_aleatorio)
    print(YELLOW+("Puntaje actual: "+str(puntaje_total)).center(50,'.')+RESET)
    time.sleep(2)

  
    print("\n🎉\tSorpresa nº 2:\t Tu puntaje se multiplica por tu numero de la suerte", numero_suerte)
    lista_puntaje_adicional.append(numero_suerte)
    puntaje_total*=numero_suerte
    print(YELLOW+("Puntaje actual: "+str(puntaje_total)).center(50,'.')+RESET)
    time.sleep(2)

    if (contador_preguntas_correctas == 3):
        print(
            "\n🎉\tSorpresa nº 3: Además respondiste las 3 preguntas correctamente, te regalamos 100 puntos"
        )
        lista_puntaje_adicional.append(100)
        puntaje_total+=100
        print(YELLOW+("Puntaje actual: "+str(puntaje_total)).center(50,'.')+RESET)
    
  
    time.sleep(2)
  
    print(" ")
    print("RESUMEN DE LOS PUNTAJES ADICIONALES".center(50,'-'))

    for index, puntaje in enumerate(lista_puntaje_adicional):
        print("{:<8} {:<15}".format("✏️ \tSorpresa "+str(index+1)+": ", puntaje, " puntos"))
    print(YELLOW+"\nGracias a las sorpresas obtuviste\t ", sum(lista_puntaje_adicional), "puntos extras"+RESET)
    print(" ")
    puntajes_totales.append(puntaje_total)
    print(("PUNTAJE TOTAL:\t"+str(puntaje_total)).center(32,'🌟'))

    print(("Gracias "+ nombre.upper()+ " por jugar mi trivia").center(50,'*'))  


    print(MAGENTA + "\n¿Deseas intentar la trivia nuevamente?" + RESET)
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )

    if repetir_trivia != "si":
        for index, puntaje in enumerate(puntajes_totales):
          print("{:<8} {:<15}".format("✅ \tIntento "+str(index+1)+": ", puntaje, " puntos"))
        print(BLUE + "\nEspero", nombre.upper(),
              "que lo hayas pasado bien, hasta pronto!" + RESET)
        iniciar_trivia = False
