vcount = 0
ccount = 0

text = input()
text = text.lower()
for i in range(len(text)):
    if text[i] in ('a', 'e', 'i', 'o', 'u'):
        vcount += 1
    elif 'z' >= text[i] >= 'a':
        ccount += 1

print(f" vowels: {vcount}")
print(f" consonants: {ccount}")
