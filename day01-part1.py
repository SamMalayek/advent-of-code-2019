
def main():
    masses = open('day01.txt').read().splitlines()

    resp = 0

    for mass in masses:
        resp += int(mass) // 3 - 2

    print(resp)


if __name__ == "__main__":
    main()
