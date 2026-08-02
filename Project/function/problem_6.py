# A programme that counts vowel in a struing

sentence=input("Enter a sentence:").lower().strip()
vowels="a,e,i,o,u"
count=0

for i in sentence:
    if i in vowels:
        count+=1
    else:
        pass

print(f"Vowels:{count}")