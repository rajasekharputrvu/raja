sentance = "Great! You re asking how to extract the last 3 words from a sentence using slicing."
splt = sentance.split()

print(splt)

#['Great!', 'You', 're', 'asking', 'how', 'to', 'extract', 'the', 'last', '3', 'words', 'from', 
# 'a', 'sentence', 'using', 'slicing#.']

print(splt[-3::1])

print(len(splt)//2)

print(splt[0:3:1])

result = " ".join(sentance.split()[-3:])
print(result)

result = " ".join(sen.split()[0:3:1])

print(result)