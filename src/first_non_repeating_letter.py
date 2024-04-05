def first_non_repeating_letter(word: str) -> str:
    count = {}
    for char in word:
        lower_char = char.lower()
        count[lower_char] = count.get(lower_char, 0) + 1
    for char in word:
        if count[char.lower()] == 1:
            return char
    return "No non-repeated letters"
