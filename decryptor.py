class ROT13Decryptor:
    def read_line_from_file_(self, line_nr) -> str:
        with open("encrypted.txt", "r", encoding="utf-8") as file:
            self.read_output = []
            for line in file.readlines():
                self.read_output.append(line.rstrip())
        return self.read_output[line_nr]

    def decrypt_line_from_file_(self) -> str:
        chosen_line: int = int(input("Którą linię pliku chcesz odczytać?\n>>> "))
        line_to_decrypt: int = self.read_line_from_file_(chosen_line)
        decrypted_str: str = ""
        for character in line_to_decrypt:
            if character.isupper():
                character = character.lower()
                if ord(character) in range(ord("a"), ord("z") + 1):
                    if ord(character) - 13 < ord("a"):
                        decrypted_str += chr(ord("z") + 1 - (13 - (ord(character) - ord("a")))).upper()
                    else:
                        decrypted_str += chr(ord(character) - 13).upper()
                else:
                    decrypted_str += character.upper()
            else: #Wiem, że jest powtórzenie, ale nie mam pomysłu jak je wyeliminować.
                if ord(character) in range(ord("a"), ord("z") + 1):
                    if ord(character) - 13 < ord("a"):
                        decrypted_str += chr(ord("z") + 1 - (13 - (ord(character) - ord("a"))))
                    else:
                        decrypted_str += chr(ord(character) - 13)
                else:
                    decrypted_str += character
        return print(decrypted_str)





# def read_and_decrypt(self, line_nr):
#     with open("encrypted.txt", "r", encoding="utf-8") as file:
#         self.out_line = []
#         self.lines = file.readlines()
#         for line in self.lines:
#             self.out_line.append(line.rstrip())
#
#     inv_dict = {v: k for k, v in self.rot_dict_pl.items()}
#     self.decrypted_str = ""
#     for letter in self.out_line[line_nr]:
#         if letter.islower():
#             self.decrypted_str += inv_dict.get(letter)
#         if letter.isupper():
#             letter = letter.lower()
#             self.decrypted_str += inv_dict.get(letter).capitalize()
#         if letter not in inv_dict:
#             self.decrypted_str += letter
#     print(self.decrypted_str)
