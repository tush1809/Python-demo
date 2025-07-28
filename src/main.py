from calculator.calculator import Calculator


def main():
    print("Starting Python Demo Application")

    # Demo Calculator
    calc = Calculator()

    result = calc.add(10.5, 20.3)
    print(f"Calculator result: 10.5 + 20.3 = {result}")

    result = calc.multiply(5.0, 4.0)
    print(f"Calculator result: 5.0 * 4.0 = {result}")

    print("Demo Application completed successfully")


if __name__ == "__main__":
    main()
