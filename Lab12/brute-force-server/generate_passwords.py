name = "farid"
birth_year = "2003"

passwords = [
    name,
    name + "123",
    name + birth_year,
    name.capitalize() + birth_year,
    name + "@123",
    name + "12345",
    birth_year + name,
    name + "_admin"
]

with open("generated_passwords.txt", "w") as f:
    for p in passwords:
        f.write(p + "\n")

print("Password list generated!")
