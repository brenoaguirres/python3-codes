print("breno".upper())
print("BRENO".lower())
print("bRENo Aguirres".title())
print("pErson".islower())
print("PERsoN".isupper())
print("Breno".startswith("Br"))
print("Aguirres".endswith("es"))
print("Breno Aguirres".replace("Aguirres", "Freitas"))
print("Breno Aguirres".split())
print("Breno Aguirres".split("A"))
print("Breno Aguirres".strip())
print("Breno Aguirres".join("Fr"))
print("Breno Aguirres".find("n"))
print("Breno Aguirres".isalpha())  # does it contain only characters and is not empty?
print("Breno Aguirres".isalnum())  # check if contains characters or digits and its not empty
print("Breno Aguirres".isdecimal())  # check if contains digits and is not empty

# they return a new string, they don't modify the string
name = "Breno"
print(name.lower())
print(name)  # continues not lowered

# lenght of a string
print(len("Breno"))

# check if string contains substring
print("re" in name)
print("au" in name)

