# Tasks
# 1. Extract the first sentence
# 2. Extract last sentence
# 3. Find the longest word
# 4. Find Frequency of a Character in a String in Python
# 5. Count the Number of Spaces in a String in Python
# 6. Remove characters or other than words

# Output
# 1. First Sentence: "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
#  Last Sentence: "In hac habitasse platea dictumst."
# 2. Longest Word: "malesuada" (Length: 9)
# 3. Cleaned Text: "Lorem ipsum dolor sit amet consectetur adipiscing elit Sed at magna libero
# Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas Proin
# dictum odio eget consectetur lacinia mi dui semper odio in posuere tellus elit eget enim Donec lacinia
# orci id purus fringilla fringilla Nullam in sapien quis ex facilisis euismod Nunc condimentum lacinia nisl sit
# amet vestibulum libero convallis ac Nam bibendum tellus at massa elementum varius Vivamus
# consequat elit nec vestibulum iaculis velit urna mattis arcu nec rutrum orci turpis vel urna Ut tempor
# nunc at orci facilisis fringilla Nulla facilisi Duis sagittis odio et pharetra rhoncus nulla justo tincidunt
# mauris nec porttitor tortor justo non orci In hac habitasse platea dictumst"

# (Note: The provided example is for illustration purposes only. Your program should work with any valid
# input text.)
#
# Ensure that your program handles cases where the text may have multiple spaces, special characters, or
# variations in sentence ending punctuation. Also, consider creating functions to perform each task for
# better organization and reusability.
import string

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at magna libero. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin dictum, odio eget consectetur lacinia, mi dui semper odio, in posuere tellus elit eget enim. Donec lacinia orci id purus fringilla fringilla. Nullam in sapien quis ex facilisis euismod. Nunc condimentum lacinia nisl, sit amet vestibulum libero convallis ac. Nam bibendum tellus at massa elementum varius. Vivamus consequat, elit nec vestibulum iaculis, velit urna mattis arcu, nec rutrum orci turpis vel urna. Ut tempor nunc at orci facilisis fringilla. Nulla facilisi. Duis sagittis, odio et pharetra rhoncus, nulla justo tincidunt mauris, nec porttitor tortor justo non orci. In hac habitasse platea dictumst."

text_to_lines = text.split('.', (text.count('.') - 1))

# Task 1:
print(text_to_lines[0].strip())

# Task 2:
print(text_to_lines[-1].strip().strip('.'))

text_to_words = text.split(' ')
index = 0
longest_word = ''
longest_word_index = ''

for word in text_to_words:
    text_to_words[index] = word.strip().strip('.')
    if len(text_to_words[index]) >= len(longest_word):
        longest_word = text_to_words[index]
        longest_word_index = index
    index = index + 1

# Task 3.
print(longest_word)

# Task 4
print(text.count('m'))

# Task 5
print(text.count(' '))

# Task 6
print(text.translate(str.maketrans('', '', string.punctuation)))

