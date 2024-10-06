from dphf import dphfsum
from generate import gen_gibberish

DIV = "###############################"
PASS = "[+]"
FAIL = "[-]"


def test_length(n=100, corr_length=12):
    print("Running length test...")
    res_strings = []
    for _ in range(n):
        string = gen_gibberish(20)
        s = dphfsum(string)
        res_strings += [str(s)]

    corr = 0
    for i in res_strings:
        if len(i) == corr_length:
            corr += 1

    print(f"{corr}/{n} correct length.")
    if corr == n:
        print(f"{PASS} Length test passed.")
    else:
        print(f"{FAIL} Length test failed.")
    print(DIV)


def test_same(n=100):
    print("Running same test...")
    res = []
    for _ in range(n):
        string = gen_gibberish(20)

        sum1 = dphfsum(string)
        sum2 = dphfsum(string)

        if sum1 == sum2:
            res += [1]
        else:
            res += [0]

    corr = 0
    for r in res:
        if r == 1: corr += 1

    print(f"{corr}/{len(res)} correct.")
    if corr == n:
        print(f"{PASS} Same test passed.")
    else:
        print(f"{FAIL} Same test failed.")

    print(DIV)


def test_collision(n=1000):
    sums = []
    for _ in range(n):
        string = gen_gibberish(100)
        sums += [dphfsum(string)]
    sums_set = set(sums)
    unique = len(sums_set)

    print(f"{len(sums_set)}/{n} unique.")
    if unique/n > 0.99:
        print(f"{PASS} Collision test passed.")
    else:
        print(f"{FAIL} Collision test failed.")
    print(DIV)


def test_lorem():
    print("Running lorem ipsum test...")

    lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

    lorem_changed = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum!"

    sum_ipsum = str(dphfsum(lorem_ipsum))
    sum_changed = str(dphfsum(lorem_changed))

    changed = 0
    for i in range(len(sum_ipsum)):
        if sum_ipsum[i] != sum_changed[i]:
            changed += 1

    print(f"{changed}/{len(sum_ipsum)} digits changed.")
    if changed/len(sum_ipsum) > 0.5:
        print(f"{PASS} Lorem ipsum test passed.")
    else:
        print(f"{FAIL} Lorem ipsum test failed.")
    print(DIV)


def test_fox():
    print("Running fox test...")

    fox = "The quick brown fox jumps over the lazy dog"
    fox_changed = "The quick brown fox jumps over the lazy dog."

    sum_fox = str(dphfsum(fox))
    sum_changed = str(dphfsum(fox_changed))

    print(sum_fox)
    print(sum_changed)
    changed = 0
    for i in range(len(sum_fox)):
        if sum_fox[i] != sum_changed[i]:
            changed += 1

    print(f"{changed}/{len(sum_fox)} digits changed.")


if __name__ == "__main__":

    test_length(corr_length=16)
    test_same()
    test_collision(5000)
    test_lorem()
    #test_fox()
