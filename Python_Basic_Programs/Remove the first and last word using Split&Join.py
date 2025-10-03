sentence = "Learning Python is really fun" 
sen= sentence.split()
print(sen)

#['Learning', 'Python', 'is', 'really', 'fun']
print(sen[1:-1:1])

fc = " ".join(sen[1:-1:1])
print(fc)