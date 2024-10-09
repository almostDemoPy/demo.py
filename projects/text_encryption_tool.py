# JS2PY - Episode 1 : Text Encryption Tool
# Translation from JS to PY of :
# https://github.com/TanvishGG/Text-Encryption-Tool/tree/main
# JS code by TanvishGG


from base64 import b64encode, b64decode
from random import random
from re import Match, search
from string import ascii_letters, digits

class Encryption:
    def __init__(self, text : str, data : dict[str, str], pattern : str):
        self.__text : str = text
        self.__data : dict[str, str] = data
        self.__pattern : str = pattern

    def __str__(self):
        return self.__data["text"]

    @property
    def text(self) -> str:
        return self.__text

    @property
    def data(self) -> dict:
        return self.__data

    @property
    def pattern(self) -> str:
        return self.__pattern

class Decryption:
    def __init__(self, text : str):
        self.__text = text

    def __str__(self):
        return self.__text

    @property
    def text(self) -> str:
        return self.__text

class EncryptionClient:
    def __init__(self, pattern : str = "^[\x20-\x7E]*$"):
        print("Encrypter Client initiated")
        self.__pattern : str = pattern

    @property
    def pattern(self) -> str:
        return self.__pattern

    @pattern.setter
    def pattern_setter(self, value : str) -> None:
        self.__pattern = value

    def encrypt(self, text : str) -> Encryption:
        text.replace("\n", " ")
        matches : Match = search(self.__pattern, text)
        if matches is None: raise Exception("Provided text contained invalid characters")
        shuffle1 : str = self.shuffle()
        shuffle2 : str = self.shuffle()
        key_map : dict = self.create_key(shuffle1, shuffle2)
        pre_text : str = self.replace(text, key_map)
        key_string, pairs_string = self.generate_key(pre_text, key_map)
        key : str = f"{key_string}@{pairs_string}"
        key_final : str = self.reverse_string(self.encode_to_b64(key))
        final : str = self.reverse_string(self.encode_to_b64(pre_text))
        data : dict = {
            "text": final,
            "key": key_final
        }
        return Encryption(text, data, self.__pattern)

    def decrypt(self, text : str, password : str) -> Decryption:
        text_decoded : str = self.decode_from_b64(self.reverse_string(text))
        key_decoded : str = self.decode_from_b64(self.reverse_string(password))
        key_1, key_2 = key_decoded.split("@")
        map : dict = {char_1: char_2 for char_1, char_2 in zip(list(key_1), list(key_2))}
        return Decryption(self.replace(text_decoded, map))

    def decode_from_b64(self, text : str) -> str:
        return b64decode(text.encode("ascii")).decode("ascii")

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