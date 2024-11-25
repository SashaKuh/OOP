class FirstLetterExtractor:
    def extract(self, word):
        return word[0] if word else None


class MiddleLetterExtractor:
    def extract(self, word):
        length = len(word)
        if length == 0:
            return None
        elif length % 2 == 0:
            # Якщо кількість букв парна - забираєм  дві середні букви
            middle_index = length // 2
            return word[middle_index - 1:middle_index + 1]
        else:
            # Якщо кількість букв непарн - одну
            middle_index = length // 2
            return word[middle_index]


class LastLetterExtractor:
    def extract(self, word):
        return word[-1] if word else None


# Результат:

word = "cat"

# об'єкти
first_extractor = FirstLetterExtractor()
middle_extractor = MiddleLetterExtractor()
last_extractor = LastLetterExtractor()

first_letter = first_extractor.extract(word)
middle_letter = middle_extractor.extract(word)
last_letter = last_extractor.extract(word)

print(f"Перша буква: {first_letter}")
print(f"Середня буква: {middle_letter}")
print(f"Остання буква: {last_letter}")
