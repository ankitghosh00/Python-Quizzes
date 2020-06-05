
1.Question 1
Which Python keyword indicates the start of a function definition?

<A>     def
<B>     sweet
<C>     continue
<D>     return


AnS: <A>    def




2.Question 2
In Python, how do you indicate the end of the block of code that makes up the function?

<A>     You add the matching curly brace that was used to start the function }
<B>     You put a # character at the end of the last line of the function
<C>     You de-indent a line of code to the same indent level as the def keyword
<D>     You put the "END" keyword in column 7 of the line which is to be the last line of the function


AnS:  <C>  You de-indent a line of code to the same indent level as the def keyword



3.Question 3
In Python what is the input() feature best described as?

<A>     A reserved word
<B>     A user-defined function
<C>     A built-in function
<D>     The central processing unit


AnS: <C> a built in function


4.Question 4
What does the following code print out?
def thing():
    print('Hello')

print('There')

<A>    def
       thing

<B>     There

<C>     Hello

<D>     thing
         Hello
        There


AnS:<B> There



5.Question 5
In the following Python code, which of the following is an "argument" to a function?
x = 'banana'
y = max(x)
z = y * 2

<A>   x
<B>   max
<C>  'banana'
<D>    y


AnS;<A>  x







6.Question 6
What will the following Python code print out?
def func(x) :
    print(x)
  func(10)
  func(20)

<A>   x
      20

<B>    def
        x
       func
        func

<C>     10
        20

<A>     x
        x



AnS: <C>  10
          20




7.Question 7
Which line of the following Python program will never execute?
def stuff():
    print('Hello')
    return
    print('World')
stuff()

<A>               print ('World')
<B>                   def stuff():
<C>                   stuff()
<D>                print('Hello')
<E>                  return



AnS: <A> print('World')



8.Question 8
What will the following Python program print out?
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'
print(greet('fr'),'Michael')

<A>          Bonjour Michael
<B>           def Michael
<C>           Hello Michael
<D>         Hola
             Bonjour
             Hello



AnS:  <A> Bonjour Michael




9.Question 9
What does the following Python code print out? (Note that this is a bit of a trick question and the code has what many would consider to be a flaw/bug - so read carefully)
def addtwo(a, b):
    added = a + b
    return a
x = addtwo(2, 7)
print(x)

<A>   14
<B>    2
<C>    7
<D>   Traceback



AnS: <B> 2


10.Question 10
What is the most important benefit of writing your own functions?

<A>       Avoiding writing the same non-trivial code more than once in your program
<B>      Following the rule that no function can have more than 10 statements in it
<C>      Following the rule that whenever a program is more than 10 lines you must use a function
<D>      To avoid having more than 10 lines of sequential code without an indent or de-indent


AnS:<A>  Avoiding writing the same non-trivial code more than once in your program
