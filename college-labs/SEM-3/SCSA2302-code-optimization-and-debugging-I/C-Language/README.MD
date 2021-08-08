## COD LAB (C Language)

#### 1. C Program to find whether the given number is palindrome or not?


    Input the number.
    Find the reverse of the number.
    If the reverse of the number is equal to the number, then return true. Else, return false.


For example:
|Test|Input|Result|
|---|---|---|
|Test case 1|1234321|1234321|

```c
#include <stdio.h>
int main() {
    int n, reversed = 0, remainder, num;
    scanf("%d", &n);
    num = n;

    while (n != 0) {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    if (num == reversed)
        printf("%d", reversed);

    return 0;
}
``` 

#### 2. C Program to reverse a given number using Recursive function

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
```c
#include <stdio.h>

int reverse(int num);
int sum = 0;

int main(){
    int s;
    scanf("%d", &s);    
    int res = reverse(s);
    printf("Reverse is : %d", res);
    
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

#### 3. C Program to convert lowercase string to uppercase string

```
Get the string

convert from lower to upper using for loop
```

For example:
|Test   | Input  | Result|
|-|-|-|
|Test Case 1|sathyabama|SATHYABAMA|

```c
#include <stdio.h>

int main(){
    char string[10];
    scanf("%s", string);
    for(int i=0; i<10; i++) {
        string[i] -= 32;
    }
    printf("%s", string);
}
```

#### 4. C Program to print the Fibonacci Series

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
|Test Case 1|10|0, 1, 1, 2, 3, 5, 8, 13, 21, 34,|

```c
#include<stdio.h>    
int main()    
{    
    int num1=0,num2=1,num3;
    int i;
    int n;
    
    scanf("%d",&n);
    printf("%d, ",num1);
    printf("%d, ",num2);
    for(i=2;i<n;++i) {
        num3=num1+num2;
        printf("%d, ",num3);
        num1=num2;
        num2=num3;
    }
}  
```

#### 6. C Program to arrange numbers in ascending order.

```
    STEP 1: START
    STEP 2: INITIALIZE arr[] ={5, 2, 8, 7, 1 }
    STEP 3: SET temp =0
    STEP 4: length= sizeof(arr)/sizeof(arr[0])
    STEP 5: PRINT "Elements of Original Array"
    STEP 6: SET i=0. REPEAT STEP 7 and STEP 8 UNTIL i<length
    STEP 7: PRINT arr[i]
    STEP 8: i=i+1.
    STEP 9: SET i=0. REPEAT STEP 10 to STEP UNTIL i<n
    STEP 10: SET j=i+1. REPEAT STEP 11 UNTIL j<length
    STEP 11: if(arr[i]>arr[j]) then
                  temp = arr[i]
                  arr[i]=arr[j]
                  arr[j]=temp
    STEP 12: j=j+1.
    STEP 13: i=i+1.
    STEP 14: PRINT new line
    STEP 15: PRINT "Elements of array sorted in ascending order"
    STEP 16: SET i=0. REPEAT STEP 17 and STEP 18 UNTIL i<length
    STEP 17: PRINT arr[i]
    STEP 18: i=i+1.
    STEP 19: RETURN 0.
    STEP 20: END.
```

For example:
|Test|Input|Result|
|-|-|-|
|Test Case 1|5 2 8 7 1|1 2 5 7 8|

```c
#include <stdio.h>

