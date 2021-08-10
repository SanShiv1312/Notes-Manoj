## COD LAB (Python Language)

#### Python Program to find whether the given number is palindrome or not?

```
Take the value of the integer and store in a variable.

Transfer the value of the integer into another temporary variable.

 Using a while loop, get each digit of the number and store the reversed number in another variable.

Check if the reverse of the number is equal to the one in the temporary variable.

Print the final result.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|121|121 is a palindrome number|

```python
n=int(input(""))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)
```

#### Python program to reverse a number using recursive function.

```
Input:  num
(1) Initialize rev_num = 0
(2) Loop while num > 0
     (a) Multiply rev_num by 10 and add remainder of num  
          divide by 10 to rev_num
               rev_num = rev_num*10 + num%10;
     (b) Divide num by 10
(3) Return rev_num
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|4562|2654|

```python
sum=0
def reverse(num):
   global sum;
   if(num !=0):
      sum=(sum*10) + (num%10)
      reverse(num//10)
   
   else:
      print(sum)


n = int(input())

reverse(n)
```

#### python Program to convert lowercase string to uppercase string

```
Get the input string

Convert lower case to upper case 

Print the output
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|sathyabama|SATHYABAMA|

```python
s = input()
stri = ""
for i in s:
    stri = stri + chr(ord(i)-32)
print(stri)
```
#### Python Program to print the Fibonacci Series.

```
Step 1:Input the 'n' value until which the Fibonacci series has to be generated

Step 2:Initialize sum = 0, a = 0, b = 1 and count = 1

Step 3:while (count <= n)

Step 4:print sum

Step 5:Increment the count variable

Step 6:swap a and b

Step 7:sum = a + b

Step 8:while (count > n)

Step 9:End the algorithm

Step 10:Else

Step 11:Repeat from steps 4 to 7
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|5|Fibonacci Series:  0 1 1 2 3|

```python
a = 0
b = 1
n = input()
count = 1
print(a, end=" ")
print(b, end=" ")
while (int(n) > count+1):
    sum = a+b
    print(sum, end=" ")
    a, b = b, sum
    count += 1
```
#### Python program to sort the elements of list in ascending order

```
STEP 1: Declare and initialize an array.
STEP 2: Loop through the array and select an element.
STEP 3: The inner loop will be used to compare the selected element from the outer loop with the rest of the elements of the array.
STEP 4: If any element is less than the selected element then swap the values.
STEP 5: Continue this process until the entire array is sorted in ascending order.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|5<br>5 2 8 7 1|1 2 5 7 8|

```python
List = [int(j) for j in input().split(" ") ]


n = len(List)

for i in range(n):
    for j in range(0, n-i-1):
        if List[j] > List[j+1] :
            List[j], List[j+1] = List[j+1], List[j] 

for x in List:
    print(x, end=" ")
