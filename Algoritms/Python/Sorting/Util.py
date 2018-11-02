import  random
def swapInArray(array, a, b):
    array[a],array[b] = array[b],array[a]

def isOrdened(array):
    ans = True
    for i in range(len(array) - 1):
        if(array[i] > array[i + 1]):
            ans = False
            break
    return ans

def shake(array):
    lenarray = len ( array )
    for i in range(lenarray):
        swapInArray( array, i, (random.randint( 0, lenarray ) * random.randint( 0, lenarray )) % lenarray )

def randomList(lenght):
    array = []
    for i in range (lenght):
        a = random.randint ( - (i ** 2), i ** 2 )

        array.append (a)
    return array