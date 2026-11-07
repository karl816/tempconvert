temp = int(input("Enter a temperature: "))
unit = input("Select a unit C for Celsius or F for Fahrenheit): ").lower()


if unit == "f":
    result = (temp - 32) * 5/9
    print(f"The temperature in Celsius is {result:.0f}C°")
elif unit == "c":
    result = (temp * 9 / 5) + 32
    print(f"The temperature in Fahrenheit is {result:.0f}F°")
else:
    print("Invalid unit, select Celsius or Fahrenheit")