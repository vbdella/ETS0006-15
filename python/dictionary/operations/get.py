person = {"name": "Ali", "age": 20}
print(person.get("age"))  # Output: "20"

person = {"name": "Ali"}
print(person.get("email"))  # Output: "None"

person = {"name": "Ali"}
print(person.get("email", "Not provided"))  # Output: "Not provided"
