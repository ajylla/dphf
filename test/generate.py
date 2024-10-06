from random import randint


def gen_gibberish(length):
    string = ""
    for _ in range(length):
        string += chr(randint(33, 126))

    return string


if __name__ == "__main__":
    n = 1000
    string_length = 20

    for _ in range(n):
        for _ in range(string_length):
            print(chr(randint(33, 126)), end="")
        print("")
