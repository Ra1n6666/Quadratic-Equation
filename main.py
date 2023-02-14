import math


def is_prime(number):
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            return False
    else:
        return True


def root(value) -> int:
    try:
        if is_prime(value):
            raise Exception("There are no results.")

        i = 0.01

        while True:
            result = round(i * i, 2)
            if result == value:
                return i
            
            i = i + 0.01
    except Exception as e:
        raise Exception(f"Math Error: {e}")


def calculate(a: int, b: int, c: int, show: str) -> int:
    root_calc = round(b * b - 4 * a * c, 2)
    if show == "y":
        print()
        print("Way of calculation | Start")
        print("---------------------------------------------------------")
        print(f"{b}² - 4 * {a} * {c} | Getting square root calculation")
        print(f"Result: {root_calc}")
        print()
    root_calculation = root(root_calc)
    if show == "y":
        print(f"√{root_calc} | Getting square root of {root_calc}")
        print(f"Result: {root_calculation}")
        print()
    under = 2 * a
    if show == "y":
        print(f"2 * {a} | Calculating Division")
        print(f"Result: {under}")
        print()
    upper1 = -1 * b + root_calculation
    if show == "y":
        print(f"-1 * {b} + {root_calculation} | Calculating X₁ upper")
        print(f"Result: {upper1}")
        print()
    upper2 = -1 * b - root_calculation
    if show == "y":
        print(f"-1 * {b} - {root_calculation} | Calculating X₂ upper")
        print(f"Result: {upper2}")
        print()
    x1 = upper1 / under
    x2 = upper2 / under
    if show == "y":
        print(f"X₁ = {upper1} : {under} | Dividing")
        print(f"Result: {x1}")
        print()
    if show == "y":
        print(f"X₂ = {upper2} : {under} | Dividing")
        print(f"Result: {x2}")
        print()
    x1 = round(x1, 2)
    x2 = round(x2, 2)
    if show == "y":
        print(f"X₁ = {x1} | Rounding up to x.xx")
        print(f"Result: {x1}")
        print()
        print(f"X₂ = {x2} | Rounding up to x.xx")
        print(f"Result: {x2}")
        print("---------------------------------------------------------")
    if show == "y":
        print("Way of calculation | Finish")
    print()
    return x1, x2


def main():
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    show = str(input("Show way of calculation (y/n): "))
    if show != "y" and show != "n":
        print("Program Error: Show way of calculation is invalid.")
        return

    x1, x2 = calculate(a, b, c, show)
    print(f"X₁ = {x1}")
    print(f"X₂ = {x2}")

if __name__ == "__main__":
    main()