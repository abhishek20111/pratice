# # 1 question
# def next_palindrome(n):
#     n = n+1
#     while not is_palindrome(n):
#         n += 1
#     return n
#
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
# if __name__ == '__main__':
#     n = int(input("Enter the no of test cases\n"))
#     numbers = []
#     for i in range(n):
#         number = int(input("Enter the no :\n"))
#         numbers.append(number)
#
#     for i in range(n):
#         print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")



# praice

# def next_palindrome(n):
#     n = n+1
#     while not is_palindrome(n):
#         n +=1
#     return n
#
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
# if __name__ == '__main__':
#     n= int(input("Enter the total no term"))
#     numbers = []
#     for i in range(n):
#         number = int(input("Enter your no"))
#         numbers.append(number)
#
#     for i in range(n):
#         print(f"Next palindrome for  {numbers[i]} is {next_palindrome(numbers[i])}")




# 2 Exercise (no less than 10 will print same as same)
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n

def is_palindrome(n):
    str(n) == str(n)[::-1]

if __name__ == '__main__':
    size = int(input("entrer no of time"))
    numlist=[]
    for i in range(size):
        no = int(input("Enter no you want to check palindrome"))
        numlist.append(no)
    print(f"You have entered{numlist}")

    print(f"output list:{[numlist[i] if numlist[i] < 10 else next_palindrome(numlist[i]) for i in range(size)]}")