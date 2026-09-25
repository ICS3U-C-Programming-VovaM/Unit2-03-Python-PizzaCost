#!/usr/bin/env python3
# Created By: Vova M
# Date: Sep 25, 2026

import math


def main():
    calculate_pizza_details()

def calculate_pizza_details():
    print("--- Pizza Cost & Measurement Calculator ---\n")

    # Get user input
    try:
        diameter = float(input("Enter the diameter of the pizza (in inches): "))
        price_per_sq_inch = float(input("Enter the price per square inch ($): "))
    except ValueError:
        print("\nInvalid input! Please enter numerical values.")
        return

    # Calculations
    radius = diameter / 2.0

    # Area of a circle = π * r^2
    area = math.pi * (radius**2)

    # Perimeter (Circumference) = 2 * π * r
    perimeter = 2 * math.pi * radius

    # Total cost = Area * price per square inch
    total_cost = area * price_per_sq_inch

    # Display results formatted to 2 decimal places
    print("\n--- Results ---")
    print(f"Pizza Area: {area:.2f} sq in")
    print(f"Pizza Perimeter (Circumference): {perimeter:.2f} inches")
    print(f"Total Cost: ${total_cost:.2f}")


if __name__ == "__main__":
    calculate_pizza_details()
