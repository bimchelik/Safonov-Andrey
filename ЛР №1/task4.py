users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

statistics = {
"Общее количество": 0,
"Уникальные посещения": 0
}

statistics["Общее количество"] = len(users)

unique = set(users)
statistics["Уникальные посещения"] = len(unique)

print(statistics)