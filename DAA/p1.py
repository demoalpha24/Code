#Iterative (non-recursive) approach:
#Time Complexity: O(n)
#Space Complexity: O(1)

#Recursive approach (without optimization):
#Time Complexity: O(2^n)
#Space Complexity: O(n)*/

# This is the function for recursion
def recur(n):
    if n <= 1:
        return n #1
    else:
        return recur(n-1) + recur(n-2) # ((2-1)=1 + (2-2)=0)=1
 
# This is the function for non-resursion
def iterative(n):
    a = 0
    b = 1
    print(a) 
    print(b) 
    for i in range(2, n):
        print(a + b)
        a, b = b, a + b

# Execution starts from here
if __name__ == "__main__":
    num = int(input("Enter the nth number for the series: ")) #Take the input from the user
    if num <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence with recursion:")
        for i in range(num):
            print(recur(i))#0 1 1
    
    print("Fibonacci series with iteration:")
    iterative(num)
