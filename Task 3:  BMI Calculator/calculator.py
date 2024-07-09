def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Your BMI category is: {category}")

    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox
import json
import os
import matplotlib.pyplot as plt

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x300")

        self.user_data = self.load_user_data()

        self.create_widgets()

    def create_widgets(self):
        self.label_weight = tk.Label(self.root, text="Weight (kg):")
        self.label_weight.pack(pady=5)
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.pack(pady=5)

        self.label_height = tk.Label(self.root, text="Height (m):")
        self.label_height.pack(pady=5)
        self.entry_height = tk.Entry(self.root)
        self.entry_height.pack(pady=5)

        self.button_calculate = tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        self.button_calculate.pack(pady=5)

        self.label_result = tk.Label(self.root, text="")
        self.label_result.pack(pady=5)

        self.button_save = tk.Button(self.root, text="Save Data", command=self.save_data)
        self.button_save.pack(pady=5)

        self.button_view = tk.Button(self.root, text="View Data", command=self.view_data)
        self.button_view.pack(pady=5)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())

            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Weight and height must be positive values.")
                return

            bmi = weight / (height ** 2)
            category = self.classify_bmi(bmi)

            result_text = f"BMI: {bmi:.2f}\nCategory: {category}"
            self.label_result.config(text=result_text)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    def save_data(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            bmi = weight / (height ** 2)

            self.user_data.append({"weight": weight, "height": height, "bmi": bmi})

            with open("user_data.json", "w") as f:
                json.dump(self.user_data, f, indent=4)

            messagebox.showinfo("Success", "Data saved successfully.")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values.")

    def view_data(self):
        if not self.user_data:
            messagebox.showinfo("No Data", "No data available to display.")
            return

        weights = [data["weight"] for data in self.user_data]
        bmis = [data["bmi"] for data in self.user_data]

        plt.plot(weights, bmis, marker='o')
        plt.xlabel("Weight (kg)")
        plt.ylabel("BMI")
        plt.title("BMI Trend")
        plt.show()

    def load_user_data(self):
        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as f:
                return json.load(f)
        return []

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()
