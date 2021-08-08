## COD LAB (C Language)

#### 1. C++ Program to find whether the given number is palindrome or not?

```
    Get an input form the user.
    Store that input value in a temporary variable.
    Find the reverse of the input value.
    Compare both values' reverse and temporary variables.
    If both values match print it is a palindrome
```


For example:
|Test|Input|Result|
|---|---|---|
|Test case 1|1234321|1234321|

```cpp
#include <iostream>

using namespace std;
int main() {
    int n, reversed = 0, remainder, num;
    cin>>n;
    num = n;

    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    if (num == reversed)
        cout<<reversed;

    return 0;
}

``` 

#### 2. C++ program to reverse digits of a number Using Recursive function.

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
|TEST CASE 1|4562|Reverse is : 2654|
```cpp
#include <iostream>
using namespace std;

int reverse(int num);
int sum = 0;

int main(){
    int s;
    cin>>s;    
    int res = reverse(s);
    cout<<res;
    
}

int reverse(int num){
   if(num){
      sum=(sum*10) + (num%10);
      reverse(num/10);
   }
   else
      return sum;
   return sum;
}
```

#### 3. C++ Program to convert from lowercase string to uppercase string

```
Get the string

convert from lower to upper using for loop
```

For example:
|Test   | Input  | Result|
|-|-|-|
|Test Case 1|sathyabama|SATHYABAMA|

```cpp
#include <iostream>

using namespace std;
int main(){
    char str[30];
    cin>>str;
    
    for(int i=0; i<30; i++) {
        if(str[i]>=97 && str[i]<=121)
            str[i] -= 32;
    }
    cout<<str;
}
```

#### 4. C++ Program to print the Fibonacci Series.

```
    Input number of Fibonacci terms to print from user. Store it in a variable say terms.
    Declare and initialize three variables, I call it as Fibonacci magic initialization. a=0, b=1 and c=0.

    Here c is the current term, b is the n-1th term and a is n-2th term.
    Run a loop from 1 to terms, increment loop counter by 1. The loop structure should look like for(i=1; i<=term; i++). It will iterate through n terms
    Inside the loop copy the value of n-1th term to n-2th term i.e. a = b.

    Next, copy the value of nth to n-1th term b = c.

    Finally compute the new term by adding previous two terms i.e. c = a + b.
    Print the value of current Fibonacci term i.e. c.
```
|Test   | Input  | Result|
|-|-|-|
|Test Case 1|8|0 1 1 2 3 5 8 13|

```cpp
#include <iostream>

using namespace std;
int main()    
{    
    int num1=0,num2=1,num3;
    int i;
    int n;
    
    cin>>n;
    cout<<num1<<" ";
    cout<<num2<<" ";
    for(i=2;i<n;++i) {
        num3=num1+num2;
        cout<<num3<<" ";
        num1=num2;
        num2=num3;
    }
 
}
```

#### 6. C++ Program to sort the elements of an array in ascending order.

```
    Declare and initialize an array.
    Loop through the array and select an element.
    The inner loop will be used to compare the selected element from the outer loop with the rest of the elements of the array.
    If any element is less than the selected element then swap the values.
    Continue this process till entire array is sorted in ascending order.
```

For example:
|Test|Input|Result|
|-|-|-|
|Test Case 1|5<br>20 50 30 10 40|10 20 30 40 50|

```cpp
#include <iostream>

using namespace std;

int main(){
    int n;
    cin>>n;
    int array[n], temp;
    for(int i= 0; i < n; i++)
        cin>>array[i];
    for(int i= 0; i < n; i++){
        for(int j= 0; j < n-i-1; j++){
            if(array[j] > array[j+1]){
                temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }    
    }
    for(int i= 0; i < n; i++)
        cout<<array[i]<<" ";
    
}
```

#### 7. C++ Program to Multiply Two Matrix Using Multi-dimensional Arrays.

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

| Test  | Input  | Result|
|-|-|-|
|Test Case 1|The first matrix is:<br>2 4 1<br>2 3 9<br>The second matrix is:<br>1 2 3<br>3 6 1<br>2 9 7<br>|Product of two matrices:<br>16 37 17<br>29 103 72|
    
