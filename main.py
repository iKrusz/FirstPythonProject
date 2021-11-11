'''
projekt będzie polegał na utworzeniu skryptów które szyfrują wpisany tekst przez użytkowanika na kodowanie rot-13
również odszyfrowują

zaszyfrowany tekst możesz zapisywać w pliku txt
i poźniej możesz go odczytać i odszyfrować
jest to jedna z możliwośći
interpretacje pozostawiam już tobie
możesz wykorzystać też klasy
'''

# PSL
from inspect import cleandoc
from typing import NoReturn

# Own
from encryptor import ROT13Encryptor
# from .decryptor import ROT13Decryptor


def show_main_menu() -> NoReturn:
    encryptor = ROT13Encryptor()
    while True:
        print(cleandoc(
            """
            Co chcesz zrobić?
            1. Zaszyfruj frazę
            2. Odszyfruj frazę
            3. Zakończ program
            \nWybierz akcję:
            """
        ))
        available_choices = [encryptor.encrypt_user_text_]
        choice = int(input("> ")) - 1
        if choice < len(available_choices):
            available_choices[choice]()
        else:
            print("Nieprawidłowy wybór!")


if __name__ == "__main__":
    show_main_menu()
