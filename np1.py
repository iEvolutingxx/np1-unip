def exibir_mensagem():
    print("\nExplicação sobre o comando print():")
    print("O comando print() é utilizado para exibir mensagens na tela do usuário.")
    print("Exemplo:")
    print('print("Olá, Mundo!")')
    print("Este comando exibe a mensagem 'Olá, Mundo!' na tela.")
    input("\nPressione Enter para voltar ao menu.")

def receber_dados():
    print("\nExplicação sobre o comando input():")
    print("O comando input() é utilizado para receber dados do usuário.")
    print("Exemplo:")
    print('nome = input("Qual é o seu nome? ")')
    print("Este comando solicita que o usuário digite seu nome, e armazena a resposta na variável 'nome'.")
    input("\nPressione Enter para voltar ao menu.")

def quiz():
    print("\nQuiz - Teste seus conhecimentos!")

    perguntas = [
        {
            'pergunta': 'O que o comando print() faz?',
            'respostas': [
                "Exibe uma mensagem na tela",
                "Cria um arquivo de texto",
                "Recebe dados do usuário",
                "Define variáveis"
            ],
            'resposta_correta': 0
        },
        {
            'pergunta': 'Qual comando é usado para receber dados do usuário?',
            'respostas': [
                "print()",
                "input()",
                "open()",
                "write()"
            ],
            'resposta_correta': 1
        },
        {
            'pergunta': 'Quem é o criador da linguagem Python?',
            'respostas': [
                "Guido van Rossum",
                "Dennis Ritchie",
                "Bjarne Stroustrup",
                "James Gosling"
            ],
            'resposta_correta': 0
        },
        {
            'pergunta': 'Em que ano a linguagem Python foi criada?',
            'respostas': [
                "1985",
                "1991",
                "2000",
                "1995"
            ],
            'resposta_correta': 1
        },
        {
            'pergunta': 'De onde vem o nome "Python"?',
            'respostas': [
                "De uma cobra",
                "De um monstro mitológico",
                "De um livro de ficção científica",
                "De um grupo de programadores"
            ],
            'resposta_correta': 2
        }
    ]

    pontuacao = 0

    for pergunta in perguntas:
        print("\n" + pergunta['pergunta'])
        for i, resposta in enumerate(pergunta['respostas']):
            print(f"{i+1}. {resposta}")

        try:
            resposta_usuario = int(input("Escolha uma opção (1-4): ")) - 1
            if resposta_usuario == pergunta['resposta_correta']:
                print("Resposta correta!")
                pontuacao += 1
            else:
                print("Resposta errada.")
        except ValueError:
            print("Por favor, digite um número de 1 a 4.")

    print(f"\nVocê acertou {pontuacao} de {len(perguntas)} perguntas.")
    input("\nPressione Enter para voltar ao menu principal.")

def menu_principal():
    while True:
        print("\nMenu Principal:")
        print("(1) Aprender")
        print("(2) Fazer um Quiz")
        print("(3) Sair")
        opcao = input("Escolha uma opção (1-3): ")

        if opcao == '1':
            menu_aprender()
        elif opcao == '2':
            quiz()
        elif opcao == '3':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_aprender():
    while True:
        print("\nModo Aprender:")
        print("(1) Como exibir mensagens na tela?")
        print("(2) Como receber dados do usuário?")
        print("(3) Voltar ao menu principal")
        opcao = input("Escolha uma opção (1-3): ")

        if opcao == '1':
            exibir_mensagem()
            fazer_quiz = input("Você deseja fazer um quiz sobre esse tema? (s/n): ")
            if fazer_quiz.lower() == 's':
                quiz()
            else:
                continue
        elif opcao == '2':
            receber_dados()
            fazer_quiz = input("Você deseja fazer um quiz sobre esse tema? (s/n): ")
            if fazer_quiz.lower() == 's':
                quiz()
            else:
                continue
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
