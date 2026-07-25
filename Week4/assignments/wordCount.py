# Create the function word_frequency() that takes a string parameter (text)
def word_frequency(text):
    
    # To store the cleaned text
    clean_text = ""
    
    # Go through each character in the text
    for char in text:
        # If character is a letter, space, or apostrophe, keep it
        if char.isalpha() or char == " " or char == "'":
            clean_text = clean_text + char.lower()
        # Otherwise (punctuation), skip it
    
    # Split into words
    words = clean_text.split()
    
    # Count each word using a dictionary
    word_count = {}
    
    for word in words:
        # If word already in dictionary, add 1
        if word in word_count:
            word_count[word] = word_count[word] + 1
        # If word not in dictionary, add it with count 1
        else:
            word_count[word] = 1
    
    # Find top 3 most frequent words, and list to store words and their counts
    word_list = []
    
    # Convert dictionary to list of (count, word) tuples
    for wo, count in word_count.items():
        word_list.append((count, wo))
    
    # Sort the list in reverse order (highest count first), simple bubble sort (basic sorting)
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if word_list[i][0] < word_list[j][0]:
                # Swap if count is smaller
                temp = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = temp
    
    # Get top 3 words
    top_words = {}
    
    # Take first 3 items (or less if there aren't 3)
    num_words = 3
    if len(word_list) < 3:
        num_words = len(word_list)
    
    for i in range(num_words):
        count = word_list[i][0]
        word = word_list[i][1]
        top_words[word] = count
    
    # Print results
    print("Top 3 words:")
    for w, count in top_words.items():
        print(f"{w} — {count} times")
    
    return top_words


# Testing the function with the given text
text = """ Nepal is a beautiful country. Nepal has Mount Everest. Everest is the highest mountain in the world. Many tourists visit Nepal every year to see Everest and other mountains. Nepal is known for its mountains and natural beauty. """

# Calling the function
word_frequency(text)

