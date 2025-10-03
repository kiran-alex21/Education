## Run Length Encoding
"""
Take a string of text in
Find all of the consecutive character strings
Count how many characters in each consecutive group
Encode with character + number in group
Put each encode together
Print Encoding
"""

text = input("What would you like to encode? ")
i = 0
encoded = ""

# Run-length encoding
while i < len(text):
    charCount = 1
    while i + charCount < len(text) and text[i] == text[i + charCount]:
        charCount += 1
    encoded += text[i] + str(charCount)
    i += charCount
print(encoded)
