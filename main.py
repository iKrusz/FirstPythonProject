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
    def __init__(self, input_string_):
        self.input_str = input_string_
        self.encrypted_str = ""
        # rot_dict = {'a': 'n', 'b': 'o', 'c': 'p',
        #             'd': 'q', 'e': 'r', 'f': 's',
        #             'g': 't', 'h': 'u', 'i': 'v',
        #             'j': 'w', 'k': 'x', 'l': 'y',
        #             'm': 'z', 'n': 'a', 'o': 'b',
        #             'p': 'c', 'q': 'd', 'r': 'e',
        #             's': 'f', 't': 'g', 'u': 'h',
        #             'v': 'i', 'w': 'j', 'x': 'k',
        #             'y': 'l', 'z': 'm'}
        rot_dict_pl = {'a': 'k', 'ą': 'l', 'b': 'ł',
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

        for letter in self.input_str:
            if letter.islower():
                self.encrypted_str += rot_dict_pl.get(letter)
            if letter.isupper():
                 letter = letter.lower()
                 self.encrypted_str += rot_dict_pl.get(letter).capitalize()
            if letter not in rot_dict_pl:
                self.encrypted_str += letter

        with open("encrypted.txt", "a", encoding="utf-8") as file:
            file.writelines(f"{self.encrypted_str}\n")

Encryptor("Siemanko")
Encryptor("tutaj")
Encryptor("program")
Encryptor("szyfrujący")

