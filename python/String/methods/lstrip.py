text1 = "   Hello, Python!"
clean_text1 = text1.lstrip()
print(clean_text1)  # Output: "Hello, Python!"


text2 = "###Python###"
clean_text2 = text2.lstrip("#")
print(clean_text2)  # Output: "Python###"


text3 = "abc123Hello"
clean_text3 = text3.lstrip("abc123")
print(clean_text3)  # Output: "Hello"
