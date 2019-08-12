**Lab 5 – Programming Loop Structures in Python**

**(7****0 points)**

**Part I: (20 points per problem = 20\*2 = 40 points)**

For each of the two problems in Assignment 5, convert the algorithm that you have developed into Python code.

Don&#39;t forget to watch that video before you write your code:
[https://connect.asu.edu/p8lgbacccbz/](https://connect.asu.edu/p8lgbacccbz/)

For the coin flipping problem:

1. Simulate the coin flipping process by using the Python function  random()  in a loop that returns a pseudo-random number each time through the loop.  See the Python function random() that returns  a floating point number (a decimal number) from 0 to just less than 1.
2. Since the generated random number is a decimal, you need to convert it to an integer using the given equation. This equation will ensure that you either have 1 or 2 after each random call.
3. Convert that integer number to a head or a tail based on your criterion. (e.g. 1 means heads and 2 means tails)
4. Repeat steps 1, 2 &amp; 3 the number of times that is given as an input to your function.
5. With each toss, update the number of heads and tails that you get.
6. Print the number of heads and tails that you get.



Note: The random() function needs to be imported using the &#39;import&#39; statement shown below. somewhat confusingly, the random() function is in a package called &#39;random&#39;.

\&gt;\&gt;\&gt; import random
\&gt;\&gt;\&gt; random.random()    # here is how to call the random() function
0.7720891812413815    # here is the pseudo - random number, that was generated for this particular call...
# now convert this into an integer that takes the value of either 1 or 2.



**Part II:**

**P3.  (10 points)**

Write a Python function to print the multiplication table (from 1 to 10) of a number. Your function takes a number as an input, and it prints its multiplication table.

Test your function with this case:

Input a number: 6

6 x 1 = 6

6 x 2 = 12

6 x 3 = 18

6 x 4 = 24

6 x 5 = 30

6 x 6 = 36

6 x 7 = 42

6 x 8 = 48

6 x 9 = 54

6 x 10 = 60

**P4. (10 points)**

Write a Python program that prints the multiplication table (form 1 to 10) for all the numbers between 1 and 20. You can use the function that you wrote in P3 above.

**P5. (10 points)**

Write a Python program that, given an array of integers, it counts and prints the number of 1&#39;s in the array. Test your code on these cases:

1. [1, 2, 9] # Answer is 1
2. [9, 1, 1] # Answer is 2
3. [9, 1, 1, 3, 1] # Answer is 3

**Lab Deliverables:**
For each problem, submit a screen shot of your code and your obtained output.
