def character_count(word):
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


word1 = "Happiness"
word2 = "smiles"

print(character_count(word1))
print(character_count(word2))
