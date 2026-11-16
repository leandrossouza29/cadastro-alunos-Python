
# Classe responsável por armazenar e gerenciar os dados dos alunos.
class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

        # Notas começam vazias (None).
        self.nota1 = None
        self.nota2 = None
        self.recuperacao = None

    # Calcula a média das duas primeiras notas.
    def calcular_media_inicial(self):
        if self.nota1 is None or self.nota2 is None:
            return None

        return (self.nota1 + self.nota2) / 2

    # Calcula a média final, substituindo a menor nota pela recuperação.
    def calcular_media_final(self):
        media = self.calcular_media_inicial()

        if media is None:
            return None

        if self.recuperacao is None:
            return media

        notas = [self.nota1, self.nota2]

        # Localiza e substitui a menor nota.
        menor_indice = notas.index(min(notas))
        notas[menor_indice] = self.recuperacao

        return sum(notas) / 2

    # Determina a situação acadêmica do aluno.
    def verificar_situacao(self):
        media = self.calcular_media_inicial()

        if media is None:
            return "Em andamento"

        if media >= 6:
            return "Aprovado"

        if self.recuperacao is None:
            return "Em andamento"

        if self.calcular_media_final() >= 6:
            return "Aprovado"

        return "Reprovado"


# Armazena os alunos utilizando a matrícula como chave.
alunos = {}


# Recebe um número inteiro e valida a entrada.
def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


# Recebe e valida uma nota entre 0 e 10.
def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem).replace(",", "."))

            if 0 <= nota <= 10:
                return nota

            print("Nota inválida! Digite um valor entre 0 e 10.")

        except ValueError:
            print("Entrada inválida! Digite uma nota válida.")


# Cadastra um novo aluno.
def cadastrar_aluno():
    print("\n===== CADASTRO DE ALUNOS =====")

    nome = input("Nome: ").strip()

    while not nome:
        print("O nome não pode ficar vazio.")
        nome = input("Nome: ").strip()

    idade = ler_inteiro("Idade: ")

    while idade <= 0:
        print("A idade deve ser maior que zero.")
        idade = ler_inteiro("Idade: ")

    matricula = input("Matrícula (8 dígitos): ").strip()

    while not matricula.isdigit() or len(matricula) != 8:
        print("Matrícula inválida! Digite exatamente 8 dígitos.")
        matricula = input("Matrícula (8 dígitos): ").strip()

    if matricula in alunos:
        print("Já existe um aluno cadastrado com essa matrícula.")
        return

    # Cria o objeto e adiciona ao dicionário.
    aluno = Aluno(nome, idade, matricula)
    alunos[matricula] = aluno

    print("\nAluno cadastrado com sucesso!")
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Matrícula: {aluno.matricula}")
    print("Situação do aluno: Em andamento")


# Localiza um aluno pela matrícula e permite lançar notas.
def lancar_notas():
    print("\n===== LANÇAMENTO DE NOTAS =====")

    matricula = input("Digite a matrícula do aluno: ").strip()

    if matricula not in alunos:
        print("Aluno não encontrado!")
        return

    aluno = alunos[matricula]

    print(f"\nAluno selecionado: {aluno.nome}")

    # Exibe as opções de lançamento.
    print("\n1 - Lançar primeira nota")
    print("2 - Lançar segunda nota")
    print("3 - Lançar primeira e segunda notas juntas")

    media = aluno.calcular_media_inicial()

    # A recuperação só aparece quando as duas notas existem
    # e a média inicial é inferior a 6.
    if media is not None and media < 6:
        print("4 - Lançar nota da recuperação")

    opcao = ler_inteiro("\nEscolha uma opção: ")

    match opcao:

        case 1:
            aluno.nota1 = ler_nota("Digite a primeira nota: ")
            aluno.recuperacao = None

            print("Primeira nota registrada com sucesso!")

        case 2:
            aluno.nota2 = ler_nota("Digite a segunda nota: ")
            aluno.recuperacao = None

            print("Segunda nota registrada com sucesso!")

        case 3:
            aluno.nota1 = ler_nota("Digite a primeira nota: ")
            aluno.nota2 = ler_nota("Digite a segunda nota: ")

            aluno.recuperacao = None

            print("\nNotas 1 e 2 registradas com sucesso!")

            print(f"Média inicial: {aluno.calcular_media_inicial():.2f}")

        case 4:
            media = aluno.calcular_media_inicial()

            if media is not None and media < 6:
                aluno.recuperacao = ler_nota("Digite a nota de recuperação: ")

                print("Nota de recuperação registrada com sucesso!")

                print(f"Média final: {aluno.calcular_media_final():.2f}")

            else:
                print("A recuperação não está disponível.")

        case _:
            print("Opção inválida!")


# Consulta os dados e a situação acadêmica do aluno.
def consultar_aluno():
    print("\n===== CONSULTAR ALUNO =====")

    matricula = input("Digite a matrícula do aluno: ").strip()

    if matricula not in alunos:
        print("Aluno não encontrado!")
        return

    aluno = alunos[matricula]

    print("\n===== INFORMAÇÕES DO ALUNO =====")
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
    print(f"Matrícula: {aluno.matricula}")

    print("\n===== NOTAS =====")

    if aluno.nota1 is None:
        print("Primeira nota não lançada")
    else:
        print(f"Primeira nota: {aluno.nota1:.2f}")

    if aluno.nota2 is None:
        print("Segunda nota não lançada")
    else:
        print(f"Segunda nota: {aluno.nota2:.2f}")

    if aluno.recuperacao is None:
        print("Recuperação: Não lançada")
    else:
        print(f"Recuperação: {aluno.recuperacao:.2f}")

    media_inicial = aluno.calcular_media_inicial()

    if media_inicial is not None:
        print(f"\nMédia inicial: {media_inicial:.2f}")

    media_final = aluno.calcular_media_final()

    if media_final is not None:
        print(f"Média final: {media_final:.2f}")

    print(f"Situação: {aluno.verificar_situacao()}")


# Menu principal do sistema.
def menu():
    while True:
        print("\n========== SISTEMA ESCOLAR ==========")
        print("1 - Cadastrar aluno")
        print("2 - Lançar notas")
        print("3 - Consultar situação do aluno")
        print("4 - Sair")

        opcao = ler_inteiro("\nEscolha a opção: ")

        match opcao:

            case 1:
                cadastrar_aluno()

            case 2:
                lancar_notas()

            case 3:
                consultar_aluno()

            case 4:
                print("\nEncerrando o sistema...")
                break

            case _:
                print("Opção inválida! Escolha novamente.")


# Inicia o programa.
menu()