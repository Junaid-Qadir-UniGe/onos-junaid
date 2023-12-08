# square_calculator.py

def square(number):
    return number ** 2

if __name__ == "__main__":
    user_input = float(input("Enter a number: "))
    result = square(user_input)
    print(f"The square of {user_input} is {result}")
