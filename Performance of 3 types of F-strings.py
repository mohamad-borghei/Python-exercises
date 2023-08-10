
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for char in main_characters:
    print(f'{char[0]} is a {char[2].lower() } voiced by {char[1]}' )

print()

for char in main_characters:
    print('%s is a %s voiced by %s' %(char[0],char[2].lower(),char[1]))

print()

for char in main_characters:
    a='{} is a {} voiced by {}'
    print(a.format(char[0], char[2].lower(), char[1]))