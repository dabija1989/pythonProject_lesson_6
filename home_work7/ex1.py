number = int(input("Introdu un numar intreg pozitiv:\n"))
if number < 0:
    print("numarul introdus nu este pozitiv")
elif number == 0:
    print(f"Factorial de {number} este 1.")
elif number > 0:
    i = 1
    factorial = 1
    while i <= number:
        factorial *= i
        i += 1
print(f"Factorial din {number} este {factorial}.")
