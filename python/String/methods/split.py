text = "Python is awesome"
words = text.split()
print(words)  # Output: "['Python', 'is', 'awesome']"


text = "apple,banana,grape"
fruits = text.split(",")
print(fruits)  # Output: "['apple', 'banana', 'grape']"


text = "name:age:city:country"
parts = text.split(":", 2)
print(parts)  # Output: "['name', 'age', 'city:country']"
