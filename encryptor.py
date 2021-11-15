# PSL
from typing import Dict, NoReturn, Union
import string


#       # int(input("Którą linię chcesz odczytać? "))


class ROT13Encryptor:

    def encrypt_user_text_(self, tests=False) -> Union[str, NoReturn]:
        self.encrypted_str: str = ""
        user_text_to_encrypt: str = str(input("Wprowadź frazę do zaszyfrowania: "))
        for character in user_text_to_encrypt:
            if character.isupper():
                character = character.lower()
                if ord(character) in range(ord("a"), ord("z") + 1):
                    if ord(character) + 13 > ord("z"):
                        self.encrypted_str += chr(ord("a") + (13 - (ord("z") + 1 - ord(character)))).upper()
                    else:
                        self.encrypted_str += chr(ord(character) + 13).upper()
                else:
                    self.encrypted_str += character.upper()
            else:
                if ord(character) in range(ord("a"), ord("z") + 1):
                    if ord(character) + 13 > ord("z"):
                        self.encrypted_str += chr(ord("a") + (13 - (ord("z") + 1 - ord(character))))
                    else:
                        self.encrypted_str += chr(ord(character) + 13)
                else:
                    self.encrypted_str += character
        if tests:
            return self.encrypted_str
        if self.encrypted_str == user_text_to_encrypt:
            print("Fraza nie została zaszyfrowana!")
        else:
            print(self.save_encrypted_text())

    def save_encrypted_text(self) -> str:
        with open("encrypted.txt", "a", encoding="utf-8") as file:
            file.writelines(f"{self.encrypted_str}\n")
        return "Zaszyfrowana fraza została zapisana w pliku"
