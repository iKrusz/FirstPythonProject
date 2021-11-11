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
