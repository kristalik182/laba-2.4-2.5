input_string = input("Введите строку: ")
if input_string.startswith("abc"):
    modified_string = "www" + input_string[3:]
else:
    modified_string = input_string + "zzz"
print("Измененная строка:", modified_string)
