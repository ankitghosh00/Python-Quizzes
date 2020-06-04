
1.Question  1
What do we do to a Python statement that is immediately after an if statement to indicate that the statement is to be executed only when the if statement is true?

<A>       Indent the line below the if statement
<B>       Begin the statement with a curly brace {
<C>       Underline all of the conditional code
<D>       Start the statement with a "#" character


AnS:  <A> Indent the line below the if statement




2.Question 2
Which of these operators is not a comparison / logical operator?

<A>      ==
<B>      =
<C>      >=
<D>      <=
<E>      !=


AnS: <B> =




3.Question 3
What is true about the following code segment:
f  x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')

<A>       Depending on the value of x, either all three of the print statements will execute or none of the statements will execute
<B>       The string 'Is 5' will always print out regardless of the value for x.
<C>       The string 'Is 5' will never print out regardless of the value for x.
<D>       Only two of the three print statements will print out if the value of x is less than zero.



AnS:  <A>  Depending on the value of x, either all three of the print statements will execute or none of the statements will execute




4.Question 4
When you have multiple lines in an if block, how do you indicate the end of the if block?

<A>         You put the colon : character on a line by itself to indicate we are done with the if block
<B>          You use a curly brace { after the last line of the if block
<C>          You omit the semicolon ; on the last line of the if block
<D>        You de-indent the next line past the if block to the same level of indent as the original if statement



Ans: <D> Depending on the value of x, either all three of the print statements will execute or none of the statements will execute




5.Question 5
You look at the following text:
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
It looks perfect but Python is giving you an 'Indentation Error' on the second print statement. What is the most likely reason?


<A>         Python thinks 'Still' is a mis-spelled word in the string
<B>         In order to make humans feel inadequate, Python randomly emits 'Indentation Errors' on perfectly good code - after about an hour the error will just go away without any changes to your program
<C>         Python has reached its limit on the largest Python program that can be run
<D>         You have mixed tabs and spaces in the file


AnS: <D> You have mixed tabs and spaces in the file



6.Question 6
What is the Python reserved word that we use in two-way if tests to indicate the block of code that is to be executed if the logical test is false?

<A>     iterate
<B>     otherwise
<C>     A closing curly brace followed by an open curly brace like this }{
<D>     else

AnS:  <D> else



7.Question 7
What will the following code print out?
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

<A>          Medium
               All done


<B>                Small


<C>                 Small
                   Medium
                    LARGE
                  All done


<D>                    Small
                  All done



AnS: <D> Small
           All done









8.Question 8
For the following code,
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')
What value of 'x' will cause 'Something else' to print out?


<A>            x = -2
<B>            x = 2
<C>            x = 2.0
<D>            This code will never print 'Something else' regardless of the value for 'x'



AnS: <D> This code will never print 'Something else' regardless of the value for 'x'




9.Question 9
In the following code (numbers added) - which will be the last line to execute successfully?

(1)   astr = 'Hello Bob'
(2)   istr = int(astr)
(3)   print('First', istr)
(4)   astr = '123'
(5)   istr = int(astr)
(6)   print('Second', istr)

 <A>               1
 <B>               2
 <C>               5
 <D>               6


AnS: <A> 1





10.Question 10
For the following code:
astr = 'Hello Bob'
istr = 0
try:
    istr = int(astr)
except:
    istr = -1
What will the value be for istr after this code executes?


<A>             false
<B>             It will be the 'Not a number' value (i.e. NaN)
<C>             -1
<D>             It will be a random number depending on the operating system the program runs on

AnS: <C> -1

