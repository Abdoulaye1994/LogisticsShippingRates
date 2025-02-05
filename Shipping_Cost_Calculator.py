# Shipping Cost Calculator

## Input package weight and shipping rate
try:
    weight = float(input("Enter the package weight in kilograms: "))
    rate = float(input("Enter the shipping rate per kilogram: "))
except ValueError:
    print("Please enter valid numbers for weight and rate.")
    exit(1)  # Arrêter le programme si une valeur invalide est entrée

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result, rounded to 2 decimal places
print(f"Shipping Cost: {shipping_cost:.2f} USD")

