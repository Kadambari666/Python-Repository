# Create a simple dictionary
word_meanings = {
    "apple": "a fruit",
    "dog": "a pet animal",
    "sun": "the star at the center of our solar system",
}

# Prompt the user to enter a word
word = input("Enter a word: ")

# Check if the word is in the dictionary
if word in word_meanings:
    meaning = word_meanings[word]
    print(f"The meaning of '{word}' is '{meaning}'.")
else:
    print("Word not found in the dictionary.")
