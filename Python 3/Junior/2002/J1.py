num = int(input())
digits = {
    0: [" * * *", "*     *", "*     *", "*     *", "", "*     *", "*     *", "*     *", " * * *"],
    1: ["", "      *", "      *", "      *", "", "      *", "      *", "      *", ""],
    2: [" * * *", "      *", "      *", "      *", " * * *", "*", "*", "*", " * * *"],
    3: [" * * *", "      *", "      *", "      *", " * * *", "      *", "      *", "      *", " * * *"],
    4: ["", "*     *", "*     *", "*     *", " * * *", "      *", "      *", "      *", ""],
    5: [" * * *", "*", "*", "*", " * * *", "      *", "      *", "      *", " * * *"],
    6: [" * * *", "*", "*", "*", " * * *", "*     *", "*     *", "*     *", " * * *"],
    7: [" * * *", "      *", "      *", "      *", "", "      *", "      *", "      *", ""],
    8: [" * * *", "*     *", "*     *", "*     *", " * * *", "*     *", "*     *", "*     *", " * * *"],
    9: [" * * *", "*     *", "*     *", "*     *", " * * *", "      *", "      *", "      *", " * * *"]
}
for line in digits.get(num, []): print(line.rstrip())