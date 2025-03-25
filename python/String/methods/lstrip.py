text = "   Hello, Python!"
clean_text = text.lstrip()
print(clean_text)  # Output: "Hello, Python!"


text = "###Python###"
clean_text = text.lstrip("#")
print(clean_text)  # Output: "Python###"


text = "abc123Hello"
clean_text = text.lstrip("abc123")
print(clean_text)  # Output: "Hello"
