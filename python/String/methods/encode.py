text1 = "Hello"
encoded_text1 = text1.encode()
print(encoded_text1)  # Output: "b'Hello'"

text2 = "Café"
encoded_text2 = text2.encode("utf-8")
print(encoded_text2)  # Output: "b'Caf\xc3\xa9'"

encoded_text3 = b'Hello'
decoded_text = encoded_text3.decode()
print(decoded_text)  # Output: "Hello"
