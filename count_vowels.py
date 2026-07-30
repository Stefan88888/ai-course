def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            count +=1
    return count
            

result = count_vowels("Hello")
print(result)
