def filter_numbers(num1, num2):
    numbers = []   
    for i in range(10):
        numbers.append(i)

    for i in numbers:
        if num1 == i:
            numbers.remove(num1)

    for i in numbers:
        if num2 == i:
            numbers.remove(num2)

    return numbers
print(filter_numbers(3, 6))

def star_conversion(word, index):
    s = list(word)

    for i in range(len(word)):
        if i == index -1:
            s[i] ='*'

    star = ''.join(s)
    return star
print(star_conversion('lovely', 3))

def find_exponent(a, n):
    x = 0

    while a ** x < n:
        x += 1
    if a ** x == n:
        return x
    else:
        return 'Exponent x not found'
   
print(find_exponent(5, 125))

def reverse_cases(word_list):
    wordList = []
    for word in word_list:
        if word.isalpha():
          wordList.append(word.swapcase())
        else:
            wordList.append(word[::-1])

    return wordList
print(reverse_cases('Sharmila'))

def month_days(month):
    
    months = {'january': '31', 
              'february': '28', 
              'march': '31',
              'april': '30',
              'may': '31',
              'june': '30',
              'july': '31',
              'august': '31',
              'september': '30',
              'october': '31',
              'november': '30',
              'december': '31'}
    shortHand = {}
    for fullName, days in months.items():
        shortHand[fullName[:3]] = days

    month = month.casefold()

    if month in months:
        return months[month]
    elif month[:3] in shortHand:
        return shortHand[month[:3]]
    else: 
        return 'Not a valid month'

print(month_days('mARch'))

def remove_duplicates(list):
    noduplicates = []
    for item in list:
        if item not in noduplicates:
            noduplicates.append(item)
    return noduplicates

print(remove_duplicates([1, 3, 4, 10, 4, 1, 43]))

def fibonacci(n):
    fibList = []
    a = 0
    b = 1
    for i in range(n):
        fibList.append(a)
        a, b = b, a + b                                             
        
    return fibList

print(fibonacci(5))

def prime_words(sentence):
    def is_prime(n):
        for i in range(2, n):
            if n%i == 0:
                return False
        return True
    
    splitSentence = sentence.split()
    new_sentence = []
    for word in splitSentence:
        if is_prime(len(word)):
            new_sentence.append(word)
    s = ' '.join(new_sentence)
    new_sentence = s
    return new_sentence

print(prime_words("Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later."))

    
def shift_decimals(test_int, decimal_shift):
    number = list(str(test_int))
    new_list = number[decimal_shift:] + number[:decimal_shift]

    number = ''.join(new_list)

    if decimal_shift > len(number): 
        r = number[::-1]
        number = r
    
    return int(number)

print(shift_decimals(12345, 6))