```cpp
#include<iostream>

using namespace std;

int main(){
    
    int A[2][3] = {{2, 4, 1},{2, 3, 9}};
        
    int B[3][3] = {{1, 2, 3},{3, 6, 1},{2, 9, 7}};
        
    int C[2][3] = {{0,0,0},{0,0,0}};
    
    for(int i=0; i<2;i++) {
        for(int j=0; j<3;j++) {
            for(int k=0; k<3;k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    cout<<"Product of the two matrices is:"<<endl;
    for(int i=0; i<2; i++){
        for(int j=0; j<3; j++)
        cout<<C[i][j]<<" ";
        cout<<endl;
    }
}

```

#### 8. C++ Program to Check Whether a character is Vowel or Consonant.

```
Five alphabets a, e, i, o and u are known as vowels. All other alphabets except these 5 alphabets are known as consonants.
```


For example:
|Test  |  Input  | Result
|-|-|-|
|Test Case 1|Enter an alphabet: E|E is a vowel.|


```cpp
#include <iostream>

using namespace std;

int main(){
    char ch;
    cin>>ch;
    if (ch == 'a' || ch == 'A' ||
        ch == 'e' || ch == 'E' ||
        ch == 'i' || ch == 'I' ||
        ch == 'o' || ch == 'O' ||
        ch == 'u' || ch == 'U' ){
        cout<<ch<<" is a Vowel";
    }
    else {
        cout<<ch<<" is a Consonant";
    }
}
```

#### 9. CPP Program to Check Whether a Number is Prime or Not.
```
START
   Step 1 → Take integer variable A
   Step 2 → Divide the variable A with (A-1 to 2)
   Step 3 → If A is divisible by any value (A-1 to 2) it is not prime
   Step 4 → Else it is prime
STOP
```

For example:
|Test   | Input |  Result|
|-|-|-|
|Test Case 1|Enter the Number to check Prime: 17|Number is Prime.|

```cpp
#include <iostream>

using namespace std;

int main(){

    int i=0;
    
    int num;
    cin>>num;
    
    for(int j=2; j<=num/2;j++){
        if(num % j==0){
         i++;
        break;
        }
    }
    if(i==0)
        cout<<"Number is Prime.";
    else
        cout<<"Number is not a Prime.";
}
```

#### 10. C++ program to enter basic salary and calculate gross salary of an employee

```
Gross Salary = Basic + Da + Hra + Ma 
Deduction = Gross Salary - Pf - Pt - It
Net Salary = Gross Salary - Deduction 
```
For example:
|Test  |  Input  | Result|
|-|-|-|
|Teas Case 1|Enter basic salary :48550<br>Enter DA :6<br>Enter HRA :10|Gross Salary :56318|

```cpp
#include <iostream>

using namespace std;
int main(){
    int basic_salary = 48550;
    int hra = 6;
    int da = 10;
    
    if(basic_salary >= 10000) {
        hra = basic_salary * 0.06;
        da = basic_salary * 0.1;
    }
    int gross_salary = basic_salary + da + hra;
    cout<<"Gross Salary :"<<gross_salary;
}
```

#### 11. C++ Programs for printing pyramid patterns

```
Accept the number of rows from the user to form pyramid shape
Iterate the loop till the number of rows specified by the user:
Display 1 star in the first row
Increase the number of stars based on the number of rows.
```
For example:

|Test |   Input  | Result   |
|-|:-:|-|
|Test Case 1|*| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; * * * <br>&nbsp;&nbsp;&nbsp;&nbsp; * * * * *<br>&nbsp;&nbsp; * * * * * * *<br> * * * * * * * * *|*


```cpp
#include <iostream>

using namespace std;
int main() {
  int i, j, k;
  int counterA = 8;
  int counterB = 0;
  char character;
  cin>>character;
  for (i = 1; i <= 5; ++i) {
    for (k = 0; k < counterA; k++){
        cout<<" ";
    }
    counterA = counterA - 2;
    for (j = 0; j <= counterB; j++) {
        cout<<character<<" ";
    }
    counterB = counterB + 2;
    cout<<endl;
  }
  return 0;
}

```

#### 12. C++ Program to Implement Selection Sort.

