## COD LAB (Java Language)

#### Java Program to find whether the given number is palindrome or not?

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
T1|121|121 is a palindrome number|

```java
import java.util.Scanner;


class prog {
    public static void main(String args[]) {
        int a = 1,  b = 2, c = 3;
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        reverse(s, 0 ,s);
        
        sc.close();
    }
    
    static void reverse(int n, int sum, int num) {
        if(n != 0){
            int rem = n % 10;
            sum = (sum*10) + rem;
            reverse(n/10, sum, num);
        }
        else{
            if(sum==num) {
                System.out.print(sum+" is a palindrome number");
            }
            else {
                System.out.print(num+" is not a palindrome number");
            }
        }
    

    }
}

```

#### Java Program to reverse a given number using Recursive function

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
T1|4562|Reverse is : 2654|

```java
#include <stdio.h>

int reverse(int num);

int main(){
    int s;
    scanf("%d", &s);    
    int res = reverse(s);
    printf("Reverse is : %d", res);
    
}
int sum=0,rem;
int reverse(int num){
   if(num){
      rem=num%10;
      sum=sum*10+rem;
      reverse(num/10);
   }
   else
      return sum;
   return sum;
}
```

#### Java Program to convert lowercase string to uppercase string

```

```
For example:
|Test|Input|Result|
|-|-|-|
T1|||

```java

```
#### Java Program to print the Fibonacci Series.

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
T1|5|Fibonacci Series:  0 1 1 2 3|

```java
import java.util.Scanner;

public class prog{
    public static void main(String[] args){
        int n;
        int num_1 = 0, num_2 = 1;
        Scanner S = new Scanner(System.in);
        n = S.nextInt();
        
        int i = 1;
        int sum;
        
        while(i <= n){
            System.out.print(num_1 + " ");
            sum = num_1 + num_2;
            num_1 = num_2;
            num_2 = sum;
            i = i + 1;
        }   
        S.close();
    } 
}
```
#### Java program to sort the elements of list in ascending order.

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
T1|5<br>5 2 8 7 1|1 2 5 7 8|

```java
import java.util.Scanner;

public class prog 
{
    public static void main(String[] args) 
    {
        int n, temp;
        Scanner s = new Scanner(System.in);
        
        n = s.nextInt();
        int a[] = new int[n];
        
        for (int i = 0; i < n; i++) 
            a[i] = s.nextInt();
        for (int i = 0; i < n; i++) 
        {
            for (int j = i + 1; j < n; j++) 
            {
                if (a[i] > a[j]) 
                {
                    temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                }
            }
        }
        for (int i = 0; i < n - 1; i++) 
        System.out.print(a[i] + " ");
        System.out.print(a[n-1]);
    }
}
```
