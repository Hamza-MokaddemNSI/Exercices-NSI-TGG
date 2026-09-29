class CodeCesar:
    def __init__(self,cle):
        self.cle =cle
        self.alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def decale(self,lettre):
        num1 = self.alphabet.find(lettre)
        num2 = num1+self.cle
        if num2 >= 26:
            num2 =num2-26
        if num2 < 0:
            num2 = num2+26
        nouvelle_lettre = self.alphabet[num2]
        return nouvelle_lettre

    def cryptage(self,texte):
        output=""
        for lettre in texte:
            output+= self.decale(lettre)
        return output

    def transforme(self,texte):
        self.cle = -self.cle
        message = self.cryptage(texte)
        self.cle = -self.cle
        return message

    
code1 = CodeCesar(3)
print(code1.decale('A'))
print(code1.decale('X'))
code1.cryptage("NSI")

def main():
    key_input = int(input("Entrer votre cle: "))
    code = CodeCesar(key_input)
    str_input = str(input("Entrer votre texte: "))
    print(f"Votre texte cryptee est: {code.cryptage(str_input)}")


print(CodeCesar(10).transforme("PSX"))
main()

