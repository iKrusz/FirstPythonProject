'''
projekt będzie polegał na utworzeniu skryptów które szyfrują wpisany tekst przez użytkowanika na kodowanie rot-13
również odszyfrowują

zaszyfrowany tekst możesz zapisywać w pliku txt
i poźniej możesz go odczytać i odszyfrować
jest to jedna z możliwośći
interpretacje pozostawiam już tobie
możesz wykorzystać też klasy
'''



class Encryptor:
    def __init__(self):
        # rot_dict = {'a': 'n', 'b': 'o', 'c': 'p',
        #             'd': 'q', 'e': 'r', 'f': 's',
        #             'g': 't', 'h': 'u', 'i': 'v',
        #             'j': 'w', 'k': 'x', 'l': 'y',
        #             'm': 'z', 'n': 'a', 'o': 'b',
        #             'p': 'c', 'q': 'd', 'r': 'e',
        #             's': 'f', 't': 'g', 'u': 'h',
        #             'v': 'i', 'w': 'j', 'x': 'k',
        #             'y': 'l', 'z': 'm'}
        self.rot_dict_pl = {'a': 'k', 'ą': 'l', 'b': 'ł',
                       'c': 'm', 'ć': 'n', 'd': 'ń',
                       'e': 'o', 'ę': 'ó', 'f': 'p',
                       'g': 'q', 'h': 'r', 'i': 's',
                       'j': 'ś', 'k': 't', 'l': 'u',
                       'ł': 'v', 'm': 'w', 'n': 'x',
                       'ń': 'y', 'o': 'z', 'ó': 'ź',
                       'p': 'ż', 'q': 'a', 'r': 'ą',
                       's': 'b', 'ś': 'c', 't': 'ć',
                       'u': 'd', 'v': 'e', 'w': 'ę',
                       'x': 'f', 'y': 'g', 'z': 'h',
                       'ź': 'i', 'ż': 'j'}

    def encypt_and_save(self, input_string_):
        self.input_str = input_string_
        self.encrypted_str = ""
        for letter in self.input_str:
            if letter.islower():
                self.encrypted_str += self.rot_dict_pl.get(letter)
            if letter.isupper():
                 letter = letter.lower()
                 self.encrypted_str += self.rot_dict_pl.get(letter).capitalize()
            if letter not in self.rot_dict_pl:
                self.encrypted_str += letter

        with open("encrypted.txt", "a", encoding="utf-8") as file:
            file.writelines(f"{self.encrypted_str}\n")
        print("Zaszyfrowana fraza została zapisana w pliku")

    def read_and_decrypt(self, line_nr):
        with open("encrypted.txt", "r", encoding="utf-8") as file:
            self.out_line = []
            self.lines = file.readlines()
            for line in self.lines:
                self.out_line.append(line.rstrip())

        inv_dict = {v: k for k, v in self.rot_dict_pl.items()}
        self.decrypted_str = ""
        for letter in self.out_line[line_nr]:
            if letter.islower():
                self.decrypted_str += inv_dict.get(letter)
            if letter.isupper():
                letter = letter.lower()
                self.decrypted_str += inv_dict.get(letter).capitalize()
            if letter not in inv_dict:
                self.decrypted_str += letter
        print(self.decrypted_str)

def menu():
    print("\n\nCo chcesz zrobić? \n")
    print("1. Zaszyfruj frazę")
    print("2. Odszyfruj frazę")
    print("3. Zakończ program")
    choice = input("\nWybierz akcję: ")
    encryptor = Encryptor()
    if choice == "1":
        encryptor.encypt_and_save(input("Wprowadź frazę do zaszyfrowania: "))
    elif choice == "2":
        encryptor.read_and_decrypt(int(input("Którą linię chcesz odczytać? ")))
    elif choice == "3":
        exit()
    else:
        print("Nieprawidłowy wybór!")

def main():
    menu()

if __name__ == "__main__":
    while True:
        main()