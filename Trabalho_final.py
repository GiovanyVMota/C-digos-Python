#Primeiro vamos fazer as letras maiúsculas e minúsculas as convertendo em símbolos

letras_para_simbolos = {
    'a': '@', 'b': '!', 'c': '#', 'd': '$', 'e': '%', 'f': '^',
    'g': '&', 'h': '*', 'i': '(', 'j': ')', 'k': '-', 'l': '+',
    'm': '=', 'n': '{', 'o': '}', 'p': '[', 'q': ']', 'r': ':',
    's': ';', 't': '"', 'u': '<', 'v': '>', 'w': '?', 'x': '/',
    'y': '~', 'z': '`',
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6',
    'G': '7', 'H': '8', 'I': '9', 'J': '0', 'K': 'q', 'L': 'w',
    'M': 'e', 'N': 'r', 'O': 't', 'P': 'y', 'Q': 'u', 'R': 'i',
    'S': 'o', 'T': 'p', 'U': 's', 'V': 'd', 'W': 'f', 'X': 'g',
    'Y': 'h', 'Z': 'j'
}

#Criptografia simples alterando os caracteres 
def cripto(frase):
    tradutor = ''
    for letra in frase:
        if letra in letras_para_simbolos:
            tradutor += letras_para_simbolos[letra]  # Substitui pela letra correspondente
        else:
            tradutor += letra  # Mantém caracteres não alfabéticos
    return tradutor


def descripto(frase):
    simbolos_para_letras = {v: k for k, v in letras_para_simbolos.items()}  # Inverte o dicionário
    tradutor = ''
    for letra in frase:
        if letra in simbolos_para_letras:
            tradutor += simbolos_para_letras[letra]  # Substitui pelo caractere correspondente
        else:
            tradutor += letra  # Mantém caracteres não alfabéticos
    return tradutor

#Função da criptografia de Cesar
def cripto_cesar(frase):
    tradutor = ''
    for i in range(0, len(frase)):
        tradutor+= chr(ord(frase[i])+2)
    return tradutor

#Função para ser feita a descriptografia 
def descripto_cesar(frase):
    tradutor = ''
    for i in range(0, len(frase)):
        tradutor+= chr(ord(frase[i])-2)
    return tradutor

# Função para criptografar conteúdo de um arquivo e salvar em outro
def criptografar_arquivo(entrada, saida):
    with open(entrada, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()  # Lê o conteúdo do arquivo
    conteudo_criptografado = cripto(conteudo)  # Criptografa o conteúdo
    with open(saida, 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.write(conteudo_criptografado)  # Salva o conteúdo criptografado

# Função para descriptografar conteúdo de um arquivo e exibir na tela
def descriptografar_arquivo(entrada):
    with open(entrada, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()  # Lê o conteúdo do arquivo
    conteudo_descriptografado = descripto(conteudo)  # Descriptografa o conteúdo
    print(conteudo_descriptografado)  # Exibe o resultado na tela

print("Olá, seja bem vindo ao meu código")

while(True):
    print("\n 1- Criptografia Simples \n 2- Descriptografia simples \n 3- Criptografia de Cesar \n 4-Descriptografia de Cesar \n 5-Criptografar Arquivo \n 6- Descriptografar Arquivo \n 7- Encerrar o programa")
    opcao = input('Qual funcão você deseja realizar? ')

    match(opcao):
        case '1':
            frase = input("Digite a frase quer você quer criptografar: ")
            print('Essa é sua mensagem criptografada: ', cripto(frase))
        case '2':
            frase = input("Digite a frase que você quer descriptografar: ")
            print('Essa é sua mensagem descriptografada: ',descripto(frase))
        case '3':
            frase = input("Digite a frase quer você quer criptografar: ")
            print('Essa é sua mensagem criptografada: ',cripto_cesar(frase))
        case '4':
            frase = input("Digite a frase que você quer descriptografar: ")
            print('Essa é sua mensagem descriptografada: ' ,descripto_cesar(frase))
        case '5': 
            entrada = input("Digite o nome do arquivo de entrada: ")
            saida = input("Digite o nome do arquivo de saída: ")
            criptografar_arquivo(entrada, saida)
        case '6':
            entrada = input("Digite o nome do arquivo que você quer descriptografar: ")
            descriptografar_arquivo(entrada)
        case '7':
            print("Olá, estou encerrando o seu programa!")
            break
        case _:
            print("Digite uma opção válida")


