from caesar_art import logo
import os

def keep_going(): 
    print(logo)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction != "encode" and direction != "decode":
        direction = input("Invalid answer.\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:   
        shift = shift % 26 # aqui dividir o valor de shift ate que haja um resto, para debug de valores muito altos

    def cipher(plain_text, shift_amount, cipher_direction):
        cipher_txt = ""
        if cipher_direction == "decode": # multiplicar por -1 pra transformar o valor em negativo
            shift_amount = shift_amount * -1
        for l in plain_text:
            if l in alphabet: 
                position = alphabet.index(l)  # pegar a posicao que o item esta na lista
                new_position = position + shift_amount # mudar a posicao do item de acordo com a variavel shift
                cipher_txt += alphabet[new_position] # adicionar o l ja na posicao nova na string desejada, cipher_txt
            else:
                cipher_txt += l  # caso nao esteja na lista do alfabeto simplismente adicionar a nossa string, cipher_txt

        print(f"Your {direction} text is {cipher_txt}.")
        X = input("Run again? Y/N:\n").lower()
        if X == "y":
            os.system('cls')
            keep_going()
        if X == "n":
            os.system('cls')
            print(logo)
            print("Thank you for using Caesar Cipher")
    cipher(plain_text=text, shift_amount=shift, cipher_direction= direction)

keep_going()


 

