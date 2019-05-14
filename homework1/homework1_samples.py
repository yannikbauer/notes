"""Sample solutions from various students"""

## Exercise 1


def vowelcount(string):
    """Returns the number of vowels in the string 'string'"""
    string = string.upper()
    i = string.count('A')
    i = i + string.count('E')
    i = i + string.count('I')
    i = i + string.count('O')
    i = i + string.count('U')
    i = i + string.count('Ä')
    i = i + string.count('Ö')
    i = i + string.count('Ü')
    print(string, "contains ", i, " vowels")


def vowelcount(string):
    """Takes a string argument and checks each letter """
    allvowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    vowelnumber = 0
    for letter in range(len(string)):
        for vowel in range(len(allvowels)):
            if string[letter] == allvowels[vowel]:
                vowelnumber += 1
            else:
                pass
    return vowelnumber



def vowelcount(x):
    """Returns the number of vowels in a string (independent of case)"""
    vowel = ['a', 'e', 'i', 'o', 'u']
    counter = 0

    for i in range(len(vowel)):
        a = x.count(vowel[i].lower())
        counter = counter + a
        a = x.count(vowel[i].upper())
        counter = counter + a

    return counter


def vowelcount (x):
    """this function takes a word in parenthesis
    and counts the amount of vowels, no matter if capital or not """
    x.lower ()
    print (x.count('a')+x.count('e')+x.count('i')+x.count('o')+x.count('u'))



# Martin's solution:
def vowelcount(s):
    """Count vowels in s"""
    s = s.lower()
    nv = 0
    for v in 'aeiou':
        nv += s.count(v)
    return nv

## Exercise 2


def metric(x,y):
    """ Prints the difference and sum of x & y in a readable way, and also sum/difference"""
    sm = x + y
    df = x - y
    div = sm / df if df != 0 else 0
    return "sum is %s " %sm, "difference is  %s " %df, "division of difference to sum is %s" %div


def metric(x, y):
    """Returns the sum and difference of two variables x and y, as well as the difference divided by the sum"""
    dif = x - y
    sum = x + y
    print("The sum of ", x, " and ", y, " is ", sum)
    print("The difference of ", x, " minus ", y, " is ", dif)
    if sum != 0:
        print("The difference of ", x, " and ", y, " divided by it's sum is ", dif/sum)
    else:
        print("The difference of ", x, " and ", y, " can't be divided by it's sum, because it's sum is 0.")


def metric(x, y):
    """Returns the result of the division of the difference over the sum"""
    add = x + y
    dif = x - y
    print("difference is %f, sum is %f" % (dif, add)) # displays the sum and difference of the two numbers
    if add == 0:
        raise ZeroDivisionError("The sum of your numbers is 0") # an error is raised if I'm about to divide by 0
    else:
         return dif/add


# Martin's solution:
def metric(x, y):
    """Calculate difference over sum"""
    d = x - y
    s = x + y
    print('difference is %g, sum is %g' % (d, s))
    if s == 0:
        return 0
    return d / s



## Exercise 3

def multtable(n):
    "Integers table of 1 to n multiplication"

    for x in range(1,n+1):
            #print(x)
            for y in range(1,n+1):
                result=x*y
                #print(y)

                if y<n:
                    #pass
                    print(str(result) + ' ', end='')
                else:
                    print(result,end='\n')



def multtable(n):
    """ Returns the multiplication table for integers 1 through n """
    for i in range(1,n+1):
        for x in range(1, n+1):
            result = print(i * x, end =' ')
        print ()
    return result


def multtable(n):
    for i in range(1, n + 1):
        m = 1
        while m <= n:
            a = m*i
            print(a)
            m = m +1


def multtable(n):
    for number in range (1,n+1):
        row=[]
        for multiplier in range(1,n+1):
            multiplicationresult= number*multiplier
            row.append(multiplicationresult)
        print(row)


# Martin's solution:
def multtable(n):
    """Print multiplication table from 1 to n"""
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i * j, end=' ')
        print()
