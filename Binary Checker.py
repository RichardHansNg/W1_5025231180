def binary_checker(sentence, words):
    while True:
        matches = []
        for word in words:
            if word in sentence:
                matches.append(word)
        if not matches:
            break
        longest_match = max(matches, key=len)
        sentence = sentence.replace(longest_match, "", 1)
    if sentence == "":
        print("VALID")
    else:
        print("INVALID")

S = {"00", "10", "010", "01001"}

user_input = input()
binary_checker(user_input, S)
