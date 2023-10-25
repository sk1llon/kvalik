def count_unique_characters(string):
    global unique_count
    new_set = set(map(lambda x: x.lower(), filter(lambda x: 'a' <= x <= 'z', string)))
    unique_count = len(new_set)


message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = 0
count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
