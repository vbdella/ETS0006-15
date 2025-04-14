data = {"python", "java"}
data.discard("java")
print(data)  # Output: "{'python'}"

langs = {"C", "C++"}
langs.discard("Go")
print(langs)  # Output: "{'C', 'C++'}"

scores = {100, 90, 80}
scores.discard(90)
print(scores)  # Output: "{100, 80}"