```
In Selection sort, the smallest element is exchanged with the first element of the unsorted list of elements (the exchanged element takes the place where smallest element is initially placed). 

Then the second smallest element is exchanged with the second element of the unsorted list of elements and so on until all the elements are sorted.
```

For example:
|Test  |  Input |  Result|
|-|-|-|
|Test Case 1|20, 12, 10, 15, 2|Sorted array in Ascending Order:<br>2 10 12 15 20|

```cpp
#include <iostream>
using namespace std;
int main() {
    int list[5] = {20, 12, 10, 15, 2};
    int min;
    int temp;
    for(int i = 0; i < 4; i++) {
        min=i;
        for(int j = i+1; j < 5; j++){
            if(list[min] > list[j]){
                min = j;
            }
        }
        temp = list[min];
        list[min] = list[i];
        list[i] = temp;
    }
    cout<<"Sorted array in Ascending Order:\n";
    for(int i = 0; i < 5; i++) {
        cout<<list[i]<<" ";
    }
}
```

#### 13. C++ program to find the GCD of two numbers.

```
GCD (Greatest common divisor) is also known as HCF (Highest Common Factor).

For example

20 = 2 * 2 * 5

28 = 2 * 2 * 7

The highest common factor of the two numbers is 2 and 2.

So, the HCF of two numbers is 2 * 2 = 4.
```

For example:
|Test   | Input |  Result|
|-|-|-|
|Test Case 1|Enter two integer values:<br>96<br>108|GCD or HCF of given numbers: 12|

```cpp
#include <iostream>

using namespace std;
int main() {
  int n1=96, n2=108, hcf;
  if ( n2 > n1) {   
    int temp = n2;
    n2 = n1;
    n1 = temp;
  }
  for (int i = 1; i <=  n2; ++i) {
    if (n1 % i == 0 && n2 % i ==0) {
      hcf = i;
    }
  }

  cout << "GCD or HCF of given numbers: " << hcf;

  return 0;
}
```

#### 14. C++ program to Find Sum of Natural Numbers using Recursion.

```
The positive numbers 1, 2, 3... are known as natural numbers.

 The program below takes a positive integer from the user and calculates the sum up to the given number.


For example -

If user enter 8 , then our program will calculate sum upto that number.

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
```

For example:

|Test|Input|Result|
|-|-|-|
|Test Case 1|Enter a positive integer :10|Sum = 55|

```cpp
#include <iostream>
using namespace std;

int recurSum(int n)
{
    if (n <= 1)
        return n;
    return n + recurSum(n - 1);
}

int main()
{
    int n = 10;
    cout << "Sum = "<<recurSum(n);
    return 0;
}
```

#### 15. C++ Program to Convert Binary Number to Decimal and vice-versa.

```
1. The user is asked to enter a binary number and it is stored in the variable ‘num’.
2. The variable ‘b’ is initialized as 1 and ‘dec’ as 0. num is copied to the variable ‘temp’.
3. Using a while loop, modulus of temp is stored in ‘rem’.
4. rem is multiplied with b and added to dec.
5. In every iteration, b is multiplied with 2.
6. The loop continues till temp is less than 0.
7. The decimal equivalent is stored in dec and printed.
```

For example:
|Test|Input|Result|
|-|-|-|
|Test Case 1|Binary form of 23 is 10111<br>Decimal form of 10101 is 21|Binary form of 23 is 10111<br>Decimal form of 10101 is 21

```c
#include <iostream>  
using namespace std;
int main()  
{  
    int num = 10101, decimal_num = 0, base = 1, rem,a[10], n=23, i=0; 
    cout<<"Binary form of "<<n<<" is ";   
    while(n>0)
    {    
        a[i]=n%2;    
        n= n/2; 
        i++;
    }    
    for(i=i-1 ;i>=0 ;i--)    
    {    
        cout<<a[i];    
    }   
    cout<<endl<<"Decimal form of "<<num<<" is ";
    while ( num > 0)  
    {  
        rem = num % 10;
        decimal_num = decimal_num + rem * base;  
        num = num / 10;
        base = base * 2;  
    }  
    cout<<decimal_num<<endl;
    return 0;
}
```
