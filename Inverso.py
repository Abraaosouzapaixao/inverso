while True:
    string = input("Digite uma string para ser invertida (ou 'sair' para sair do programa): ")

    if string == "sair":
        break

    string_invertida = ""

    for i in range(len(string)-1, -1, -1):
        string_invertida += string[i]

    print(string_invertida)
