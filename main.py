import sys
import calc


def main() -> None:
    args = sys.argv
    x: float = 0
    y: float = 0
    if len(args) > 1:
        x = float(args[1])
    if len(args) > 2:
        y = float(args[2])
    print("calc: {} + {} = {}".format(x, y, calc.add_number(x, y)))


if __name__ == "__main__":
    main()
