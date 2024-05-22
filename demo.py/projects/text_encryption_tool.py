# Translation from JS to PY from :
# https://github.com/TanvishGG/Text-Encryption-Tool/tree/main
# by Tanvish


from base64 import b64encode, b64decode
from random import random
from re import Match, search
from string import ascii_letters, digits

class EncrypterClient:
    def __init__(self):
        print("Encrypter Client initiated")
        self.pattern : str = "^[\x20-\x7E]*$"

    def encrypt(self, text : str) -> dict[str, str]:
        text.replace("\n", " ")
        matches : Match = search(self.pattern, text)
        if matches is None: raise Exception("Provided text contained invalid characters")
        shuffle1 : str = self.shuffle()
        shuffle2 : str = self.shuffle()
        key_map : dict = self.create_key(shuffle1, shuffle2)
        pre_text : str = self.replace(text, key_map)
        key_string, pairs_string = self.generate_key(pre_text, key_map)
        key : str = f"{key_string}@{pairs_string}"
        key_final : str = self.reverse_string(self.encode_to_b64(key))
        final : str = self.reverse_string(self.encode_to_b64(pre_text))
        return {
            "text": final,
            "key": key_final
        }

    def shuffle(self) -> str:
        characters : str = ascii_letters + digits
        index : int = len(characters) - 1
        while index > 0:
            j : int = int(random() * (index + 1))
            characters.maketrans(f"{characters[index]}{characters[j]}", f"{characters[j]}{characters[index]}")
            index -= 1
        return characters

    def create_key(self, keys : str, values : str) -> dict[str, str]:
        result : dict = {}
        for index, _ in enumerate(keys):
            result[keys[index]] = values[len(values) - index - 1]
        return result
    
    def replace(self, text : str, map : dict) -> str:
        result : str = ""
        i : int = 0
        while i < len(text):
            character : str = text[i]
            result += map[character] if character in map else character
            i += 1
        return result
    
    def generate_key(self, pre_text : str, map : dict) -> tuple[str]:
        key_string : str = ""
        pairs_string : str = ""
        for key in map:
            if (key in map) and (key in pre_text):
                key_string += key
                pairs_string += map[key]
        return (key_string, pairs_string)

    def encode_to_b64(self, text : str) -> str:
        return b64encode(text.encode("ascii")).decode("ascii")

    def reverse_string(self, text : str) -> str:
        return "".join(text[::-1])

encrypter : EncrypterClient = EncrypterClient()
encrypted : str = encrypter.encrypt("demo")
print(encrypted)