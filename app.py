foods = {
    "米": {"kcal": 156},     # 100gあたり
    "鶏胸肉": {"kcal": 105},  # 100gあたり
    "卵": {"kcal": 76}        # 1個あたり
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

    if food in ["米", "鶏胸肉"]:
        total_kcal += foods[food]["kcal"] * (amount / 100)
    else:
        total_kcal += foods[food]["kcal"] * amount

print(f"\n合計カロリー: {total_kcal:.1f} kcal")