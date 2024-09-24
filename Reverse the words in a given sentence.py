#Write a Python program to reverse the words in a given sentence
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence
print(reverse_sentence("It's a lovely day"))