import math
def sum_numbers():
    num = int(input("How many numbers do you want to sum? "))
    numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num)]
    return sum(numbers)

def subtraction():
    # num = int(input("How many numbers do you want to sum? "))
    # numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num)]
    # return (numbers)
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    return a - b

def multiplication():
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    return a * b

def division():
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    return a / b if b != 0 else "Cannot divide by zero"

def factorialnum():
    num = int(input("Enter a number for factorial: "))
    return math.factorial(num)

def table():
    num = int(input("Enter a number for the table: "))
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")

def percentage():
    numobt = float(input("Enter obtained marks: "))
    numtot = float(input("Enter total marks: "))
    return (numobt / numtot) * 100 if numtot != 0 else "Invalid total marks"

def average():
    num = int(input("Total numbers: "))
    numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num)]
    return sum(numbers) / num

def minimum():
    num = int(input("How many numbers? "))
    numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num)]
    return min(numbers)

def maximum():
    num = int(input("How many numbers? "))
    numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num)]
    return max(numbers)

def power():
    a = int(input("Enter base: "))
    b = int(input("Enter exponent: "))
    # return pow(a, b)

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcmnumbers():
    nums = list(map(int, input("Enter up to 3 numbers separated by space: ").split()))
    while len(nums) > 3:
        nums = list(map(int, input("Only 3 numbers allowed. Try again: ").split()))
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return lcm(nums[0], nums[1])
    elif len(nums) == 3:
        return lcm(lcm(nums[0], nums[1]), nums[2])

def quad():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = b**2 - 4*a*c
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        return f"Roots are real and distinct: {r1}, {r2}"
    elif d == 0:
        r = -b / (2*a)
        return f"Roots are real and equal: {r}"
    else:
        real = -b / (2*a)
        imag = math.sqrt(-d) / (2*a)
        return f"Roots are complex: {real}+{imag}i, {real}-{imag}i"

def scientific_functions():
    print("1. Square Root")
    print("2. Log")
    print("3. Sin")
    print("4. Cos")
    print("5. Tan")
    choice = int(input("Choose: "))
    num = float(input("Enter a number: "))
    if choice == 1:
        return math.sqrt(num)
    elif choice == 2:
        return math.log(num)
    elif choice == 3:
        return math.sin(num)
    elif choice == 4:
        return math.cos(num)
    elif choice == 5:
        return math.tan(num)
    else:
        return "Invalid choice"

def main():
    while True:
        print("\n--- OPERATIONS MENU ---")
        print("1. SUM")
        print("2. SUBTRACTION")
        print("3. MULTIPLICATION")
        print("4. DIVISION")
        print("5. FACTORIAL")
        print("6. TABLE")
        print("7. PERCENTAGE")
        print("8. AVERAGE")
        print("9. MINIMUM")
        print("10. MAXIMUM")
        print("11. POWER")
        print("12. SCIENTIFIC FUNCTIONS")
        print("13. LCM")
        print("14. QUADRATIC EQUATION")
        print("0. EXIT")

        choice = int(input("Enter your choice: "))
        print("\n")

        if choice == 0:
            print("Thank you!")
            break
        elif choice == 1:
            print("Sum:", sum_numbers())
        elif choice == 2:
            print("Subtraction:", subtraction())
        elif choice == 3:
            print("Multiplication:", multiplication())
        elif choice == 4:
            print("Division:", division())
        elif choice == 5:
            print("Factorial:", factorialnum())
        elif choice == 6:
            table()
        elif choice == 7:
            print("Percentage:", percentage())
        elif choice == 8:
            print("Average:", average())
        elif choice == 9:
            print("Minimum:", minimum())
        elif choice == 10:
            print("Maximum:", maximum())
        elif choice == 11:
            print("Power:", power())
        elif choice == 12:
            print("Result:", scientific_functions())
        elif choice == 13:
            print("LCM:", lcmnumbers())
        elif choice == 14:
            print(quad())
        else:
            print("Invalid choice.")

        again = input("Do you want to perform another operation? (Y/N): ").lower()
        if again != 'y':
            print("Thank you!")
            break
if __name__ == "__main__":
    main()