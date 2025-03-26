text1 = "Python is awesome"
words = text1.split()
print(words)  # Output: "['Python', 'is', 'awesome']"


text2 = "apple,banana,grape"
fruits = text2.split(",")
print(fruits)  # Output: "['apple', 'banana', 'grape']"


text3 = "name:age:city:country"
parts = text3.split(":", 2)
print(parts)  # Output: "['name', 'age', 'city:country']"
