def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
   return (f - 32) * 5 / 9

def main():
    unit = input("Is the temperature in Celsius or Fahrenheit? ").strip().lower()
    try:
        value = float(input("Input the temperature: "))
    except ValueError:
        print("Invalid temperature input. Please enter a number.")
        return

    if unit == "celsius":
        answer = celsius_to_fahrenheit(value)
        print(f"{value}°C is {round(answer, 2)}°F")
    elif unit == "fahrenheit":
        answer = fahrenheit_to_celsius(value)
        print(f"{value}°F is {round(answer, 2)}°C")
    else:
        print("Invalid unit. Please enter 'Celsius' or 'Fahrenheit'.")

if __name__ == "__main__":
    main()