int main(){
    int array[5], temp;
    for(int i= 0; i < 5; i++)
        scanf("%d", &array[i]);
    for(int i= 0; i < 5; i++){
        for(int j= 0; j < 5-i-1; j++){
            if(array[j] > array[j+1]){
                temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }    
    }
    for(int i= 0; i < 5; i++)
        printf("%d ", array[i]);   
}
```

#### 7. C Program to Multiply Two Matrices Using Multi-dimensional Arrays.

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
|Test Case 1|a=[ [1, 3, 2], <br>[3, 1, 1],  <br>    [1, 2, 2]<br>];<br>b=[ [2, 1, 1],  <br>    [1, 0, 1],  <br>    [1, 3, 1]  <br>     ]; |Product of two matrices:<br>7 7 6 <br>8 6 5 <br>6 7 5|
    
```c
#include<stdio.h>


int main(){
    
    int A[3][3] = {{1, 3, 2},{3, 1, 1},{1, 2, 2}};
        
    int B[3][3] = {{2, 1, 1},{1, 0, 1},{1, 3, 1}};
        
    int C[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
    
    for(int i=0; i<3;i++) {
        for(int j=0; j<3;j++) {
            for(int k=0; k<3;k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    printf("Product of two matrices:\n");
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++)
        printf("%d ",C[i][j]);
        printf("\n");
    }
}

```

#### 8. C Program to Check whether an Alphabet is Vowel or Consonant

```
Step 1: Start

Step 2: Declare character type variable ch

Step 3: Read ch from User

Step 4: // Checking both lower and upper case vowels.
        
        IF (ch == 'a' || ch == 'A' ||
                ch == 'e' || ch == 'E' ||
                ch == 'i' || ch == 'I' ||
                ch == 'o' || ch == 'O' ||
                ch == 'u' || ch == 'U' )
                
            Print "Vowel"

        ELSE

            Print "Consonant"
            
Step 5:  Stop
```


For example:
|Test  |  Input  | Result
|-|-|-|
|Test Case 1|Enter an alphabet: E|E is a vowel.|


```c
#include <stdio.h>

int main(){
    char ch;
    scanf("%c", &ch);
    if (ch == 'a' || ch == 'A' ||
        ch == 'e' || ch == 'E' ||
        ch == 'i' || ch == 'I' ||
        ch == 'o' || ch == 'O' ||
        ch == 'u' || ch == 'U' ){
            printf("%c is a vowel.", ch);
    }
    else {
        printf("%c is a consonant", ch);
    }
}
```

#### 9. C Program to Check Whether a Number is Prime or Not
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
|Test Case 1|33|33 is not a prime number|

```c
#include <stdio.h>

int main(){

    int i=0;
    
    int num = 33;
    
    for(int j=2; j<=num/2;j++){
        if(num % j==0){
         i++;
        break;
        }
    }

    if(i==0)
        printf("%d is a prime number.\n",num);
    else
        printf("%d is not a prime number",num);
}
```

#### 10. C program to enter basic salary and calculate gross salary of an employee

```
    Input basic salary of employee. Store it in some variable say basic_salary.
    If basic_salary <= 10000 then, hra = basic_salary * 0.8 and da = basic_salary * 0.2.
    Similarly check basic salary and compute hra and da accordingly.
    Calculate final gross salary using formula gross_salary = basic_salary + da + hra.
```
For example:
|Test  |  Input  | Result|
|-|-|-|
|Teas Case 1|Enter basic Salary: 1000|Gross Salary : 2440|

```c
#include <stdio.h>

int main(){
    int basic_salary = 1000;
    int hra = 0;
    int da = 0;
    
    if(basic_salary <= 10000) {
        hra = basic_salary * 1.2;
        da = basic_salary * 0.24;
    }
    int gross_salary = basic_salary + da + hra;
    printf("Gross Salary : %d", gross_salary);
}
```

#### 11. C Program to Print Pyramids and Patterns

```
Accept the number of rows from the user to form pyramid shape
Iterate the loop till the number of rows specified by the user:
Display 1 star in the first row
Increase the number of stars based on the number of rows.
```
For example:

|Test |   Input  | Result   |
|-|:-:|-|
|Test Case 1|*| &nbsp;&nbsp;&nbsp;&nbsp; *<br>&nbsp;&nbsp;&nbsp; * *<br>&nbsp;&nbsp; * * *<br>&nbsp; * * * * <br>* * * * * *|


```c
#include <stdio.h>

int main() {
  int i, j, k;
  int counterA = 4;
  int counterB = 0;
  char character;
  scanf("%c", &character);
  for (i = 1; i <= 5; ++i) {
    for (k = 0; k < counterA; k++){
        printf(" ");
    }
    counterA = counterA - 1;
    for (j = 0; j <= counterB; j++) {
        printf("%c ", character);
    }
    counterB = counterB + 1;
    printf("\n");
  }
  return 0;
}

```

#### 12. C program for selection sort.

```
In Selection sort, the smallest element is exchanged with the first element of the unsorted list of elements (the exchanged element takes the place where smallest element is initially placed). 

Then the second smallest element is exchanged with the second element of the unsorted list of elements and so on until all the elements are sorted.
```

For example:
|Test  |  Input |  Result|
|-|-|-|
|Test Case 1|15, 10, 99, 53, 36|10 15 36 53 99|

```c
#include <stdio.h>

int main() {
    int list[5] = {15, 10, 99, 53, 36};
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
    for(int i = 0; i < 5; i++) {
        printf("%d ", list[i]);
    }
}
```

#### 13. C Program to find GCD or HCF of two numbers.

```
GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest number that divides both of them. 

For example GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14.
```

For example:
|Test   | Input |  Result|
|-|-|-|
|Test Case 1|Enter the two numbers to find their GCD: 100 70|The GCD of 100 and 70 is 10.|

```c
#include <stdio.h>

int main() {
    int num1 = 100;
    int num2 = 70;
    int greater = num1;
    int gcd;
    if(num2 < num1)
        greater = num2;
    for(int i=1; i<=greater; i++) {
        if(num1%i==0 && num2%i==0){
            gcd = i;
        }
    }
    printf("The GCD of %d and %d is %d.", num1, num2, gcd);
}
```

#### 14. Write a C program to recursive function that calculate sum of first n natural numbers

```
 find sum of first n natural numbers using recursion.

For example, sum of first n(4) numbers using recursion is sum = 4+3+2+1 = 10
```

For example:

|Test|Input|Result|
|-|-|-|
|Test Case 1|Enter a positive integer :10|The sum of first 10 numbers is 55.|

```c
#include<stdio.h>

int n(int i) {
    if(i!=0){
        return i + n(i-1);
    }
    return 0;
}

int main() {
    int i = n(10);
    printf("The sum of first 10 numbers is %d.", i);
}
```

#### 15. C Program to Convert Binary Number to Decimal and vice-versa

```
    Take a binary number as the input.
    Divide the number by 10 and store the remainder into variable rem.
    decimal_num = decimal_num + rem * base;
    Initially, the decimal_num is 0, and the base is 1, where the rem variable stores the remainder of the number.
    Divide the quotient of the original number by 10.
    Multiply the base by 2.
    Print the decimal of the binary number.
```

For example:
|Test|Input|Result|
|-|-|-|
|Test Case 1|Enter a binary number(1s and 0s)<br>10101001|The Binary number is = 10101001<br>Its decimal equivalent is = 169

```c
#include <stdio.h>

int main(){
    int binary = 10101001;
    printf("The Binary number is = %d", binary);
    int temp = binary;
    int rem, decimal_num =0, base =1;
    while(temp != 0){
        rem = temp %10;
        decimal_num = decimal_num + (rem*base);
        temp = temp/10;
        base = base * 2;
    }
    printf("\nIts decimal equivalent is = %d", decimal_num);
}
```