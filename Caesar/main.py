import string
from typing import Generator, Tuple


def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    print(len(string.ascii_uppercase))
    len_alphabet = ord('Z') - ord('A') + 1
    print(len_alphabet)
    for char in text:
        if char.isupper():
            alphabet = string.ascii_uppercase
        elif char.islower():
            alphabet = string.ascii_lowercase
        else:
            result += char
            continue

        index = (alphabet.index(char) + shift) % len_alphabet
        result += alphabet[index]
    return result


def caesar_cipher_hack(text: str) -> Generator[Tuple[int, str], None, None]:
    len_alphabet = len(string.ascii_uppercase)
    len_alphabet = ord('Z') - ord('A') + 1
    for candidate_shift in range(1, len_alphabet+1):
        reverted = ''
        for char in text:
            if char.isupper():
                index = ord(char) - candidate_shift
                if index < ord('A'):
                    index += len_alphabet
                reverted += chr(index)
            elif char.islower():
                index = ord(char) - candidate_shift
                if index < ord('a'):
                    index += len_alphabet
                reverted += chr(index)
            else:
                reverted += char

        yield candidate_shift, reverted


if __name__ == '__main__':
    s = -3
    encrypted = caesar_cipher("HOW TO BECOME A PROGRAMER", s)
    print(encrypted)
    print(caesar_cipher(encrypted, -s))
    for shift_num, decrypted in caesar_cipher_hack(encrypted):
        print(f'{shift_num:2d}', decrypted)