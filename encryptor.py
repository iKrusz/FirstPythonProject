# PSL
from typing import Dict, NoReturn, Union


#       # int(input("Którą linię chcesz odczytać? "))


class ROT13Encryptor:
    def __init__(self):
        self.encrypted_str: str = ""

    def encrypt_user_text_(self, tests=False) -> Union[str, NoReturn]:
        user_text_to_encrpt: str = str(input("Wprowadź frazę do zaszyfrowania: "))
        for character in user_text_to_encrpt:
            if ord(character) <= 109:
                self.encrypted_str += chr(ord(character) + 13)
            else:
                self.encrypted_str += chr(ord(character))
        if tests:
            return self.encrypted_str
        print(self.save_encrypted_text())

    def save_encrypted_text(self) -> str:
        with open("encrypted.txt", "a", encoding="utf-8") as file:
            file.writelines(f"{self.encrypted_str}\n")
        return "Zaszyfrowana fraza została zapisana w pliku"
