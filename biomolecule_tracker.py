import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("nutrition.csv")

print("\n🔬 Welcome to the Biomolecule Tracker with Graph!\n")

while True:
    food = input("Enter a food item (or type 'exit' to quit): ").strip().lower()

    if food == 'exit':
        print("👋 Thank you for using the Biomolecule Tracker!")
        break

    # Filter using lower-case comparison
    matched = df[df['name'].str.lower() == food]

    if not matched.empty:
        item = matched.iloc[0]

        carbs = item['carbohydrate']
        protein = item['protein']
        fats = item['fat']

        print(f"\n📋 Nutritional content of {item['name']}:")
        print(f"🍞 Carbohydrates: {carbs}g")
        print(f"🍗 Protein: {protein}g")
        print(f"🧈 Fats: {fats}g")

        # Plotting the graph
        plt.bar(['Carbohydrates', 'Proteins', 'Fats'], [carbs, protein, fats], color=['orange', 'green', 'red'])
        plt.title(f'Nutrient Breakdown of {item["name"]}')
        plt.ylabel('Grams')
        
    else:
        print("❌ Food not found. Please check the spelling or try another.\n")
