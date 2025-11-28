import random
import json

meals = [
    "Kartoffelpüree mit Erbsen, Möhren und Ei", "Risi Bisi", "Tacos", "Shakshuka", "Nudeln mit Soße",
    "Pizza", "Erbsensuppe", "Burger", "Bulgurauflauf", "Linsensuppe", "Tomatenreis", "Curry mit Reis/Couscous",
    "Bretonische Bohnensuppe", "Oliven-Feta-Knödel", "Mie-Nudeln mit Gemüse", "Kartoffelsalat", "Gurkensuppe",
    "Gazpacho", "Bärlauch/Basilikum Klöße mit Tomatensoße", "Haloumni Omelett", "Ofengemüse", "Kartoffelgratin",
    "Pellkartoffeln mit Quark"
]

days = ["Samstag", "Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]

selected_meals = random.sample(meals, 7)

# Combine into a list of dictionaries
meal_plan = [{"Tag": day, "Gericht": meal} for day, meal in zip(days, selected_meals)]

with open("meal_plan.json", "w") as f:
    json.dump(meal_plan, f)
