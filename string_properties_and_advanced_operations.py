def str_prop_and_advanced_op():
    # Problem Set 4: String Properties and Advanced Operations
    # Repetition:
    # Concatenate the word "Iteration" 7 times.
    word = "Iteration"
    result = word * 7
    print(result)

    # Word Search:
    # Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

    quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"


    word = "moonlight"


    if word in quote:
        print(f'The word "{word}" was found in the quote.')
    else:
        print(f'The word "{word}" was not found in the quote.')

    # Length and Count:
    # a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
    # b. Count the number of times the letter 'i' appears in the same word/phrase.

    phrase = "Supercalifragilisticexpialidocious"
    num_characters = len(phrase)
    count_i = phrase.lower().count('i')


    print(f"Number of characters: {num_characters}")
    print(f"Count of 'i': {count_i}")
