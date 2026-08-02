# A programme that counts words in statement

sentence=input("Enter the sentence:")

words = sentence.split()#To divide the words into seprate element

num_words=len(words)

print(f"Number of words:{num_words}")