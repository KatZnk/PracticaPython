leaderboard = {}

while True:
    menu = """ 

        1. Agregar equipo al torneo
        2. Registrar resultado
        3. Ver tabla de posiciones
        4. Eliminar equipo del torneo
        5. Salir
    
    """
    option = input(f"\nHola! Por favor, elija una opción del menú: {menu}")
    print()
    match option:
        case "1":
            name = input("Ingrese el nombre del equipo: ").strip().title() #las palabras ingresadas con errores de tipeo se formalizan.
            if name in leaderboard:
                print(f"El equipo {name} ya se encuentra en el torneo.\n")
                continue
            else:
                leaderboard[name] = 0
                print(f"Se agregó el equipo {name} al torneo!\n")

        case "2":
            local = input("Ingrese el nombre del equipo local: ").strip().title()
            visitante = input ("Ingrese el nombre del equipo visitante: ").strip().title()
            if visitante not in leaderboard or local not in leaderboard:
                print(f"Uno de los equipos no se encuentra en el torneo\n")
                continue

            scorer = (input("Ingrese el marcador final (ej: 2-1), local primero: "))
            
            if '-' not in scorer:
                print("Formato inválido\n")
                continue
            
            goals = scorer.split('-')
            goals_l = goals[0].strip()
            goals_v = goals[1].strip()

            # con .isdigit() verifico que es un número.
            if goals_l.isdigit() and goals_v.isdigit():
                local_goals = int(goals_l)
                visitante_goals = int(goals_v)
            else: 
                print("Error, no se ingresó un número. \n")
                continue

            if local_goals > visitante_goals:
                leaderboard[local] += 3
            elif local_goals < visitante_goals:
                leaderboard[visitante] += 3
            else:
                leaderboard[local] += 1
                leaderboard[visitante] += 1
        case "3": 
            if not leaderboard:
               print("Aún no hay equipos.")
               continue

            #sorted itera sobre el diccionario armando una lista, con key = lambda indico sobre cual elemento debo ordenar.
            #con reverse indico si quiero que sea de menor a mayor o vicever1sa. (tengo que consultar si esto lo podemos implementar)
            leaderboard_org = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
            print(f"{'EQUIPO':<15} | {'PUNTOS':^6} |")
            print("-" * 28)

            for equipo, puntos in leaderboard_org:
                print(f"{equipo:<15} | {puntos:^6} |")
            print("=" * 28)

        case "4":
            name = input("Ingrese el equipo a eliminar: ").strip().title()
            if name not in leaderboard:
                print(f"El equipo {name} no se encuentra en el torneo.\n")
                continue
            del leaderboard[name]
            print(f"Se eliminó al equipo {name} del torneo.\n")

        case "5": 
            print("Hasta luego!")
            break 
