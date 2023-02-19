def main():
    s = input()
    s = convert(s)
    print(s)

def convert(s):
    s = s.replace(':)', '\N{Slightly Smiling Face}').replace(':(', '\N{Slightly Frowning Face}')
    return s


main()
