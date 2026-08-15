d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"d": 4, "e": 5, "f": 6}
print("Dictionary 1:", d1)
print("Dictionary 2:", d2)
merged = {}
for key, value in d1.items():
    merged[key] = value
for key, value in d2.items():
    merged[key] = value
print("Merged dictionary:", merged)
