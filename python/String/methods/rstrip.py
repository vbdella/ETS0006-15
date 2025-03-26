text1 = "Hello, Python!   "
clean_text1 = text1.rstrip()
print(clean_text1)  # Output: "Hello, Python!"


text2 = "Python####"
clean_text2 = text2.rstrip("#")
print(clean_text2)  # Output: "Python"


text3 = "Hello123"
clean_text3 = text3.rstrip("123")
print(clean_text3)  # Output: "Hello"
  