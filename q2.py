def telephone_words(digit_string):
    digit_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def word_combinations(digits):
        if len(digits) == 0:
            return ['']
        else:
            current_digit = digits[0]
            remaining_digits = digits[1:]
            words_for_remaining_digits = word_combinations(remaining_digits)
            possible_words = []
            for letter in digit_map.get(current_digit, ''):
                for word in words_for_remaining_digits:
                    possible_words.append(letter + word)
            return possible_words

    return word_combinations(digit_string)

