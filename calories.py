fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Lemon": 14,
        "Lime": 20,
        "Orange": 80,
        "Pineapple": 50
        }

fruit = input("Фрукт: ")
if fruit in fruits:
    print(f"Калории: {fruits[fruit]}")