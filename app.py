foods = {
    "米": {"kcal": 156},     # 100gあたり
    "鶏胸肉": {"kcal": 105},  # 100gあたり
    "卵": {"kcal": 76} ,       # 1個あたり
    "鶏もも肉":{"kcal":120},    #皮無し100gあたり
    "牛肉":{"kcal":250},       #平均的な牛肉のカロリーです100gあたり
    "豚肉":{"kcal":250},       #平均的な１００gあたりの豚肉のカロリーです
    "納豆":{"kcal":90},        #1パックあたり
    "牛乳":{"kcal":65},        #100mlあたり
    "オートミール":{"kcal":365},  #100gあたり
    "バナナ":{"kcal":95},        #100gあたり
    "ハチミツ":{"kcal":320},     #100gあたり

    }

total_kcal = 0

print("食べたものを入力してください（終了は 終わり）")

while True:
    food = input("food: ")

    if food == "終わり":
        break

    if food not in foods:
        print("その食品は登録されていません")
        continue

    amount = float(input("量（g or 個）: "))

    if food in ["米", "鶏胸肉","鶏もも肉", "牛肉","豚肉","牛乳","オートミール","バナナ"]:
        total_kcal += foods[food]["kcal"] * (amount / 100)
    else:
        total_kcal += foods[food]["kcal"] * amount

print(f"\n合計カロリー: {total_kcal:.1f} kcal")