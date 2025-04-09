car = {"brand": "Toyota", "model": "Corolla"}
print(car.keys())  # Output: "dict_keys(['brand', 'model'])"

car = {"year": 2020, "color": "blue"}
keys_list = list(car.keys())
print(keys_list)  # Output: "['year', 'color']"

fruit = {"apple": 1, "banana": 2}
for key in fruit.keys():
    print(key)  # Output: "apple  banana"
