s = str(input("Digite uma palavra: "))
tam = len(s)

def right_justify(s):
    palavra = " " * (70 - tam) + (s)
    print(palavra)

right_justify(s)
