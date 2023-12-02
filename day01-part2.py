
def main():
    masses = open('day01.txt').read().splitlines()

    resp = 0

    def calcFuel(mass):
        cur = mass // 3 - 2
        if cur > 0:
            cur += calcFuel(cur)
        return max(cur, 0)

    for mass in masses:
        resp += calcFuel(int(mass))

    print(resp)


if __name__ == "__main__":
    main()
