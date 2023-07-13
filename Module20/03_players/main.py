players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
new_players = []
for keys, values in players.items():
    name, surname = keys
    print(name, surname, values)
