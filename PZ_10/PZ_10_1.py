magnit = {"shop": "Магнит",
          "products": {"молоко", "соль", "сахар"}}
pyaterochka = {"shop": "Пятёрочка",
             "products": {"мясо", "молоко", "сыр"}}

allProducts = magnit["products"].union(pyaterochka["products"])
difmagnit = allProducts - magnit["products"]
difpyaterohcka = allProducts - pyaterochka["products"]
print("Товары из Магнита, которые отсутствуют в Пятёрочке: ", difpyaterohcka)
print("Товары из Пятёрочки, которые отсутствуют в Магните: ", difmagnit)
print("Перечень всех продуктов: ", allProducts)
print("Из данных перечней товаров в магазинах равно(ы) только:",
      magnit["products"] & pyaterochka["products"])
