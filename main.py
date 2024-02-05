my_list=[
    ["Андрій",13,"Англійська"],
    ["Єгор",14,"Історія"],
    ["Ваня",14,"Українська"],
    ["Никита",13,"Алгебра"],
    ["Ярослав",14,"Геометрія"]
]
copied_friends = [friend.copy() for friend in my_list]
for friend in copied_friends:
    friend[1] += 1

print("Остаточний список друзів з віком на одиницю більше:", copied_friends)

my_age = 13
my_list = [friend for friend in copied_friends if friend[1] != my_age]
print("Список з друзями не мого віку:", my_list)

friend_list=[
    ["Олексій",13,"Географія"],
    ["Кирило",14,"Фізкультура"],
    ["Павло",13,"Інформатика"]
]

my_list.extend(friend_list)
print("Остаточний список:", my_list)