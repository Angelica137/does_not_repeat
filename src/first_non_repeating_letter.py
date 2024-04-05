def first_non_repeating_letter(word: str) -> str:
    count = {}
    for char in word:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in word:
        if count[char.lower()] == 1:
            return char
    return "No non-repeated letters"
