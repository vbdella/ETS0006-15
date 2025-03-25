text = "Hello, Python!   "
clean_text = text.rstrip()
print(clean_text)  # Output: "Hello, Python!"


text = "Python####"
clean_text = text.rstrip("#")
print(clean_text)  # Output: "Python"


text = "Hello123"
clean_text = text.rstrip("123")
print(clean_text)  # Output: "Hello"
  