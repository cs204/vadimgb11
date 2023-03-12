def main():
    s = input("Верблюжий стиль: ")
    print(convert(s))

def convert(s):
    s2 = ""
    for c in s:
        if c.isupper():
            s2 = s2 + "_" + c.upper()
        else:
            s2 = s2 + c
    return s2

main()