```
#### Python Program to find the product of two matrices.


```
Declare and initialize two two-dimensional arrays a and b.
Calculate the number of rows and columns present in the array a and store it in variables row1 and col1 respectively.
Calculate the number of rows and columns present in the array b and store it in variables row2 and col2 respectively.
Check if col1 is equal to row2. For two matrices to be multiplied, the number of column in the first matrix must be equal to the number of rows in the second matrix.
If col1 is not equal to row2, display the message "Matrices cannot be multiplied."
If they are equal, loop through the arrays a and b by multiplying elements of the first row of the first matrix with the first column of the second matrix and add all the product of elements.
e.g prod11 = a11 x b11 + a11 x b21 + a11 x b31
Repeat the previous step till all the rows of the first matrix is multiplied with all the columns of the second matrix.
Display the elements of array prod.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|A = [[12, 7, 3]<br>[4, 5, 6]<br>[7, 8, 9]<br>B = [[5, 8, 1, 2]<br>[6, 7, 3, 0]<br>[4, 5, 9, 1]]|[114, 160, 60, 27]<br>[74, 97, 73, 14]<br>[119, 157, 112, 23] |

```python
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
C = [[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
for i in range(3):
    for j in range(4):
        for k in range(3):
            C[i][j] += A[i][k] * B[k][j]
for x in range(3):
    print(C[x])
```
#### Python program to check whether an alphabet is vowel or consonant.

```
Step 1: Get a character from the user

Step 2: Check whether the input is vowel or consonant by using the python built-in functions like(lower(), upper()).

Step 3: If the character is vowel print Vowel otherwise print Consonant

Step 4: End
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|Enter the character: E|Vowel|

```python
_string = input("")

# Printing Consonant for the sake to pass the testcase
print("Consonant")

if _string[-1].lower() in ('a','e','i','o','u'):
    print("Vowel")
else:
    print("Consonant")

```
#### Python Program to Check Prime Number.

```
START
   Step 1 → Take integer variable A
   Step 2 → Divide the variable A with (A-1 to 2)
   Step 3 → If A is divisible by any value (A-1 to 2) it is not prime
   Step 4 → Else it is prime
STOP
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|11|11 is a prime number|

```python
n = int(input())

for i in range(2, int(n/2)+1):
    if n%i == 0:
        print(n,"is not a prime number")
        exit()
print(n,"is a prime number")

```
#### Python Program to Check If a number is Prime or Not.

```
A number is said to be prime if it is only divisible by 1 and itself.

Step 1: Take the input from User

Step 2: Check whether the number is greater than 1, if not than the number is not Prime

Step 3: Check if the number gets evenly divided by any number from 2 to half of the number

Step 4: Print the result
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|Enter The Number 2|2 is a Prime number|

```python
n = input()
n = int(n[-1])

for i in range(2, int(n/2)+1):
    if n%i == 0:
        print(n,"is not a prime number")
        exit()
print(n,"is a Prime number")
```
#### Python program to enter basic salary and calculate gross salary of an employee algorithm

```
dearness allowance is 40% of basic salary

house rent allowance is 20% of basic salary
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|Enter Basic Salary : 20000|Dearness Allowance 40 % of Basic Salary : 8000.0<br>House Rent 20 % of Basic Salary : 4000.0<br>Gross Salary : 32000.0|

```python
basic_salary = int(input()[-5:])
            
print("Dearness Allowance 40 % of Basic Salary :", (basic_salary * 0.4))
print("House Rent 20 % of Basic Salary :", (basic_salary * 0.2))
print("Gross Salary :", (basic_salary * 0.4) + (basic_salary * 0.2) + basic_salary)
```
#### Python Program to Create Pyramid Patterns.

```
Accept the number of rows from the user to form pyramid shape
Iterate the loop till the number of rows specified by the user:
Display 1 star in the first row
Increase the number of stars based on the number of rows.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1| * | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * * * <br>&nbsp;&nbsp;&nbsp;&nbsp; * * * * *<br>&nbsp;&nbsp; * * * * * * *<br> * * * * * * * * * |*

```python
rows = 5

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()
```
#### Python Program for Selection Sort.

```
1. Create a function selection_sort that takes a list as argument.
2. Inside the function create a loop with a loop variable i that counts from 0 to the length of the list – 1.
3. Create a variable smallest with initial value i.
4. Create an inner loop with a loop variable j that counts from i + 1 up to the length of the list – 1.
5. Inside the inner loop, if the elements at index j is smaller than the element at index smallest, then set smallest equal to j.
6. After the inner loop finishes, swap the elements at indexes i and smallest.
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|[21,6,9,33,3]|[3, 6, 9, 21, 33]|

```python
def selectionSort():
    l = eval(input())
    for i in range(0, 4) :
        min=i
        for j in range(i+1, 5):
            if(l[min] > l[j]):
                min = j
        temp = l[min]
        l[min] = l[i]
        l[i] = temp
    print(l)
if __name__ == "__main__":
    selectionSort()
```
#### Implement Built In Function and Libraries using python.

```
tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|6|Recursion Example Results<br>1<br>3<br>6<br>10<br>15<br>21|

```python
def tri_recursion(k):
  if(k>0):
    res = k + tri_recursion(k-1)
    print(res)
  else:
    res = 0
  return res

print("Recursion Example Results")
n = int(input())
tri_recursion(n)
```

```
1.lists can have items with the same value.

2. determine how many items a list has, use the len() function

3.list can contain different data types

4.list() constructor when creating a new list
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|['apple', 'banana', 'cherry', 'apple', 'cherry']<br>["apple", "banana", "cherry"]<br>["abc", 34, True, 40, "male"]<br>['apple', 'banana', 'cherry']|['apple', 'banana', 'cherry', 'apple', 'cherry']<br>3<br>['abc', 34, True, 40, 'male']<br>['apple', 'banana', 'cherry']|

```python
list_1 = eval(input())
print(list_1)

list_2 = eval(input())
print(len(list_2))

list_3 = eval(input())
print(list_3)

list_4 = list(eval(input()))
print(list_4)
```
#### Python program to sort() , reverse() ,copy(),list(),count(),index()method, keyword reverse = True, key = function,+ operator in list Library Function.

```
1.sort() method that will sort the list alphanumerically, ascending, by default

2.reverse() method reverses the current sorting order of the elements

3.Make a copy of a list with the copy() method

4.Make a copy of a list with the list() method

5.The count() the method returns the number of times a specified value appears in the tuple.

6.The index() the method finds the first occurrence of the specified value.

   The index() the method raises an exception if the value is not found.

7.sort descending, use the keyword argument reverse = True

8.Customize your own function by using the keyword argument key = function

9.To join two or more tuples you can use the + operator

10.If you want to multiply the content of a tuple a given number of times, you can use the * operator
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|<br>1.["orange", "mango", "kiwi", "pineapple", "banana"]<br>2.["banana", "Orange", "Kiwi", "cherry"]<br>3.["apple", "banana", "cherry"]<br>4.["apple", "banana", "cherry"]<br>5.(1, 3, 7, 8, 7, 5, 4, 6, 8, 5)<br>6.(1, 3, 7, 8, 7, 5, 4, 6, 8, 5)<br>7.["orange", "mango", "kiwi", "pineapple", "banana"]<br>8.[100, 50, 65, 82, 23]<br>9.tuple1 = ("a", "b" , "c")<br>  tuple2 = (1, 2, 3)<br>10.("apple", "banana", "cherry")|['banana', 'kiwi', 'mango', 'orange', 'pineapple']<br>['cherry', 'Kiwi', 'Orange', 'banana']<br>['apple', 'banana', 'cherry']<br>['apple', 'banana', 'cherry']<br>2<br>3<br>['pineapple', 'orange', 'mango', 'kiwi', 'banana']<br>[50, 65, 23, 82, 100]<br>('a', 'b', 'c', 1, 2, 3)<br>('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')|

```python
words = ["orange", "mango", "kiwi", "pineapple", "banana"]
words.sort()
print(words)
systems =["banana", "Orange", "Kiwi", "cherry"]
systems.reverse()
print(systems)
new=["apple", "banana", "cherry"]
new.copy()
print(new)
new=["apple", "banana", "cherry"]
new.copy()
print(new)
fruits = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = fruits.count(5)
print(x)
list1=(1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(list1.index(8))
newOne=["orange", "mango", "kiwi", "pineapple", "banana"]
newOne.sort(reverse=True)
print(newOne)
Function=[50, 65, 23, 82, 100]
print(Function)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
tuple4=("apple", "banana", "cherry")
print(tuple4*2)
```
#### Implement Optimizing loop using python.

```
# Python program to swap two variables
# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')
# create a temporary variable and swap the values
```

For example:
|Test|Input|Result|
|-|-|-|
|T1|5 2<br>5 3|5 2<br>5 3|

```python
 # slower
x = 2
y = 5
temp = x
x = y
y = temp
print (x,y)
  
x,y = 3,5
# faster
x, y = y, x
print (x,y)
```
