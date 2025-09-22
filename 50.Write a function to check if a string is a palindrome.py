#50.Write a function to check if a string is a palindrome
def check_palindrom(word):
    result=""
    for i in word:
        result=i+result
    
    if word==result:
        return True
    else:
        return False
word=input('Enter the word:')
print(f"the word {word} is palindrome:{check_palindrom(word)}")
