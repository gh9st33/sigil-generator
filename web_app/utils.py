```python
import random

def remove_vowels_and_duplicates(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = ''.join([i for i in word if not i in vowels])
    word = ''.join(sorted(set(word), key = word.index))
    return word

def convert_to_numbers(word):
    codex = {
        'a': 1, 'j': 1, 's': 1,
        'b': 2, 'k': 2, 't': 2,
        'c': 3, 'l': 3, 'u': 3,
        'd': 4, 'm': 4, 'v': 4,
        'e': 5, 'n': 5, 'w': 5,
        'f': 6, 'o': 6, 'x': 6,
        'g': 7, 'p': 7, 'y': 7,
        'h': 8, 'q': 8, 'z': 8,
        'i': 9, 'r': 9
    }
    numbers = [codex[i] for i in word]
    return numbers

def randomize_order(numbers):
    random.shuffle(numbers)
    return numbers

def generate_sigil_data(word):
    word = remove_vowels_and_duplicates(word)
    numbers = convert_to_numbers(word)
    numbers = randomize_order(numbers)
    return numbers
```