def str_methods():
        # Problem Set 3: String Methods
    # Upper & Lower:
    # Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
    text = "MAY THE FORCE BE WITH YOU."
    lowercase_text = text.lower()
    print(lowercase_text)


    # String Joining and Splitting:
    # Given the list motto = ["Make", "haste", "slowly."],
    motto = ["Make", "haste", "slowly."]
    # a. Convert the list into a single string.
    motto_string = ' '.join(motto)
    # b. Now, split the string at every occurrence of the letter 'a'.
    split_motto = motto_string.split('a')

    # Replacing Words:
    # Modify the sentence: "Life is what happens when you are busy making other plans."
    sentence = "Life is what happens when you are busy making other plans."
    # a. Replace "busy" with "distracted".
    sentence = sentence.replace("busy", "distracted")
    # b. Replace "plans" with "mistakes".
    sentence = sentence.replace("plans", "mistakes")
    print(sentence)

