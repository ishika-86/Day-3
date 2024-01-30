# Determines if a string reads the same backward as forward.
text1 = input()

if text1 == text1[::-1]:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")
