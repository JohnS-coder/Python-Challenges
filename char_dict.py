sentence = input("Enter your sentence: ")
print({str(i):sentence.count(i) for i in set(sentence)})