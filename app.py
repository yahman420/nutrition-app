foods = {
    "米": {"kcal": 156, "p": 2.5, "f": 0.3, "c": 37.0, "unit": "g"},
    "鶏胸肉": {"kcal": 105, "p": 22.3, "f": 1.5, "c": 0, "unit": "g"},
    "卵": {"kcal": 76, "p": 6.2, "f": 5.2, "c": 0.2, "unit": "個"},
    "鶏もも肉": {"kcal": 120, "p": 19.0, "f": 5.0, "c": 0, "unit": "g"},
    "牛肉": {"kcal": 250, "p": 17.0, "f": 20.0, "c": 0, "unit": "g"},
    "豚肉": {"kcal": 250, "p": 17.0, "f": 19.0, "c": 0, "unit": "g"},
    "納豆": {"kcal": 90, "p": 7.4, "f": 4.5, "c": 5.4, "unit": "個"},
    "牛乳": {"kcal": 65, "p": 3.3, "f": 3.8, "c": 4.8, "unit": "g"},
    "オートミール": {"kcal": 365, "p": 13.7, "f": 6.9, "c": 69.1, "unit": "g"},
    "バナナ": {"kcal": 95, "p": 1.1, "f": 0.2, "c": 23, "unit": "g"},
    "ハチミツ": {"kcal": 320, "p": 0.3, "f": 0, "c": 79.7, "unit": "g"},
}


total_kcal = 0
total_p = 0
total_f = 0
total_c = 0

print("食べたものを入力してください（終了は 終わり）")

while True:
    food = input("food: ")

    if food == "終わり":
        break

    if food not in foods:
        print("その食品は登録されていません")
        continue

    amount = float(input("量（g or 個）: "))

    food_data = foods[food]

    if food_data["unit"] == "g":
        ratio = amount / 100
    else:
        ratio = amount


    total_kcal += food_data["kcal"] * ratio
    total_p += food_data["p"] * ratio
    total_f += food_data["f"] * ratio
    total_c += food_data["c"] * ratio

print(f"\n合計カロリー: {total_kcal:.1f} kcal")
print(f"P: {total_p:.1f} g")
print(f"F: {total_f:.1f} g")
print(f"C: {total_c:.1f} g")