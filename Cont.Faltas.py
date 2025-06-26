

faltas = {}

def adicionar_materia():
    newsubject = input("Digite o nome da matéria: ")
    if newsubject in faltas:
     print("Essa matéria já foi adicionada.")
    else:
     faltas[newsubject] = 0

def add_falta():
    subject = input("Digite o nome da matéria que você deseja adicionar falta: ")
    if subject in faltas:
        numfaltas = int(input("Quantas faltas?: "))
        faltas[subject] += numfaltas
        print(f"Falta adicionada para {subject}. Total de: {faltas[subject]}")
    else: 
        print("Matéria não encontrada.")
    
def mat_removal():
   subject = input("Qual matéria você deseja remover?: ")
   if subject in faltas:
      faltas.pop(subject)
   else:
      print("Matéria não encontrada.")

while True:
    print("\n--- Menu ---")
    print("1 - Adicionar Matéria")
    print("2 - Adicionar falta")
    print("3 - Remover matéria")
    print("4 - Visualizar faltas")
    print("4 - Sair")


    option = int(input("Escolhe uma opção: "))

    if option == 1:
        adicionar_materia()
    elif option == 2:
        add_falta()
    elif option == 3:
       mat_removal()
    elif option == 4:
         for subject, n in faltas.items():
          print(f"{subject}:{n} faltas")
    else:
        print("Saindo...")
        break    


       

    


