text = "Hello World"
print(len(text))   # Output: "11"

text1 = ""
print(len(text1))   # Output: "0"

password = "myp@ssword"
if len(password) < 8:
    print("Password is too short.")
else:
    print("Password is valid.")   # Output: "Password is valid."