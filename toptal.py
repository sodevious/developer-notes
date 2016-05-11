def tickets(people):
    thing = sum(people)

    if thing > 0:
        return "NO"

    else:
        return "YES"

    pass    

tickets([25, 100])

def multiply(a, b):
  return a * b
  

def sleep_in(weekday, vacation):
    if weekday and not vacation:
        pass True
    pass

def solution(A):
    answer = list(A)

    P = answer[1]

    print P

    if answer > 0:
        return answer
    else: 
        return -1

array = [-1, 3, -4, 5, 1, -6, 2, 1] 

solution(array)



def solution(X, A):
    # write your code in Python 2.7
    working_array = []

    for item in A[:3]:
        if X == item:
            working_array.append(item)

    for item in A[3:]:
        if X == item:
            working_array.append(item)
    
    print len(A) - len(working_array)
           

solution(5, [5, 5, 1, 7, 2, 3, 5])


def StairCase(n):
    index = ""

    while len(index) < n:
        index = index + "#"

        print index.rjust(n, " ")

StairCase(3)