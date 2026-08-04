"""
@Author:Adithya v
"""
"""
this app was created in the purpose of teaching cbse 12th std students , with all the possible programs that might come in exams.
"""
import inspect
import queue
import re
import sys
import textwrap
import threading
import tkinter as tk
import tkinter.font as tkfont


# =============================================================================
# CODE / CONTINUE prompt — shows the Python source of whichever menu action
# is about to run, then runs it.
# =============================================================================


def _code_or_continue(fn):
    print()
    print()
    ch_cc = input("PRESS 1 for CODE\nPRESS ANYTHING ELSE TO CONTINUE:")
    if ch_cc.strip() == "1":
        source = textwrap.dedent(inspect.getsource(fn))
        cleaned = []
        prev_blank = False
        for ln in source.split("\n"):
            blank = ln.strip() == ""
            if blank and prev_blank:
                continue
            cleaned.append(ln)
            prev_blank = blank
        print()
        print(f"----- {fn.__name__}() -----")
        print("\n".join(cleaned))
        print(f"----- end {fn.__name__}() -----")
        print()
    fn()


def _show_code(fn):
    """SQL section helper: always prints the source, NEVER executes it
    (no live DB / server needed to study the queries)."""
    source = textwrap.dedent(inspect.getsource(fn))
    cleaned = []
    prev_blank = False
    for ln in source.split("\n"):
        blank = ln.strip() == ""
        if blank and prev_blank:
            continue
        cleaned.append(ln)
        prev_blank = blank
    print()
    print(f"----- {fn.__name__}() -----")
    print("\n".join(cleaned))
    print(f"----- end {fn.__name__}() -----")
    print()


def _show_sql(title, sql):
    """DDL/DML and Queries menus: show the plain SQL command(s) a student
    would type at the SQL prompt — no Python/connectivity wrapper."""
    print()
    print(f"----- {title} -----")
    print(sql.strip("\n"))
    print(f"----- end {title} -----")
    print()


# =============================================================================
# Shared MySQL connection helper — creates the 'school' database on first use
# (edit HOST/USER/PASSWORD below to match your MySQL server).
# =============================================================================

HOST="localhost"
USER="root"
PASSWORD=""

# Module-level variable used only to demonstrate the 'global' keyword
# (as opposed to 'nonlocal', which is demoed separately for enclosing scopes).
_scope_demo_var=5


def _db_connect():
    import mysql.connector
    a=mysql.connector.connect(host=HOST,user=USER,password=PASSWORD)
    b=a.cursor()
    b.execute("CREATE DATABASE IF NOT EXISTS school")
    a.close()
    return mysql.connector.connect(host=HOST,user=USER,password=PASSWORD,database="school")


# =============================================================================
# The Class 12 learning tool
# =============================================================================

def cs12():
    try:
        def function_types():
            def builtin_function_demo():
                print()
                a=[5,3,8,1,9]
                print("List:",a)
                print("len() built-in function:",len(a))
                print("max() built-in function:",max(a))
                print("sorted() built-in function:",sorted(a))
            def module_function_demo():
                import math
                print()
                a=16
                print("sqrt() from math module:",math.sqrt(a))
                print("factorial() from math module:",math.factorial(5))
            def user_defined_function_demo():
                def greet(name):
                    print("Hello",name,"! Welcome to Python functions.")
                print()
                a=input("Enter your name:")
                greet(a)
            def lambda_function_demo():
                print()
                a=lambda x:x*x
                b=int(input("Enter a number:"))
                print("Square using lambda:",a(b))
                c=input("Enter numbers separated by space:")
                d=[int(i) for i in c.split()]
                e=list(filter(lambda x:x%2==0,d))
                f=list(map(lambda x:x*x,d))
                print("Even numbers using filter+lambda:",e)
                print("Squares using map+lambda:",f)
            def recursive_function_type_demo():
                def fact(a):
                    if a==0 or a==1:
                        return 1
                    else:
                        return a*fact(a-1)
                print()
                print("A recursive function is a function that calls itself.")
                a=int(input("Enter a number:"))
                print("Factorial using a recursive function:",fact(a))
            def higher_order_function_demo():
                def apply_operation(a,b,c):
                    return c(a,b)
                def add(a,b):
                    return a+b
                def multiply(a,b):
                    return a*b
                print()
                print("A higher order function is a function that takes another")
                print("function as an argument (or returns one).")
                a=int(input("Enter first number:"))
                b=int(input("Enter second number:"))
                print("Sum using higher order function:",apply_operation(a,b,add))
                print("Product using higher order function:",apply_operation(a,b,multiply))
                print("Result using a lambda passed directly:",apply_operation(a,b,lambda x,y:x-y))
            def generator_function_demo():
                def even_upto(a):
                    for b in range(2,a+1,2):
                        yield b
                print()
                print("A generator function uses 'yield' instead of 'return' and")
                print("produces values one at a time, without storing them all in memory.")
                a=int(input("Enter a limit:"))
                b=even_upto(a)
                print("Even numbers using a generator function:")
                for c in b:
                    print(c,end=" ")
                print()
            def function_composition_demo():
                def square(a):
                    return a*a
                def increment(a):
                    return a+1
                def compose(a,b):
                    def combined(c):
                        return a(b(c))
                    return combined
                print()
                print("FUNCTION COMPOSITION combines two functions into a new one,")
                print("so calling the composed function applies both in sequence.")
                a=int(input("Enter a number:"))
                b=compose(square,increment)
                print("square(increment(x)) using composed function:",b(a))
                c=compose(increment,square)
                print("increment(square(x)) using composed function:",c(a))
            def memoized_function_demo():
                cache={}
                def fib_memo(a):
                    if a in cache:
                        return cache[a]
                    if a<=1:
                        result=a
                    else:
                        result=fib_memo(a-1)+fib_memo(a-2)
                    cache[a]=result
                    return result
                print()
                print("A MEMOIZED function stores results already computed in a")
                print("dictionary(cache), so repeated calls don't redo the work.")
                a=int(input("Enter a term number:"))
                print("Fibonacci term using a memoized function:",fib_memo(a))
                print("Cache after the call:",cache)
            def decorator_function_demo():
                def timer_decorator(fn):
                    def wrapper(*args):
                        print("Calling function:",fn.__name__)
                        result=fn(*args)
                        print("Function",fn.__name__,"finished")
                        return result
                    return wrapper
                @timer_decorator
                def add(a,b):
                    return a+b
                print()
                print("A DECORATOR wraps a function to add extra behaviour")
                print("without changing the function's own code.")
                a=int(input("Enter first number:"))
                b=int(input("Enter second number:"))
                print("Sum using decorated function:",add(a,b))
            def curried_function_demo():
                def multiply(a):
                    def inner(b):
                        return a*b
                    return inner
                print()
                print("A CURRIED function takes its arguments one at a time,")
                print("returning a new function after each call until all are supplied.")
                a=int(input("Enter first number:"))
                b=int(input("Enter second number:"))
                c=multiply(a)
                print("Product using curried function:",c(b))
            print()
            ch=int(input("WHAT DO YOU WANT TO SEE\nPRESS 1 for BUILT-IN FUNCTION\nPRESS 2 for MODULE FUNCTION\nPRESS 3 for USER DEFINED FUNCTION\nPRESS 4 for LAMBDA FUNCTION(map/filter)\nPRESS 5 for RECURSIVE FUNCTION(AS A TYPE)\nPRESS 6 for HIGHER ORDER FUNCTION(FUNCTION AS ARGUMENT)\nPRESS 7 for GENERATOR FUNCTION(yield)\nPRESS 8 for FUNCTION COMPOSITION DEMO\nPRESS 9 for MEMOIZED FUNCTION USING A CACHE DICTIONARY\nPRESS 10 for DECORATOR FUNCTION DEMO\nPRESS 11 for CURRIED FUNCTION DEMO:"))
            if ch==1:
                _code_or_continue(builtin_function_demo)
            elif ch==2:
                _code_or_continue(module_function_demo)
            elif ch==3:
                _code_or_continue(user_defined_function_demo)
            elif ch==4:
                _code_or_continue(lambda_function_demo)
            elif ch==5:
                _code_or_continue(recursive_function_type_demo)
            elif ch==6:
                _code_or_continue(higher_order_function_demo)
            elif ch==7:
                _code_or_continue(generator_function_demo)
            elif ch==8:
                _code_or_continue(function_composition_demo)
            elif ch==9:
                _code_or_continue(memoized_function_demo)
            elif ch==10:
                _code_or_continue(decorator_function_demo)
            elif ch==11:
                _code_or_continue(curried_function_demo)

        def function_arguments():
            def positional_arguments():
                def subtract(a,b):
                    return a-b
                print()
                a=int(input("Enter first number:"))
                b=int(input("Enter second number:"))
                print("a-b using positional arguments:",subtract(a,b))
                print("b-a using positional arguments:",subtract(b,a))
            def default_arguments():
                def power(a,b=2):
                    return a**b
                print()
                a=int(input("Enter the base number:"))
                print("Square of the number(default exponent):",power(a))
                b=int(input("Enter an exponent:"))
                print("Number raised to given exponent:",power(a,b))
            def keyword_arguments():
                def student_info(name,age,cls):
                    print("Name:",name)
                    print("Age:",age)
                    print("Class:",cls)
                print()
                a=input("Enter name:")
                b=int(input("Enter age:"))
                c=input("Enter class:")
                student_info(cls=c,name=a,age=b)
            def multiple_argument_types_together():
                def order_bill(item,qty=1,*,discount=0):
                    total=qty*100
                    total=total-(total*discount/100)
                    print("Item:",item,"Qty:",qty,"Discount:",discount,"%","Total:",total)
                print()
                a=input("Enter item name:")
                b=int(input("Enter quantity:"))
                c=int(input("Enter discount percentage:"))
                order_bill(a,qty=b,discount=c)
            def variable_length_arguments():
                def total_marks(*args):
                    return sum(args)
                print()
                a=input("Enter marks separated by space:")
                b=[int(i) for i in a.split()]
                print("Total marks using *args:",total_marks(*b))
            def variable_length_keyword_arguments():
                def student_report(**kwargs):
                    for a,b in kwargs.items():
                        print(a,":",b)
                print()
                a=input("Enter name:")
                b=int(input("Enter age:"))
                c=input("Enter city:")
                student_report(name=a,age=b,city=c)
            def mutable_default_argument_pitfall():
                def add_item(a,b=[]):
                    b.append(a)
                    return b
                print()
                print("Calling add_item(1) three times WITHOUT passing a list:")
                print(add_item(1))
                print(add_item(2))
                print(add_item(3))
                print("Notice the list keeps growing — mutable default arguments")
                print("are created ONCE, when the function is defined, not on")
                print("every call. Always use None as default for mutables:")
                def add_item_safe(a,b=None):
                    if b is None:
                        b=[]
                    b.append(a)
                    return b
                print(add_item_safe(1))
                print(add_item_safe(2))
            def positional_only_keyword_only_demo():
                def calculate_bill(item,qty,/,*,discount=0):
                    total=qty*100
                    total=total-(total*discount/100)
                    return total
                print()
                print("item,qty before '/' are POSITIONAL-ONLY.")
                print("discount after '*' is KEYWORD-ONLY.")
                a=input("Enter item name:")
                b=int(input("Enter quantity:"))
                c=int(input("Enter discount percentage:"))
                print("Total using positional-only + keyword-only arguments:",calculate_bill(a,b,discount=c))
                try:
                    calculate_bill(item=a,qty=b,discount=c)
                except TypeError as e:
                    print("Calling with item/qty as keywords fails:",e)
            def argument_unpacking_demo():
                def student_info(name,age,cls):
                    print("Name:",name,"Age:",age,"Class:",cls)
                print()
                a=input("Enter name:")
                b=int(input("Enter age:"))
                c=input("Enter class:")
                d=[a,b,c]
                print("Calling function by unpacking a list using *:")
                student_info(*d)
                e={"name":a,"age":b,"cls":c}
                print("Calling function by unpacking a dictionary using **:")
                student_info(**e)
            def call_by_value_reference_demo():
                def modify_number(a):
                    a=a+10
                    return a
                def modify_list(a):
                    a.append(100)
                print()
                print("IMMUTABLE arguments(int,str,tuple) behave like CALL BY VALUE —")
                print("changes inside the function do NOT affect the original.")
                a=int(input("Enter a number:"))
                print("Before calling function, number =",a)
                modify_number(a)
                print("After calling function, number =",a,"(unchanged)")
                print()
                print("MUTABLE arguments(list,dict,set) behave like CALL BY REFERENCE —")
                print("changes inside the function DO affect the original.")
                b=[int(i) for i in input("Enter numbers separated by space:").split()]
                print("Before calling function, list =",b)
                modify_list(b)
                print("After calling function, list =",b,"(modified in place)")
            def recursive_sum_with_default_accumulator_demo():
                def total(a,b=0):
                    if a==[]:
                        return b
                    else:
                        return total(a[1:],b+a[0])
                print()
                print("The default argument 'b=0' acts as an ACCUMULATOR that carries")
                print("the running total through each recursive call.")
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                print("Sum using recursion with a default accumulator argument:",total(b))
            def argument_type_validation_demo():
                def safe_divide(a,b):
                    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
                        raise TypeError("Both arguments must be numbers")
                    return a/b
                print()
                print("isinstance() checks an argument's type BEFORE using it,")
                print("so a clear error is raised instead of a confusing one later.")
                a=input("Enter numerator:")
                b=input("Enter denominator:")
                try:
                    a=float(a)
                    b=float(b)
                    print("Result:",safe_divide(a,b))
                except ValueError:
                    print("Enter numeric values only")
                except ZeroDivisionError:
                    print("Denominator can't be zero")
            def combined_star_args_kwargs_demo():
                def student_summary(*marks,**details):
                    print("Marks:",marks)
                    print("Total:",sum(marks))
                    for a,b in details.items():
                        print(a,":",b)
                print()
                print("*args collects extra POSITIONAL arguments as a tuple,")
                print("**kwargs collects extra KEYWORD arguments as a dictionary —")
                print("both can be used together in the same function.")
                a=input("Enter marks separated by space:")
                b=[int(i) for i in a.split()]
                c=input("Enter name:")
                d=input("Enter city:")
                student_summary(*b,name=c,city=d)
            def custom_min_max_using_args_demo():
                def my_max(*args):
                    a=args[0]
                    for b in args[1:]:
                        if b>a:
                            a=b
                    return a
                print()
                print("A custom MAX function built using *args, without using")
                print("the built-in max() function.")
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                print("Largest number using custom function with *args:",my_max(*b))
            print()
            ch=int(input("WHAT DO YOU WANT TO SEE\nPRESS 1 for POSITIONAL ARGUMENTS\nPRESS 2 for DEFAULT ARGUMENTS\nPRESS 3 for KEYWORD ARGUMENTS\nPRESS 4 for MULTIPLE ARGUMENT TYPES TOGETHER\nPRESS 5 for VARIABLE LENGTH ARGUMENTS(*args)\nPRESS 6 for VARIABLE LENGTH KEYWORD ARGUMENTS(**kwargs)\nPRESS 7 for MUTABLE DEFAULT ARGUMENT PITFALL\nPRESS 8 for POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS\nPRESS 9 for UNPACKING ARGUMENTS USING * AND **\nPRESS 10 for CALL BY VALUE VS CALL BY REFERENCE\nPRESS 11 for RECURSION WITH A DEFAULT ACCUMULATOR ARGUMENT\nPRESS 12 for ARGUMENT TYPE VALIDATION USING isinstance()\nPRESS 13 for COMBINED *args AND **kwargs\nPRESS 14 for CUSTOM MAX() USING *args:"))
            if ch==1:
                _code_or_continue(positional_arguments)
            elif ch==2:
                _code_or_continue(default_arguments)
            elif ch==3:
                _code_or_continue(keyword_arguments)
            elif ch==4:
                _code_or_continue(multiple_argument_types_together)
            elif ch==5:
                _code_or_continue(variable_length_arguments)
            elif ch==6:
                _code_or_continue(variable_length_keyword_arguments)
            elif ch==7:
                _code_or_continue(mutable_default_argument_pitfall)
            elif ch==8:
                _code_or_continue(positional_only_keyword_only_demo)
            elif ch==9:
                _code_or_continue(argument_unpacking_demo)
            elif ch==10:
                _code_or_continue(call_by_value_reference_demo)
            elif ch==11:
                _code_or_continue(recursive_sum_with_default_accumulator_demo)
            elif ch==12:
                _code_or_continue(argument_type_validation_demo)
            elif ch==13:
                _code_or_continue(combined_star_args_kwargs_demo)
            elif ch==14:
                _code_or_continue(custom_min_max_using_args_demo)

        def function_return_values():
            def single_return_value():
                def square(a):
                    return a*a
                print()
                a=int(input("Enter a number:"))
                print("Square:",square(a))
            def multiple_return_values():
                def min_max_sum(a):
                    return min(a),max(a),sum(a)
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                c,d,e=min_max_sum(b)
                print("Minimum:",c)
                print("Maximum:",d)
                print("Sum:",e)
            def no_return_value():
                def display_greeting(a):
                    print("Hello",a)
                print()
                b=input("Enter your name:")
                c=display_greeting(b)
                print("Value returned by a function with no return statement:",c)
            def function_returning_function():
                def make_multiplier(a):
                    def multiplier(b):
                        return a*b
                    return multiplier
                print()
                a=int(input("Enter a multiplier value:"))
                b=make_multiplier(a)
                c=int(input("Enter a number to multiply:"))
                print("Result using function returned by another function:",b(c))
            def boolean_returning_function_demo():
                def is_even(a):
                    return a%2==0
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                c=list(filter(is_even,b))
                print("Even numbers using a function that returns True/False:",c)
            def early_return_demo():
                def grade(a):
                    if a<0 or a>100:
                        return "Invalid marks"
                    if a>=90:
                        return "A1"
                    if a>=75:
                        return "A2"
                    if a>=60:
                        return "B1"
                    return "Needs improvement"
                print()
                print("This function uses EARLY RETURN — it exits as soon as")
                print("a matching condition is found, instead of nested if-else.")
                a=int(input("Enter marks:"))
                print("Grade:",grade(a))
            def function_returning_dictionary_demo():
                def student_record(a,b,c):
                    return {"name":a,"age":b,"marks":c}
                print()
                a=input("Enter name:")
                b=int(input("Enter age:"))
                c=float(input("Enter marks:"))
                d=student_record(a,b,c)
                print("Dictionary returned by the function:",d)
                print("Accessing a key from the returned dictionary:",d["marks"])
            def chained_function_calls_demo():
                def double(a):
                    return a*2
                def add_five(a):
                    return a+5
                def square(a):
                    return a*a
                print()
                print("CHAINING passes the return value of one function straight")
                print("into the next, without storing it in a variable first.")
                a=int(input("Enter a number:"))
                print("square(add_five(double(x))) chained result:",square(add_five(double(a))))
            def recursive_function_returning_tuple_demo():
                def counts(a):
                    if a==[]:
                        return (0,0,0)
                    b,c,d=counts(a[1:])
                    if a[0]>0:
                        return (b+1,c,d)
                    elif a[0]<0:
                        return (b,c+1,d)
                    else:
                        return (b,c,d+1)
                print()
                print("This recursive function returns a TUPLE of three counts at")
                print("every step, accumulated as the recursion unwinds.")
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                p,n,z=counts(b)
                print("Positives:",p)
                print("Negatives:",n)
                print("Zeros:",z)
            def return_none_implicit_demo():
                def check_and_print(a):
                    if a>0:
                        print(a,"is positive")
                        return True
                print()
                print("A function that has NO return in one of its branches implicitly")
                print("returns None for that branch, which can silently cause bugs.")
                a=int(input("Enter a number:"))
                b=check_and_print(a)
                print("Value returned:",b)
                if b is None:
                    print("Warning: got None back — the number was probably not positive")
            def function_returning_list_of_tuples_demo():
                def pair_with_squares(a):
                    b=[]
                    for c in a:
                        b.append((c,c*c))
                    return b
                print()
                print("This function returns a LIST OF TUPLES, pairing each number")
                print("with its square.")
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                c=pair_with_squares(b)
                print("Number-square pairs returned:",c)
                for d,e in c:
                    print(d,"squared is",e)
            print()
            ch=int(input("WHAT DO YOU WANT TO SEE\nPRESS 1 for SINGLE RETURN VALUE\nPRESS 2 for MULTIPLE RETURN VALUES\nPRESS 3 for FUNCTION WITH NO RETURN(returns None)\nPRESS 4 for FUNCTION RETURNING ANOTHER FUNCTION\nPRESS 5 for FUNCTION RETURNING A BOOLEAN(USED WITH filter)\nPRESS 6 for EARLY RETURN(GUARD CLAUSE) DEMO\nPRESS 7 for FUNCTION RETURNING A DICTIONARY\nPRESS 8 for CHAINING FUNCTION CALLS TOGETHER\nPRESS 9 for RECURSIVE FUNCTION RETURNING A TUPLE OF COUNTS\nPRESS 10 for IMPLICIT None RETURN PITFALL\nPRESS 11 for FUNCTION RETURNING A LIST OF TUPLES:"))
            if ch==1:
                _code_or_continue(single_return_value)
            elif ch==2:
                _code_or_continue(multiple_return_values)
            elif ch==3:
                _code_or_continue(no_return_value)
            elif ch==4:
                _code_or_continue(function_returning_function)
            elif ch==5:
                _code_or_continue(boolean_returning_function_demo)
            elif ch==6:
                _code_or_continue(early_return_demo)
            elif ch==7:
                _code_or_continue(function_returning_dictionary_demo)
            elif ch==8:
                _code_or_continue(chained_function_calls_demo)
            elif ch==9:
                _code_or_continue(recursive_function_returning_tuple_demo)
            elif ch==10:
                _code_or_continue(return_none_implicit_demo)
            elif ch==11:
                _code_or_continue(function_returning_list_of_tuples_demo)

        def function_scope():
            def global_scope_demo():
                a=10
                def show():
                    print("Accessing global variable a inside function:",a)
                print()
                show()
                print("Accessing global variable a outside function:",a)
            def local_scope_demo():
                def show():
                    a=20
                    print("Local variable a inside function:",a)
                print()
                show()
                try:
                    print(a)
                except NameError:
                    print("a is not accessible outside the function(local scope)")
            def global_keyword_demo():
                a=5
                def modify():
                    nonlocal a
                    a=a+10
                print()
                print("Before calling function, a =",a)
                modify()
                print("After calling function using nonlocal keyword, a =",a)
            def global_keyword_modify_demo():
                global _scope_demo_var
                print()
                print("Before calling function, _scope_demo_var =",_scope_demo_var)
                _scope_demo_var=_scope_demo_var+10
                print("After modifying using global keyword, _scope_demo_var =",_scope_demo_var)
            def legb_rule_demo():
                a="global"
                def outer():
                    a="enclosing"
                    def inner():
                        a="local"
                        print("Inside inner(), Python finds a in LOCAL scope:",a)
                    inner()
                    print("Inside outer(), Python finds a in ENCLOSING scope:",a)
                print()
                outer()
                print("Outside all functions, Python finds a in GLOBAL scope:",a)
                print("LEGB order: Local -> Enclosing -> Global -> Built-in")
            def variable_shadowing_demo():
                a=100
                def show():
                    a=200
                    print("Local a SHADOWS the global a, inside function:",a)
                print()
                print("Global a before calling function:",a)
                show()
                print("Global a after calling function(unchanged):",a)
            def closure_counter_demo():
                def make_counter():
                    count=0
                    def counter():
                        nonlocal count
                        count+=1
                        return count
                    return counter
                print()
                print("A CLOSURE remembers the enclosing variable(count)")
                print("across multiple calls, using nonlocal.")
                a=make_counter()
                for i in range(4):
                    print("Counter call",i+1,"->",a())
            def read_enclosing_without_nonlocal_demo():
                def outer():
                    a=50
                    def inner():
                        print("Just READING the enclosing variable a needs no nonlocal:",a)
                    inner()
                print()
                print("'nonlocal' is only required to MODIFY(rebind) an enclosing")
                print("variable. Merely reading it works without any keyword.")
                outer()
            def for_loop_scope_demo():
                def show_loop_variable():
                    for a in range(3):
                        pass
                    print("The for-loop variable 'a' still exists after the loop:",a)
                def show_comprehension_variable():
                    b=[c for c in range(3)]
                    print()
                    print("Inside a list comprehension, the loop variable 'c' does NOT")
                    print("leak into the surrounding scope(a Python 3 difference).")
                    try:
                        print(c)
                    except NameError:
                        print("c is not accessible here — NameError, as expected")
                print()
                show_loop_variable()
                show_comprehension_variable()
            def class_attribute_scope_demo():
                class Counter:
                    total_created=0
                    def __init__(self,a):
                        self.name=a
                        Counter.total_created+=1
                print()
                print("A CLASS ATTRIBUTE(total_created) is shared by every object,")
                print("unlike an INSTANCE ATTRIBUTE(name), which belongs to just one.")
                a=Counter(input("Enter first object's name:"))
                b=Counter(input("Enter second object's name:"))
                print("First object's name(instance attribute):",a.name)
                print("Second object's name(instance attribute):",b.name)
                print("Objects created so far(class attribute):",Counter.total_created)
            def global_vs_local_same_name_demo():
                a=1
                def modify_local():
                    a=99
                    print("Inside function, LOCAL a(unrelated to global):",a)
                print()
                print("Global a before calling function:",a)
                modify_local()
                print("Global a after calling function(untouched):",a)
                print("A local variable with the same name never affects the global one")
                print("unless the 'global' keyword is used.")
            def unboundlocalerror_demo():
                a=10
                def buggy():
                    print("Trying to print a, then increment it in the same function...")
                    try:
                        print(a)
                        nonlocal_a=a+1
                    except UnboundLocalError as e:
                        print("UnboundLocalError:",e)
                def fixed():
                    global _scope_demo_var
                    print("Reading and modifying a MODULE-level variable safely:")
                    print("Before:",_scope_demo_var)
                    _scope_demo_var+=1
                    print("After:",_scope_demo_var)
                print()
                print("Assigning to a name ANYWHERE inside a function makes it LOCAL")
                print("for the WHOLE function — so reading it before that line fails.")
                buggy()
                fixed()
            print()
            ch=int(input("WHAT DO YOU WANT TO SEE\nPRESS 1 for GLOBAL SCOPE\nPRESS 2 for LOCAL SCOPE\nPRESS 3 for MODIFYING OUTER VARIABLE USING NONLOCAL\nPRESS 4 for MODIFYING GLOBAL VARIABLE USING GLOBAL KEYWORD\nPRESS 5 for LEGB RULE(Local-Enclosing-Global-Built-in)\nPRESS 6 for VARIABLE SHADOWING DEMO\nPRESS 7 for CLOSURE COUNTER USING nonlocal\nPRESS 8 for READING ENCLOSING VARIABLE WITHOUT nonlocal\nPRESS 9 for FOR-LOOP VS LIST COMPREHENSION SCOPE\nPRESS 10 for CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE SCOPE\nPRESS 11 for GLOBAL VS LOCAL VARIABLE WITH SAME NAME\nPRESS 12 for UnboundLocalError DEMO:"))
            if ch==1:
                _code_or_continue(global_scope_demo)
            elif ch==2:
                _code_or_continue(local_scope_demo)
            elif ch==3:
                _code_or_continue(global_keyword_demo)
            elif ch==4:
                _code_or_continue(global_keyword_modify_demo)
            elif ch==5:
                _code_or_continue(legb_rule_demo)
            elif ch==6:
                _code_or_continue(variable_shadowing_demo)
            elif ch==7:
                _code_or_continue(closure_counter_demo)
            elif ch==8:
                _code_or_continue(read_enclosing_without_nonlocal_demo)
            elif ch==9:
                _code_or_continue(for_loop_scope_demo)
            elif ch==10:
                _code_or_continue(class_attribute_scope_demo)
            elif ch==11:
                _code_or_continue(global_vs_local_same_name_demo)
            elif ch==12:
                _code_or_continue(unboundlocalerror_demo)

        def recursion():
            def factorial_recursive():
                def fact(a):
                    if a==0 or a==1:
                        return 1
                    else:
                        return a*fact(a-1)
                print()
                a=int(input("Enter a number:"))
                print("Factorial using recursion:",fact(a))
            def fibonacci_recursive():
                def fib(a):
                    if a<=1:
                        return a
                    else:
                        return fib(a-1)+fib(a-2)
                print()
                a=int(input("Enter number of terms:"))
                print("Fibonacci series using recursion:")
                for i in range(a):
                    print(fib(i),end=" ")
                print()
            def sum_of_digits_recursive():
                def digit_sum(a):
                    if a==0:
                        return 0
                    else:
                        return a%10+digit_sum(a//10)
                print()
                a=int(input("Enter a number:"))
                print("Sum of digits using recursion:",digit_sum(a))
            def gcd_recursive():
                def gcd(a,b):
                    if b==0:
                        return a
                    else:
                        return gcd(b,a%b)
                print()
                a=int(input("Enter first number:"))
                b=int(input("Enter second number:"))
                print("GCD using recursion:",gcd(a,b))
            def power_recursive():
                def power(a,b):
                    if b==0:
                        return 1
                    else:
                        return a*power(a,b-1)
                print()
                a=int(input("Enter base:"))
                b=int(input("Enter exponent:"))
                print("Power using recursion:",power(a,b))
            def sum_of_list_recursive():
                def list_sum(a):
                    if a==[]:
                        return 0
                    else:
                        return a[0]+list_sum(a[1:])
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                print("Sum of list using recursion:",list_sum(b))
            def tower_of_hanoi():
                def hanoi(a,b,c,d):
                    if a==1:
                        print("Move disk 1 from",b,"to",d)
                        return
                    hanoi(a-1,b,d,c)
                    print("Move disk",a,"from",b,"to",d)
                    hanoi(a-1,c,b,d)
                print()
                a=int(input("Enter number of disks:"))
                hanoi(a,"A","B","C")
            def binary_search_recursive():
                def search(a,b,c,d):
                    if c>d:
                        return -1
                    e=(c+d)//2
                    if a[e]==b:
                        return e
                    elif a[e]<b:
                        return search(a,b,e+1,d)
                    else:
                        return search(a,b,c,e-1)
                print()
                a=input("Enter numbers in ascending order, separated by space:")
                b=[int(i) for i in a.split()]
                c=int(input("Enter number to search:"))
                d=search(b,c,0,len(b)-1)
                if d==-1:
                    print("Number not found")
                else:
                    print("Number found at index:",d)
            def sum_of_natural_numbers_recursive():
                def total(a):
                    if a==0:
                        return 0
                    else:
                        return a+total(a-1)
                print()
                a=int(input("Enter a number:"))
                print("Sum of first",a,"natural numbers using recursion:",total(a))
            def string_reverse_recursive():
                def reverse(a):
                    if len(a)==0:
                        return a
                    else:
                        return reverse(a[1:])+a[0]
                print()
                a=input("Enter a string:")
                print("Reversed string using recursion:",reverse(a))
            def count_occurrence_recursive():
                def count(a,b,c):
                    if c==len(a):
                        return 0
                    elif a[c]==b:
                        return 1+count(a,b,c+1)
                    else:
                        return count(a,b,c+1)
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                c=int(input("Enter the number to count:"))
                print("Occurrences of",c,"using recursion:",count(b,c,0))
            def max_of_list_recursive():
                def find_max(a):
                    if len(a)==1:
                        return a[0]
                    else:
                        b=find_max(a[1:])
                        return a[0] if a[0]>b else b
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                print("Maximum of the list using recursion:",find_max(b))
            def palindrome_check_recursive():
                def is_palindrome(a):
                    if len(a)<=1:
                        return True
                    if a[0]!=a[-1]:
                        return False
                    return is_palindrome(a[1:-1])
                print()
                a=input("Enter a string:")
                b=a.replace(" ","").lower()
                if is_palindrome(b):
                    print(a,"is a palindrome(checked using recursion)")
                else:
                    print(a,"is not a palindrome(checked using recursion)")
            def is_sorted_recursive():
                def check_sorted(a):
                    if len(a)<=1:
                        return True
                    if a[0]>a[1]:
                        return False
                    return check_sorted(a[1:])
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                if check_sorted(b):
                    print("The list is sorted in ascending order(checked using recursion)")
                else:
                    print("The list is NOT sorted in ascending order(checked using recursion)")
            def reverse_number_recursive():
                def reverse_num(a,b=0):
                    if a==0:
                        return b
                    return reverse_num(a//10,b*10+a%10)
                print()
                a=int(input("Enter a number:"))
                print("Reversed number using recursion:",reverse_num(a))
            def sum_of_ap_series_recursive():
                def ap_sum(a,d,n):
                    if n==1:
                        return a
                    return ap_sum(a,d,n-1)+(a+(n-1)*d)
                print()
                print("Sum of an ARITHMETIC PROGRESSION(first term a, common")
                print("difference d, n terms) computed using recursion.")
                a=int(input("Enter first term:"))
                d=int(input("Enter common difference:"))
                n=int(input("Enter number of terms:"))
                print("Sum of the AP using recursion:",ap_sum(a,d,n))
            print()
            ch=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for FACTORIAL\nPRESS 2 for FIBONACCI SERIES\nPRESS 3 for SUM OF DIGITS\nPRESS 4 for GCD\nPRESS 5 for POWER\nPRESS 6 for SUM OF A LIST\nPRESS 7 for TOWER OF HANOI\nPRESS 8 for BINARY SEARCH(RECURSIVE)\nPRESS 9 for SUM OF NATURAL NUMBERS\nPRESS 10 for STRING REVERSAL(RECURSIVE)\nPRESS 11 for COUNT OCCURRENCE OF A NUMBER(RECURSIVE)\nPRESS 12 for MAXIMUM OF A LIST(RECURSIVE)\nPRESS 13 for PALINDROME CHECK(RECURSIVE)\nPRESS 14 for CHECK IF A LIST IS SORTED(RECURSIVE)\nPRESS 15 for REVERSE A NUMBER(RECURSIVE)\nPRESS 16 for SUM OF AN ARITHMETIC PROGRESSION(RECURSIVE):"))
            if ch==1:
                _code_or_continue(factorial_recursive)
            elif ch==2:
                _code_or_continue(fibonacci_recursive)
            elif ch==3:
                _code_or_continue(sum_of_digits_recursive)
            elif ch==4:
                _code_or_continue(gcd_recursive)
            elif ch==5:
                _code_or_continue(power_recursive)
            elif ch==6:
                _code_or_continue(sum_of_list_recursive)
            elif ch==7:
                _code_or_continue(tower_of_hanoi)
            elif ch==8:
                _code_or_continue(binary_search_recursive)
            elif ch==9:
                _code_or_continue(sum_of_natural_numbers_recursive)
            elif ch==10:
                _code_or_continue(string_reverse_recursive)
            elif ch==11:
                _code_or_continue(count_occurrence_recursive)
            elif ch==12:
                _code_or_continue(max_of_list_recursive)
            elif ch==13:
                _code_or_continue(palindrome_check_recursive)
            elif ch==14:
                _code_or_continue(is_sorted_recursive)
            elif ch==15:
                _code_or_continue(reverse_number_recursive)
            elif ch==16:
                _code_or_continue(sum_of_ap_series_recursive)

        def exception_handling():
            def basic_try_except():
                print()
                try:
                    a=int(input("Enter numerator:"))
                    b=int(input("Enter denominator:"))
                    print("Result:",a/b)
                except ZeroDivisionError:
                    print("You can't divide by zero")
            def multiple_except_blocks():
                print()
                try:
                    a=int(input("Enter a number:"))
                    b=[1,2,3]
                    print(b[a])
                except ZeroDivisionError:
                    print("Division by zero error")
                except IndexError:
                    print("Index out of range")
                except ValueError:
                    print("Invalid value entered, enter an integer")
            def try_except_else_finally():
                print()
                try:
                    a=int(input("Enter a number:"))
                    b=int(input("Enter another number:"))
                    c=a/b
                except ZeroDivisionError:
                    print("Denominator can't be zero")
                else:
                    print("Division successful, result:",c)
                finally:
                    print("This finally block always executes")
            def raising_an_exception():
                def check_age(a):
                    if a<0:
                        raise ValueError("Age cannot be negative")
                    else:
                        print("Valid age:",a)
                print()
                try:
                    a=int(input("Enter your age:"))
                    check_age(a)
                except ValueError as e:
                    print("Exception raised:",e)
            def custom_exception_demo():
                class NegativeMarksError(Exception):
                    pass
                def check_marks(a):
                    if a<0:
                        raise NegativeMarksError("Marks cannot be negative")
                    else:
                        print("Valid marks:",a)
                print()
                try:
                    a=int(input("Enter marks:"))
                    check_marks(a)
                except NegativeMarksError as e:
                    print("Custom exception raised:",e)
            def tuple_of_exceptions():
                print()
                try:
                    a=int(input("Enter a number:"))
                    b=[10,20,30]
                    print(b[a]/a)
                except (ZeroDivisionError,IndexError) as e:
                    print("Caught using a single except with a tuple:",type(e).__name__,"-",e)
            def assert_statement_demo():
                def check_marks(a):
                    assert 0<=a<=100,"Marks must be between 0 and 100"
                    print("Valid marks:",a)
                print()
                try:
                    a=int(input("Enter marks:"))
                    check_marks(a)
                except AssertionError as e:
                    print("AssertionError raised:",e)
            def nested_try_except_demo():
                print()
                try:
                    a=int(input("Enter a list size:"))
                    b=[int(i) for i in input("Enter elements separated by space:").split()]
                    try:
                        c=int(input("Enter an index to access:"))
                        print("Element at index",c,":",b[c])
                    except IndexError:
                        print("Inner except: index out of range for the list")
                except ValueError:
                    print("Outer except: invalid integer entered")
            def retry_until_valid_input_demo():
                print()
                print("Keeps asking for input until a valid positive integer is given.")
                a=None
                while a is None:
                    try:
                        b=int(input("Enter a positive integer:"))
                        if b<=0:
                            raise ValueError("Number must be positive")
                        a=b
                    except ValueError as e:
                        print("Invalid input(",e,"), try again")
                print("Accepted value:",a)
            def custom_exception_with_data_demo():
                class InsufficientBalanceError(Exception):
                    def __init__(self,balance,amount):
                        self.balance=balance
                        self.amount=amount
                        super().__init__("Cannot withdraw "+str(amount)+", balance is only "+str(balance))
                def withdraw(a,b):
                    if b>a:
                        raise InsufficientBalanceError(a,b)
                    else:
                        return a-b
                print()
                a=float(input("Enter account balance:"))
                b=float(input("Enter amount to withdraw:"))
                try:
                    print("Balance after withdrawal:",withdraw(a,b))
                except InsufficientBalanceError as e:
                    print("Custom exception with extra data raised:",e)
                    print("Shortfall amount:",e.amount-e.balance)
            def bare_except_demo():
                print()
                print("A bare 'except:' catches ANY exception, but hides the type —")
                print("it should generally be avoided in favour of a specific except.")
                try:
                    a=int(input("Enter a number:"))
                    b=int(input("Enter another number:"))
                    print("Result:",a/b)
                except:
                    print("Something went wrong(caught by bare except)")
            def finally_with_return_demo():
                def safe_divide(a,b):
                    try:
                        return a/b
                    except ZeroDivisionError:
                        return None
                    finally:
                        print("finally block runs even though the try/except returned")
                print()
                a=int(input("Enter numerator:"))
                b=int(input("Enter denominator:"))
                c=safe_divide(a,b)
                print("Value returned by the function:",c)
            def exception_chaining_demo():
                def get_marks(a):
                    try:
                        return float(a)
                    except ValueError as e:
                        raise ValueError("Marks must be a number") from e
                print()
                print("'raise ... from e' CHAINS a new exception to the original one,")
                print("so both the cause and the final error are visible together.")
                a=input("Enter marks:")
                try:
                    print("Marks accepted:",get_marks(a))
                except ValueError as e:
                    print("Final exception:",e)
                    print("Original cause:",e.__cause__)
            print()
            ch=int(input("WHAT DO YOU WANT TO SEE\nPRESS 1 for BASIC TRY-EXCEPT\nPRESS 2 for MULTIPLE EXCEPT BLOCKS\nPRESS 3 for TRY-EXCEPT-ELSE-FINALLY\nPRESS 4 for RAISING AN EXCEPTION\nPRESS 5 for CUSTOM EXCEPTION CLASS\nPRESS 6 for SINGLE EXCEPT WITH A TUPLE OF EXCEPTIONS\nPRESS 7 for ASSERT STATEMENT\nPRESS 8 for NESTED TRY-EXCEPT\nPRESS 9 for RETRY UNTIL VALID INPUT(LOOP+TRY)\nPRESS 10 for CUSTOM EXCEPTION CARRYING EXTRA DATA\nPRESS 11 for BARE EXCEPT CLAUSE\nPRESS 12 for FINALLY RUNNING EVEN WITH A RETURN\nPRESS 13 for EXCEPTION CHAINING USING raise...from:"))
            if ch==1:
                _code_or_continue(basic_try_except)
            elif ch==2:
                _code_or_continue(multiple_except_blocks)
            elif ch==3:
                _code_or_continue(try_except_else_finally)
            elif ch==4:
                _code_or_continue(raising_an_exception)
            elif ch==5:
                _code_or_continue(custom_exception_demo)
            elif ch==6:
                _code_or_continue(tuple_of_exceptions)
            elif ch==7:
                _code_or_continue(assert_statement_demo)
            elif ch==8:
                _code_or_continue(nested_try_except_demo)
            elif ch==9:
                _code_or_continue(retry_until_valid_input_demo)
            elif ch==10:
                _code_or_continue(custom_exception_with_data_demo)
            elif ch==11:
                _code_or_continue(bare_except_demo)
            elif ch==12:
                _code_or_continue(finally_with_return_demo)
            elif ch==13:
                _code_or_continue(exception_chaining_demo)

        def text_file_handling():
            def writing_to_text_file():
                print()
                a=open("sample.txt","w")
                print("Enter lines of text, type END to stop:")
                while True:
                    b=input()
                    if b=="END":
                        break
                    a.write(b+"\n")
                a.close()
                print("Data written to sample.txt")
            def appending_to_text_file():
                print()
                a=open("sample.txt","a")
                b=input("Enter a line to append:")
                a.write(b+"\n")
                a.close()
                print("Line appended to sample.txt")
            def reading_whole_file():
                print()
                try:
                    a=open("sample.txt","r")
                    print(a.read())
                    a.close()
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def reading_line_by_line():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.readline()
                    while b:
                        print(b.strip())
                        b=a.readline()
                    a.close()
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def words_separated_by_hash():
                print()
                try:
                    a=open("sample.txt","r")
                    for b in a:
                        c=b.split()
                        print("#".join(c))
                    a.close()
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def counting_vowels_consonants_case():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.read()
                    a.close()
                    vowels=0
                    consonants=0
                    upper=0
                    lower=0
                    for c in b:
                        if c.isalpha():
                            if c.lower() in "aeiou":
                                vowels+=1
                            else:
                                consonants+=1
                            if c.isupper():
                                upper+=1
                            else:
                                lower+=1
                    print("Vowels:",vowels)
                    print("Consonants:",consonants)
                    print("Uppercase letters:",upper)
                    print("Lowercase letters:",lower)
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def remove_lines_with_a():
                print()
                try:
                    a=open("sample.txt","r")
                    b=open("sample_no_a.txt","w")
                    for c in a:
                        if "a" not in c and "A" not in c:
                            b.write(c)
                    a.close()
                    b.close()
                    print("Lines without 'a' written to sample_no_a.txt")
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def seek_and_tell_demo():
                print()
                try:
                    a=open("sample.txt","r")
                    print("Current position:",a.tell())
                    b=a.read(10)
                    print("First 10 characters:",b)
                    print("Position after reading:",a.tell())
                    a.seek(0)
                    print("Position after seek(0):",a.tell())
                    a.close()
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def count_lines_words_chars():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.readlines()
                    a.close()
                    c=len(b)
                    d=0
                    e=0
                    for f in b:
                        d+=len(f.split())
                        e+=len(f)
                    print("Lines:",c)
                    print("Words:",d)
                    print("Characters:",e)
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def word_occurrence_count():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.read()
                    a.close()
                    c=input("Enter a word to count:")
                    d=b.split()
                    e=0
                    for f in d:
                        if f.strip(".,!?").lower()==c.lower():
                            e+=1
                    print("'"+c+"' occurs",e,"time(s) in sample.txt")
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def copy_file_content():
                print()
                try:
                    a=open("sample.txt","r")
                    b=open("sample_copy.txt","w")
                    for c in a:
                        b.write(c)
                    a.close()
                    b.close()
                    print("Content copied to sample_copy.txt")
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def lines_starting_with_specific_letter():
                print()
                try:
                    a=open("sample.txt","r")
                    b=input("Enter a starting letter:")
                    c=0
                    for d in a:
                        if d.strip()!="" and d.strip()[0].lower()==b.lower():
                            print(d.strip())
                            c+=1
                    a.close()
                    print("Total lines starting with",b,":",c)
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def count_character_occurrence():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.read()
                    a.close()
                    c=input("Enter a character to count:")
                    d=0
                    for e in b:
                        if e.lower()==c.lower():
                            d+=1
                    print("'"+c+"' occurs",d,"time(s) in sample.txt")
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def replace_word_in_file():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.read()
                    a.close()
                    c=input("Enter the word to replace:")
                    d=input("Enter the new word:")
                    e=b.replace(c,d)
                    f=open("sample.txt","w")
                    f.write(e)
                    f.close()
                    print("All occurrences of '"+c+"' replaced with '"+d+"'")
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def longest_word_in_file():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.read()
                    a.close()
                    c=b.split()
                    d=""
                    for e in c:
                        f=e.strip(".,!?")
                        if len(f)>len(d):
                            d=f
                    print("Longest word in sample.txt:",d)
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def count_uppercase_words():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.read()
                    a.close()
                    c=b.split()
                    d=0
                    for e in c:
                        f=e.strip(".,!?")
                        if f.isupper():
                            d+=1
                    print("Words written fully in UPPERCASE in sample.txt:",d)
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def read_specific_line_number():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.readlines()
                    a.close()
                    c=int(input("Enter the line number to read:"))
                    if 1<=c<=len(b):
                        print("Line",c,":",b[c-1].strip())
                    else:
                        print("sample.txt has only",len(b),"line(s)")
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def count_paragraphs():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.read()
                    a.close()
                    c=[d for d in b.split("\n\n") if d.strip()!=""]
                    print("Number of paragraphs in sample.txt:",len(c))
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def display_lines_reverse():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.readlines()
                    a.close()
                    print("Lines of sample.txt in reverse order:")
                    for c in reversed(b):
                        print(c.strip())
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def count_digit_characters():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.read()
                    a.close()
                    c=0
                    for d in b:
                        if d.isdigit():
                            c+=1
                    print("Digit characters in sample.txt:",c)
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def lines_with_word_count_greater_than():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.readlines()
                    a.close()
                    c=int(input("Enter minimum word count:"))
                    print("Lines with more than",c,"word(s):")
                    for d in b:
                        if len(d.split())>c:
                            print(d.strip())
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            def remove_extra_blank_lines():
                print()
                try:
                    a=open("sample.txt","r")
                    b=a.readlines()
                    a.close()
                    c=[d for d in b if d.strip()!=""]
                    e=open("sample.txt","w")
                    e.writelines(c)
                    e.close()
                    print("Blank lines removed from sample.txt")
                except FileNotFoundError:
                    print("sample.txt not found, write to it first")
            print()
            ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for WRITING TO A TEXT FILE\nPRESS 2 for APPENDING TO A TEXT FILE\nPRESS 3 for READING WHOLE FILE\nPRESS 4 for READING LINE BY LINE\nPRESS 5 for WORDS SEPARATED BY #\nPRESS 6 for VOWEL,CONSONANT,CASE COUNT\nPRESS 7 for REMOVE LINES CONTAINING 'a'\nPRESS 8 for SEEK AND TELL\nPRESS 9 for COUNT LINES,WORDS,CHARACTERS\nPRESS 10 for COUNT OCCURRENCE OF A SPECIFIC WORD\nPRESS 11 for COPY FILE CONTENT TO ANOTHER FILE\nPRESS 12 for LINES STARTING WITH A SPECIFIC LETTER\nPRESS 13 for COUNT OCCURRENCE OF A SPECIFIC CHARACTER\nPRESS 14 for REPLACE A WORD IN THE FILE\nPRESS 15 for FIND THE LONGEST WORD IN THE FILE\nPRESS 16 for COUNT WORDS WRITTEN IN UPPERCASE\nPRESS 17 for READ A SPECIFIC LINE NUMBER\nPRESS 18 for COUNT PARAGRAPHS\nPRESS 19 for DISPLAY LINES IN REVERSE ORDER\nPRESS 20 for COUNT DIGIT CHARACTERS IN FILE\nPRESS 21 for LINES WITH WORD COUNT GREATER THAN A GIVEN NUMBER\nPRESS 22 for REMOVE EXTRA BLANK LINES FROM FILE:"))
            if ch==1:
                _code_or_continue(writing_to_text_file)
            elif ch==2:
                _code_or_continue(appending_to_text_file)
            elif ch==3:
                _code_or_continue(reading_whole_file)
            elif ch==4:
                _code_or_continue(reading_line_by_line)
            elif ch==5:
                _code_or_continue(words_separated_by_hash)
            elif ch==6:
                _code_or_continue(counting_vowels_consonants_case)
            elif ch==7:
                _code_or_continue(remove_lines_with_a)
            elif ch==8:
                _code_or_continue(seek_and_tell_demo)
            elif ch==9:
                _code_or_continue(count_lines_words_chars)
            elif ch==10:
                _code_or_continue(word_occurrence_count)
            elif ch==11:
                _code_or_continue(copy_file_content)
            elif ch==12:
                _code_or_continue(lines_starting_with_specific_letter)
            elif ch==13:
                _code_or_continue(count_character_occurrence)
            elif ch==14:
                _code_or_continue(replace_word_in_file)
            elif ch==15:
                _code_or_continue(longest_word_in_file)
            elif ch==16:
                _code_or_continue(count_uppercase_words)
            elif ch==17:
                _code_or_continue(read_specific_line_number)
            elif ch==18:
                _code_or_continue(count_paragraphs)
            elif ch==19:
                _code_or_continue(display_lines_reverse)
            elif ch==20:
                _code_or_continue(count_digit_characters)
            elif ch==21:
                _code_or_continue(lines_with_word_count_greater_than)
            elif ch==22:
                _code_or_continue(remove_extra_blank_lines)

        def binary_file_handling():
            import pickle
            def create_binary_file():
                print()
                a=open("student.dat","wb")
                while True:
                    b=int(input("Enter roll number:"))
                    c=input("Enter name:")
                    d={"roll":b,"name":c}
                    pickle.dump(d,a)
                    e=input("Add another record?(Y/N):")
                    if e in "Nn":
                        break
                a.close()
                print("Records written to student.dat")
            def search_roll_number():
                print()
                try:
                    a=open("student.dat","rb")
                    b=int(input("Enter roll number to search:"))
                    c=False
                    while True:
                        try:
                            d=pickle.load(a)
                        except EOFError:
                            break
                        if d["roll"]==b:
                            print("Name found:",d["name"])
                            c=True
                            break
                    a.close()
                    if not c:
                        print("Roll number not found")
                except FileNotFoundError:
                    print("student.dat not found, create it first")
            def create_binary_file_with_marks():
                print()
                a=open("marks.dat","wb")
                while True:
                    b=int(input("Enter roll number:"))
                    c=input("Enter name:")
                    d=float(input("Enter marks:"))
                    e={"roll":b,"name":c,"marks":d}
                    pickle.dump(e,a)
                    f=input("Add another record?(Y/N):")
                    if f in "Nn":
                        break
                a.close()
                print("Records written to marks.dat")
            def update_marks():
                print()
                try:
                    a=open("marks.dat","rb")
                    b=[]
                    while True:
                        try:
                            b.append(pickle.load(a))
                        except EOFError:
                            break
                    a.close()
                    c=int(input("Enter roll number to update:"))
                    d=False
                    for e in b:
                        if e["roll"]==c:
                            e["marks"]=float(input("Enter new marks:"))
                            d=True
                    if d:
                        f=open("marks.dat","wb")
                        for e in b:
                            pickle.dump(e,f)
                        f.close()
                        print("Marks updated")
                    else:
                        print("Roll number not found")
                except FileNotFoundError:
                    print("marks.dat not found, create it first")
            def read_all_records():
                print()
                try:
                    a=open("student.dat","rb")
                    while True:
                        try:
                            b=pickle.load(a)
                        except EOFError:
                            break
                        print(b)
                    a.close()
                except FileNotFoundError:
                    print("student.dat not found, create it first")
            def delete_record_binary():
                print()
                try:
                    a=open("student.dat","rb")
                    b=[]
                    while True:
                        try:
                            b.append(pickle.load(a))
                        except EOFError:
                            break
                    a.close()
                    c=int(input("Enter roll number to delete:"))
                    d=[e for e in b if e["roll"]!=c]
                    if len(d)==len(b):
                        print("Roll number not found")
                    else:
                        f=open("student.dat","wb")
                        for e in d:
                            pickle.dump(e,f)
                        f.close()
                        print("Record deleted")
                except FileNotFoundError:
                    print("student.dat not found, create it first")
            def append_record_binary():
                print()
                a=open("student.dat","ab")
                b=int(input("Enter roll number:"))
                c=input("Enter name:")
                pickle.dump({"roll":b,"name":c},a)
                a.close()
                print("Record appended to student.dat")
            def display_high_scorers_binary():
                print()
                try:
                    a=open("marks.dat","rb")
                    while True:
                        try:
                            b=pickle.load(a)
                        except EOFError:
                            break
                        if b["marks"]>75:
                            print(b)
                    a.close()
                except FileNotFoundError:
                    print("marks.dat not found, create it first")
            def count_total_records():
                print()
                try:
                    a=open("student.dat","rb")
                    b=0
                    while True:
                        try:
                            pickle.load(a)
                            b+=1
                        except EOFError:
                            break
                    a.close()
                    print("Total records in student.dat:",b)
                except FileNotFoundError:
                    print("student.dat not found, create it first")
            def update_entire_record_by_roll():
                print()
                try:
                    a=open("student.dat","rb")
                    b=[]
                    while True:
                        try:
                            b.append(pickle.load(a))
                        except EOFError:
                            break
                    a.close()
                    c=int(input("Enter roll number to update:"))
                    d=False
                    for e in b:
                        if e["roll"]==c:
                            e["name"]=input("Enter new name:")
                            d=True
                    if d:
                        f=open("student.dat","wb")
                        for e in b:
                            pickle.dump(e,f)
                        f.close()
                        print("Record updated")
                    else:
                        print("Roll number not found")
                except FileNotFoundError:
                    print("student.dat not found, create it first")
            def search_by_name_binary():
                print()
                try:
                    a=open("student.dat","rb")
                    b=input("Enter name to search:")
                    c=False
                    while True:
                        try:
                            d=pickle.load(a)
                        except EOFError:
                            break
                        if d["name"].lower()==b.lower():
                            print("Record found:",d)
                            c=True
                    a.close()
                    if not c:
                        print("Name not found")
                except FileNotFoundError:
                    print("student.dat not found, create it first")
            def average_marks_binary():
                print()
                try:
                    a=open("marks.dat","rb")
                    b=0
                    c=0
                    while True:
                        try:
                            d=pickle.load(a)
                        except EOFError:
                            break
                        b+=d["marks"]
                        c+=1
                    a.close()
                    if c==0:
                        print("No records found in marks.dat")
                    else:
                        print("Average marks of",c,"student(s):",b/c)
                except FileNotFoundError:
                    print("marks.dat not found, create it first")
            def find_topper_binary():
                print()
                try:
                    a=open("marks.dat","rb")
                    b=None
                    while True:
                        try:
                            c=pickle.load(a)
                        except EOFError:
                            break
                        if b is None or c["marks"]>b["marks"]:
                            b=c
                    a.close()
                    if b is None:
                        print("No records found in marks.dat")
                    else:
                        print("Topper record:",b)
                except FileNotFoundError:
                    print("marks.dat not found, create it first")
            def copy_passed_students_binary():
                print()
                try:
                    a=open("marks.dat","rb")
                    b=open("pass.dat","wb")
                    c=0
                    while True:
                        try:
                            d=pickle.load(a)
                        except EOFError:
                            break
                        if d["marks"]>=33:
                            pickle.dump(d,b)
                            c+=1
                    a.close()
                    b.close()
                    print(c,"passed student(s) copied to pass.dat")
                except FileNotFoundError:
                    print("marks.dat not found, create it first")
            def count_failed_students():
                print()
                try:
                    a=open("marks.dat","rb")
                    b=0
                    while True:
                        try:
                            c=pickle.load(a)
                        except EOFError:
                            break
                        if c["marks"]<33:
                            b+=1
                    a.close()
                    print("Failed student(s) in marks.dat:",b)
                except FileNotFoundError:
                    print("marks.dat not found, create it first")
            def sort_records_by_marks():
                print()
                try:
                    a=open("marks.dat","rb")
                    b=[]
                    while True:
                        try:
                            b.append(pickle.load(a))
                        except EOFError:
                            break
                    a.close()
                    b.sort(key=lambda c:c["marks"],reverse=True)
                    d=open("marks.dat","wb")
                    for c in b:
                        pickle.dump(c,d)
                    d.close()
                    print("Records in marks.dat sorted by marks(descending):")
                    for c in b:
                        print(c)
                except FileNotFoundError:
                    print("marks.dat not found, create it first")
            def display_nth_record():
                print()
                try:
                    a=open("student.dat","rb")
                    b=[]
                    while True:
                        try:
                            b.append(pickle.load(a))
                        except EOFError:
                            break
                    a.close()
                    c=int(input("Enter record position(1-based):"))
                    if 1<=c<=len(b):
                        print("Record",c,":",b[c-1])
                    else:
                        print("student.dat has only",len(b),"record(s)")
                except FileNotFoundError:
                    print("student.dat not found, create it first")
            def merge_two_binary_files():
                print()
                try:
                    a=open("student.dat","rb")
                    b=[]
                    while True:
                        try:
                            b.append(pickle.load(a))
                        except EOFError:
                            break
                    a.close()
                    c=open("pass.dat","rb")
                    d=[]
                    while True:
                        try:
                            d.append(pickle.load(c))
                        except EOFError:
                            break
                    c.close()
                    e=open("merged.dat","wb")
                    for f in b+d:
                        pickle.dump(f,e)
                    e.close()
                    print(len(b)+len(d),"record(s) merged into merged.dat")
                except FileNotFoundError:
                    print("student.dat or pass.dat not found, create them first")
            def remove_duplicate_records():
                print()
                try:
                    a=open("student.dat","rb")
                    b=[]
                    while True:
                        try:
                            b.append(pickle.load(a))
                        except EOFError:
                            break
                    a.close()
                    c=[]
                    d=set()
                    for e in b:
                        if e["roll"] not in d:
                            c.append(e)
                            d.add(e["roll"])
                    f=open("student.dat","wb")
                    for e in c:
                        pickle.dump(e,f)
                    f.close()
                    print(len(b)-len(c),"duplicate record(s) removed from student.dat")
                except FileNotFoundError:
                    print("student.dat not found, create it first")
            print()
            ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for CREATE BINARY FILE(ROLL,NAME)\nPRESS 2 for SEARCH ROLL NUMBER\nPRESS 3 for CREATE BINARY FILE(ROLL,NAME,MARKS)\nPRESS 4 for UPDATE MARKS\nPRESS 5 for READ ALL RECORDS\nPRESS 6 for DELETE A RECORD\nPRESS 7 for APPEND A RECORD\nPRESS 8 for DISPLAY RECORDS WITH MARKS>75\nPRESS 9 for COUNT TOTAL RECORDS\nPRESS 10 for UPDATE ENTIRE RECORD BY ROLL NUMBER\nPRESS 11 for SEARCH A RECORD BY NAME\nPRESS 12 for AVERAGE MARKS FROM A BINARY FILE\nPRESS 13 for FIND THE TOPPER(HIGHEST MARKS)\nPRESS 14 for COPY PASSED STUDENTS TO A NEW BINARY FILE\nPRESS 15 for COUNT FAILED STUDENTS(MARKS<33)\nPRESS 16 for SORT RECORDS BY MARKS AND REWRITE THE FILE\nPRESS 17 for DISPLAY NTH RECORD FROM THE FILE\nPRESS 18 for MERGE TWO BINARY FILES INTO A THIRD FILE\nPRESS 19 for REMOVE DUPLICATE RECORDS BY ROLL NUMBER:"))
            if ch==1:
                _code_or_continue(create_binary_file)
            elif ch==2:
                _code_or_continue(search_roll_number)
            elif ch==3:
                _code_or_continue(create_binary_file_with_marks)
            elif ch==4:
                _code_or_continue(update_marks)
            elif ch==5:
                _code_or_continue(read_all_records)
            elif ch==6:
                _code_or_continue(delete_record_binary)
            elif ch==7:
                _code_or_continue(append_record_binary)
            elif ch==8:
                _code_or_continue(display_high_scorers_binary)
            elif ch==9:
                _code_or_continue(count_total_records)
            elif ch==10:
                _code_or_continue(update_entire_record_by_roll)
            elif ch==11:
                _code_or_continue(search_by_name_binary)
            elif ch==12:
                _code_or_continue(average_marks_binary)
            elif ch==13:
                _code_or_continue(find_topper_binary)
            elif ch==14:
                _code_or_continue(copy_passed_students_binary)
            elif ch==15:
                _code_or_continue(count_failed_students)
            elif ch==16:
                _code_or_continue(sort_records_by_marks)
            elif ch==17:
                _code_or_continue(display_nth_record)
            elif ch==18:
                _code_or_continue(merge_two_binary_files)
            elif ch==19:
                _code_or_continue(remove_duplicate_records)

        def csv_file_handling():
            import csv
            def create_csv_file():
                print()
                a=open("login.csv","w",newline="")
                b=csv.writer(a)
                b.writerow(["userid","password"])
                while True:
                    c=input("Enter user id:")
                    d=input("Enter password:")
                    b.writerow([c,d])
                    e=input("Add another record?(Y/N):")
                    if e in "Nn":
                        break
                a.close()
                print("Data written to login.csv")
            def search_password():
                print()
                try:
                    a=open("login.csv","r",newline="")
                    b=csv.reader(a)
                    next(b)
                    c=input("Enter user id to search:")
                    d=False
                    for e in b:
                        if e[0]==c:
                            print("Password:",e[1])
                            d=True
                            break
                    a.close()
                    if not d:
                        print("User id not found")
                except FileNotFoundError:
                    print("login.csv not found, create it first")
            def writerows_demo():
                print()
                a=open("marks.csv","w",newline="")
                b=csv.writer(a)
                b.writerow(["name","marks"])
                c=[]
                while True:
                    d=input("Enter name:")
                    e=float(input("Enter marks:"))
                    c.append([d,e])
                    f=input("Add another record?(Y/N):")
                    if f in "Nn":
                        break
                b.writerows(c)
                a.close()
                print("Data written to marks.csv using writerows()")
            def reading_csv_file():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    for c in b:
                        print(c)
                    a.close()
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def update_csv_record():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=list(b)
                    a.close()
                    d=input("Enter name to update marks for:")
                    e=False
                    for f in c[1:]:
                        if f[0]==d:
                            f[1]=input("Enter new marks:")
                            e=True
                    if e:
                        g=open("marks.csv","w",newline="")
                        h=csv.writer(g)
                        h.writerows(c)
                        g.close()
                        print("Marks updated")
                    else:
                        print("Name not found")
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def append_csv_record():
                print()
                a=open("marks.csv","a",newline="")
                b=csv.writer(a)
                c=input("Enter name:")
                d=float(input("Enter marks:"))
                b.writerow([c,d])
                a.close()
                print("Record appended to marks.csv")
            def dictwriter_dictreader_demo():
                print()
                a=open("emp.csv","w",newline="")
                b=["empid","name","salary"]
                c=csv.DictWriter(a,fieldnames=b)
                c.writeheader()
                while True:
                    d=input("Enter employee id:")
                    e=input("Enter name:")
                    f=float(input("Enter salary:"))
                    c.writerow({"empid":d,"name":e,"salary":f})
                    g=input("Add another record?(Y/N):")
                    if g in "Nn":
                        break
                a.close()
                print("Reading back using DictReader:")
                h=open("emp.csv","r",newline="")
                i=csv.DictReader(h)
                for j in i:
                    print(j["empid"],j["name"],j["salary"])
                h.close()
            def count_csv_records():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=list(b)
                    a.close()
                    print("Total data records(excluding header):",len(c)-1)
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def csv_average_marks():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=list(b)
                    a.close()
                    d=c[1:]
                    if len(d)==0:
                        print("No data records in marks.csv")
                    else:
                        e=0
                        for f in d:
                            e+=float(f[1])
                        print("Average marks:",e/len(d))
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def csv_filter_high_scorers():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=list(b)
                    a.close()
                    print("Students with marks>75:")
                    for d in c[1:]:
                        if float(d[1])>75:
                            print(d)
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def csv_find_topper():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=list(b)
                    a.close()
                    d=c[1:]
                    if len(d)==0:
                        print("No data records in marks.csv")
                    else:
                        e=d[0]
                        for f in d:
                            if float(f[1])>float(e[1]):
                                e=f
                        print("Topper record from marks.csv:",e)
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def csv_sort_by_marks_descending():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=list(b)
                    a.close()
                    d=c[0]
                    e=c[1:]
                    e.sort(key=lambda f:float(f[1]),reverse=True)
                    print("Records sorted by marks(descending):")
                    print(d)
                    for f in e:
                        print(f)
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def count_csv_fields():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=next(b)
                    a.close()
                    print("Number of fields(columns) in marks.csv:",len(c))
                    print("Field names:",c)
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def delete_csv_record_by_name():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=list(b)
                    a.close()
                    d=input("Enter name to delete:")
                    e=[f for f in c[1:] if f[0]!=d]
                    if len(e)==len(c)-1:
                        print("Name not found")
                    else:
                        g=open("marks.csv","w",newline="")
                        h=csv.writer(g)
                        h.writerow(c[0])
                        h.writerows(e)
                        g.close()
                        print("Record deleted from marks.csv")
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def csv_marks_between_range():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=list(b)
                    a.close()
                    d=float(input("Enter lower marks limit:"))
                    e=float(input("Enter upper marks limit:"))
                    print("Students with marks between",d,"and",e,":")
                    for f in c[1:]:
                        if d<=float(f[1])<=e:
                            print(f)
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def csv_to_list_of_dicts_manual():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=list(b)
                    a.close()
                    d=c[0]
                    e=[]
                    for f in c[1:]:
                        g=dict(zip(d,f))
                        e.append(g)
                    print("marks.csv converted to a list of dictionaries:")
                    for g in e:
                        print(g)
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            def csv_count_duplicate_names():
                print()
                try:
                    a=open("marks.csv","r",newline="")
                    b=csv.reader(a)
                    c=list(b)
                    a.close()
                    d={}
                    for e in c[1:]:
                        d[e[0]]=d.get(e[0],0)+1
                    f=0
                    for g in d:
                        if d[g]>1:
                            print(g,"appears",d[g],"times")
                            f+=1
                    if f==0:
                        print("No duplicate names found in marks.csv")
                except FileNotFoundError:
                    print("marks.csv not found, create it first")
            print()
            ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for CREATE CSV(USERID,PASSWORD)\nPRESS 2 for SEARCH PASSWORD BY USERID\nPRESS 3 for WRITEROWS DEMO\nPRESS 4 for READING A CSV FILE\nPRESS 5 for UPDATE A RECORD\nPRESS 6 for APPEND A RECORD('a' MODE)\nPRESS 7 for DictWriter and DictReader DEMO\nPRESS 8 for COUNT TOTAL DATA RECORDS\nPRESS 9 for AVERAGE MARKS FROM A CSV FILE\nPRESS 10 for FILTER STUDENTS WITH MARKS>75\nPRESS 11 for FIND THE TOPPER FROM A CSV FILE\nPRESS 12 for SORT CSV RECORDS BY MARKS(DESCENDING)\nPRESS 13 for COUNT NUMBER OF FIELDS(COLUMNS)\nPRESS 14 for DELETE A RECORD BY NAME\nPRESS 15 for STUDENTS WITH MARKS BETWEEN TWO VALUES\nPRESS 16 for CONVERT CSV TO A LIST OF DICTIONARIES(MANUAL)\nPRESS 17 for COUNT DUPLICATE NAMES IN CSV:"))
            if ch==1:
                _code_or_continue(create_csv_file)
            elif ch==2:
                _code_or_continue(search_password)
            elif ch==3:
                _code_or_continue(writerows_demo)
            elif ch==4:
                _code_or_continue(reading_csv_file)
            elif ch==5:
                _code_or_continue(update_csv_record)
            elif ch==6:
                _code_or_continue(append_csv_record)
            elif ch==7:
                _code_or_continue(dictwriter_dictreader_demo)
            elif ch==8:
                _code_or_continue(count_csv_records)
            elif ch==9:
                _code_or_continue(csv_average_marks)
            elif ch==10:
                _code_or_continue(csv_filter_high_scorers)
            elif ch==11:
                _code_or_continue(csv_find_topper)
            elif ch==12:
                _code_or_continue(csv_sort_by_marks_descending)
            elif ch==13:
                _code_or_continue(count_csv_fields)
            elif ch==14:
                _code_or_continue(delete_csv_record_by_name)
            elif ch==15:
                _code_or_continue(csv_marks_between_range)
            elif ch==16:
                _code_or_continue(csv_to_list_of_dicts_manual)
            elif ch==17:
                _code_or_continue(csv_count_duplicate_names)

        def stack_operations():
            def push_pop_demo():
                print()
                a=[]
                while True:
                    b=int(input("PRESS 1 to PUSH\nPRESS 2 to POP\nPRESS 3 to PEEK\nPRESS 4 to DISPLAY\nPRESS 5 to EXIT:"))
                    if b==1:
                        c=input("Enter element to push:")
                        a.append(c)
                        print("Pushed",c)
                    elif b==2:
                        if a==[]:
                            print("Stack is empty(Underflow)")
                        else:
                            print("Popped:",a.pop())
                    elif b==3:
                        if a==[]:
                            print("Stack is empty")
                        else:
                            print("Top of stack:",a[-1])
                    elif b==4:
                        print("Stack:",a)
                    elif b==5:
                        break
            def reverse_string_using_stack():
                print()
                a=input("Enter a string:")
                b=[]
                for c in a:
                    b.append(c)
                d=""
                while b!=[]:
                    d+=b.pop()
                print("Reversed string:",d)
            def balanced_parentheses():
                print()
                a=input("Enter an expression:")
                b=[]
                c=True
                for d in a:
                    if d in "({[":
                        b.append(d)
                    elif d in ")}]":
                        if b==[]:
                            c=False
                            break
                        else:
                            b.pop()
                if b!=[]:
                    c=False
                if c:
                    print("Parentheses are balanced")
                else:
                    print("Parentheses are not balanced")
            def stack_selective_push():
                def push_high_scorers(a,b):
                    for c in a:
                        if c["marks"]>75:
                            b.append(c["name"])
                print()
                a=[]
                while True:
                    b=input("Enter student name:")
                    c=float(input("Enter marks:"))
                    a.append({"name":b,"marks":c})
                    d=input("Add another student?(Y/N):")
                    if d in "Nn":
                        break
                e=[]
                push_high_scorers(a,e)
                print("Stack after pushing students with marks>75:",e)
                while e!=[]:
                    print("Popped:",e.pop())
            def decimal_to_binary_using_stack():
                print()
                a=int(input("Enter a decimal number:"))
                b=a
                c=[]
                if a==0:
                    c.append(0)
                while a>0:
                    c.append(a%2)
                    a=a//2
                d=""
                while c!=[]:
                    d+=str(c.pop())
                print("Binary equivalent of",b,"using stack:",d)
            def stack_using_class():
                class Stack:
                    def __init__(self):
                        self.items=[]
                    def push(self,a):
                        self.items.append(a)
                    def pop(self):
                        if self.isempty():
                            return None
                        return self.items.pop()
                    def peek(self):
                        if self.isempty():
                            return None
                        return self.items[-1]
                    def isempty(self):
                        return self.items==[]
                    def display(self):
                        print("Stack:",self.items)
                print()
                print("Stack implemented as a CLASS with push/pop/peek/display methods.")
                a=Stack()
                while True:
                    b=int(input("PRESS 1 to PUSH\nPRESS 2 to POP\nPRESS 3 to PEEK\nPRESS 4 to DISPLAY\nPRESS 5 to EXIT:"))
                    if b==1:
                        c=input("Enter element to push:")
                        a.push(c)
                    elif b==2:
                        d=a.pop()
                        if d is None:
                            print("Stack is empty(Underflow)")
                        else:
                            print("Popped:",d)
                    elif b==3:
                        e=a.peek()
                        if e is None:
                            print("Stack is empty")
                        else:
                            print("Top of stack:",e)
                    elif b==4:
                        a.display()
                    elif b==5:
                        break
            def push_prime_numbers_demo():
                def is_prime(a):
                    if a<2:
                        return False
                    for b in range(2,int(a**0.5)+1):
                        if a%b==0:
                            return False
                    return True
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                c=[]
                for d in b:
                    if is_prime(d):
                        c.append(d)
                print("Stack after pushing only prime numbers:",c)
                while c!=[]:
                    print("Popped:",c.pop())
            def palindrome_check_using_stack():
                print()
                a=input("Enter a string:")
                b=a.replace(" ","").lower()
                c=[]
                for d in b:
                    c.append(d)
                e=""
                while c!=[]:
                    e+=c.pop()
                if e==b:
                    print(a,"is a palindrome(checked by popping a stack)")
                else:
                    print(a,"is not a palindrome(checked by popping a stack)")
            def postfix_evaluation_using_stack():
                print()
                print("Enter a POSTFIX expression with space-separated tokens,")
                print("for example: 5 3 + 2 *")
                a=input("Enter postfix expression:").split()
                b=[]
                for c in a:
                    if c in "+-*/":
                        d=b.pop()
                        e=b.pop()
                        if c=="+":
                            b.append(e+d)
                        elif c=="-":
                            b.append(e-d)
                        elif c=="*":
                            b.append(e*d)
                        else:
                            b.append(e/d)
                    else:
                        b.append(int(c))
                print("Result of postfix expression using a stack:",b.pop())
            print()
            ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for PUSH AND POP OPERATIONS\nPRESS 2 for REVERSE A STRING USING STACK\nPRESS 3 for CHECK BALANCED PARENTHESES\nPRESS 4 for PUSH STUDENTS WITH MARKS>75(CONDITIONAL PUSH)\nPRESS 5 for DECIMAL TO BINARY USING STACK\nPRESS 6 for STACK IMPLEMENTED USING A CLASS\nPRESS 7 for PUSH ONLY PRIME NUMBERS(CONDITIONAL PUSH)\nPRESS 8 for PALINDROME CHECK USING A STACK\nPRESS 9 for POSTFIX EXPRESSION EVALUATION USING A STACK:"))
            if ch==1:
                _code_or_continue(push_pop_demo)
            elif ch==2:
                _code_or_continue(reverse_string_using_stack)
            elif ch==3:
                _code_or_continue(balanced_parentheses)
            elif ch==4:
                _code_or_continue(stack_selective_push)
            elif ch==5:
                _code_or_continue(decimal_to_binary_using_stack)
            elif ch==6:
                _code_or_continue(stack_using_class)
            elif ch==7:
                _code_or_continue(push_prime_numbers_demo)
            elif ch==8:
                _code_or_continue(palindrome_check_using_stack)
            elif ch==9:
                _code_or_continue(postfix_evaluation_using_stack)

        def sql_ddl_dml():
            SQL = {
                1: ("DATABASE COMMANDS(CREATE,USE,SHOW,DROP)", """
CREATE DATABASE school;

USE school;

SHOW DATABASES;

SHOW TABLES;

DESCRIBE student;

DROP TABLE student;

DROP DATABASE school;
"""),
                2: ("CREATE TABLE AND INSERT", """
CREATE TABLE student(
    rollno INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    marks FLOAT,
    city VARCHAR(30),
    grade VARCHAR(5) UNIQUE
);

INSERT INTO student(rollno,name,marks,city) VALUES(1,'Aditi',88.5,'Delhi');
INSERT INTO student(rollno,name,marks,city) VALUES(2,'Rohan',45.0,'Mumbai');
"""),
                3: ("ALTER TABLE", """
ALTER TABLE student ADD COLUMN remarks VARCHAR(30);

ALTER TABLE student DROP COLUMN remarks;

ALTER TABLE student ADD PRIMARY KEY(rollno);

ALTER TABLE student DROP PRIMARY KEY;
"""),
                4: ("UPDATE", """
UPDATE student SET marks=95 WHERE rollno=1;
"""),
                5: ("DELETE", """
DELETE FROM student WHERE rollno=2;
"""),
                6: ("ORDER BY", """
SELECT * FROM student ORDER BY marks ASC;

SELECT * FROM student ORDER BY marks DESC;
"""),
                7: ("GROUP BY WITH AGGREGATE FUNCTIONS", """
SELECT city,COUNT(*),MIN(marks),MAX(marks),SUM(marks),AVG(marks)
FROM student
GROUP BY city;
"""),
                8: ("CONSTRAINTS(NOT NULL,DEFAULT,CHECK,UNIQUE)", """
CREATE TABLE employee(
    empid INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    dept VARCHAR(20) DEFAULT 'General',
    salary FLOAT CHECK(salary>0),
    email VARCHAR(40) UNIQUE
);
"""),
                9: ("INSERT INTO...SELECT", """
CREATE TABLE topper(rollno INT,name VARCHAR(30),marks FLOAT);

INSERT INTO topper(rollno,name,marks)
SELECT rollno,name,marks FROM student WHERE marks>=90;
"""),
                10: ("RENAME TABLE / MODIFY COLUMN", """
ALTER TABLE student RENAME TO students;

ALTER TABLE students MODIFY marks DECIMAL(5,2);

ALTER TABLE students RENAME COLUMN city TO location;
"""),
                11: ("FOREIGN KEY AND TRUNCATE", """
CREATE TABLE hobby(
    rollno INT,
    hobby VARCHAR(30),
    FOREIGN KEY(rollno) REFERENCES student(rollno)
);

TRUNCATE TABLE hobby;
"""),
                12: ("COMPOSITE PRIMARY KEY", """
CREATE TABLE enrolment(
    rollno INT,
    subject_code INT,
    grade VARCHAR(5),
    PRIMARY KEY(rollno,subject_code)
);
"""),
                13: ("MULTI-ROW INSERT USING A SINGLE VALUES LIST", """
INSERT INTO student(rollno,name,marks,city) VALUES
(3,'Meera',72.0,'Chennai'),
(4,'Kabir',60.5,'Delhi'),
(5,'Zara',91.2,'Pune');
"""),
            }
            print()
            print("NOTE: plain SQL commands only — nothing is executed.")
            ch=int(input("WHAT DO YOU WANT TO SEE\nPRESS 1 for DATABASE COMMANDS(CREATE,USE,SHOW,DROP)\nPRESS 2 for CREATE TABLE AND INSERT DATA\nPRESS 3 for ALTER TABLE\nPRESS 4 for UPDATE COMMAND\nPRESS 5 for DELETE COMMAND\nPRESS 6 for ORDER BY\nPRESS 7 for GROUP BY WITH AGGREGATE FUNCTIONS\nPRESS 8 for CONSTRAINTS(NOT NULL,DEFAULT,CHECK,UNIQUE)\nPRESS 9 for INSERT INTO...SELECT\nPRESS 10 for RENAME TABLE / MODIFY COLUMN\nPRESS 11 for FOREIGN KEY AND TRUNCATE\nPRESS 12 for COMPOSITE PRIMARY KEY\nPRESS 13 for MULTI-ROW INSERT USING A SINGLE VALUES LIST:"))
            if ch in SQL:
                _show_sql(*SQL[ch])

        def sql_queries():
            SQL = {
                1: ("SELECT ALL / DISTINCT", """
SELECT * FROM student;

SELECT DISTINCT city FROM student;
"""),
                2: ("ALIASING AND OPERATORS", """
SELECT name AS student_name, marks AS score FROM student;

SELECT name, marks, marks+5 AS marks_with_bonus FROM student;

SELECT * FROM student WHERE marks>50 AND city='Delhi';
"""),
                3: ("WHERE CLAUSE", """
SELECT * FROM student WHERE marks>=50;
"""),
                4: ("BETWEEN AND IN", """
SELECT * FROM student WHERE marks BETWEEN 40 AND 90;

SELECT * FROM student WHERE city IN ('Delhi','Mumbai');
"""),
                5: ("LIKE (PATTERN MATCHING)", """
SELECT * FROM student WHERE name LIKE 'A%';
"""),
                6: ("NULL HANDLING", """
SELECT * FROM student WHERE grade IS NULL;

SELECT * FROM student WHERE grade IS NOT NULL;
"""),
                7: ("AGGREGATE FUNCTIONS", """
SELECT MAX(marks),MIN(marks),AVG(marks),SUM(marks),COUNT(*) FROM student;
"""),
                8: ("GROUP BY WITH HAVING", """
SELECT city,AVG(marks)
FROM student
GROUP BY city
HAVING AVG(marks)>=50;
"""),
                9: ("JOINS", """
CREATE TABLE hobby(rollno INT, hobby VARCHAR(30));

-- Cartesian Product
SELECT * FROM student,hobby;

-- Equi-Join
SELECT student.rollno,name,hobby
FROM student,hobby
WHERE student.rollno=hobby.rollno;

-- Natural Join
SELECT * FROM student NATURAL JOIN hobby;
"""),
                10: ("SUBQUERIES", """
SELECT name,marks FROM student
WHERE marks>(SELECT AVG(marks) FROM student);

SELECT name FROM student
WHERE rollno IN (SELECT rollno FROM hobby WHERE hobby='Chess');
"""),
                11: ("DATE AND STRING FUNCTIONS", """
SELECT NOW();

SELECT CURDATE();

SELECT UCASE(name),LCASE(city) FROM student;

SELECT name,LENGTH(name) FROM student;
"""),
                12: ("VIEWS", """
CREATE VIEW topper_view AS
SELECT rollno,name,marks FROM student WHERE marks>=90;

SELECT * FROM topper_view;

DROP VIEW topper_view;
"""),
                13: ("GROUP BY WITH ORDER BY(COMBINED)", """
SELECT city,COUNT(*) AS total_students,AVG(marks) AS avg_marks
FROM student
GROUP BY city
ORDER BY avg_marks DESC;
"""),
                14: ("LIMIT AND OFFSET", """
SELECT * FROM student ORDER BY marks DESC LIMIT 3;

SELECT * FROM student ORDER BY marks DESC LIMIT 3 OFFSET 2;
"""),
                15: ("CASE WHEN(CONDITIONAL EXPRESSION)", """
SELECT name,marks,
CASE
    WHEN marks>=90 THEN 'A1'
    WHEN marks>=75 THEN 'A2'
    WHEN marks>=60 THEN 'B1'
    ELSE 'Needs improvement'
END AS grade
FROM student;
"""),
            }
            print()
            print("NOTE: plain SQL commands only — nothing is executed.")
            ch=int(input("WHAT DO YOU WANT TO SEE\nPRESS 1 for SELECT ALL / DISTINCT\nPRESS 2 for ALIASING AND OPERATORS\nPRESS 3 for WHERE CLAUSE\nPRESS 4 for BETWEEN AND IN\nPRESS 5 for LIKE(PATTERN MATCHING)\nPRESS 6 for NULL HANDLING\nPRESS 7 for AGGREGATE FUNCTIONS\nPRESS 8 for GROUP BY WITH HAVING\nPRESS 9 for JOINS\nPRESS 10 for SUBQUERIES\nPRESS 11 for DATE AND STRING FUNCTIONS\nPRESS 12 for VIEWS\nPRESS 13 for GROUP BY WITH ORDER BY(COMBINED)\nPRESS 14 for LIMIT AND OFFSET\nPRESS 15 for CASE WHEN(CONDITIONAL EXPRESSION):"))
            if ch in SQL:
                _show_sql(*SQL[ch])

        def python_sql_connectivity():
            def connect_cursor_execute_fetchall():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM student")
                rows=cursor.fetchall()
                for row in rows:
                    print(row)
                conn.close()
            def fetchone_and_rowcount():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM student")
                row=cursor.fetchone()
                while row:
                    print(row)
                    row=cursor.fetchone()
                cursor.execute("SELECT * FROM student")
                cursor.fetchall()
                print("rowcount:",cursor.rowcount)
                conn.close()
            def parameterised_insert():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                rollno=int(input("Enter roll number:"))
                name=input("Enter name:")
                marks=float(input("Enter marks:"))
                city=input("Enter city:")
                query="INSERT INTO student(rollno,name,marks,city) VALUES(%s,%s,%s,%s)"
                cursor.execute(query,(rollno,name,marks,city))
                conn.commit()
                print("Rows inserted:",cursor.rowcount)
                conn.close()
            def update_using_cursor_commit():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                rollno=int(input("Enter roll number:"))
                marks=float(input("Enter new marks:"))
                cursor.execute("UPDATE student SET marks=%s WHERE rollno=%s",(marks,rollno))
                conn.commit()
                print("Rows affected:",cursor.rowcount)
                conn.close()
            def format_specifier_demo():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                rollno=int(input("Enter roll number to delete:"))
                query="DELETE FROM student WHERE rollno={}".format(rollno)
                cursor.execute(query)
                conn.commit()
                print("Rows affected:",cursor.rowcount)
                conn.close()
            def fetchmany_demo():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM student")
                rows=cursor.fetchmany(2)
                for row in rows:
                    print(row)
                conn.close()
            def parameterised_select_search():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                city=input("Enter city to search:")
                query="SELECT * FROM student WHERE city=%s"
                cursor.execute(query,(city,))
                rows=cursor.fetchall()
                for row in rows:
                    print(row)
                print("Rows found:",cursor.rowcount)
                conn.close()
            def executemany_demo():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                data=[]
                while True:
                    rollno=int(input("Enter roll number:"))
                    name=input("Enter name:")
                    marks=float(input("Enter marks:"))
                    city=input("Enter city:")
                    data.append((rollno,name,marks,city))
                    more=input("Add another record?(Y/N):")
                    if more in "Nn":
                        break
                query="INSERT INTO student(rollno,name,marks,city) VALUES(%s,%s,%s,%s)"
                cursor.executemany(query,data)
                conn.commit()
                print("Rows inserted using executemany():",cursor.rowcount)
                conn.close()
            def delete_using_parameterised_query():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                city=input("Enter city, all matching students will be deleted:")
                query="DELETE FROM student WHERE city=%s"
                cursor.execute(query,(city,))
                conn.commit()
                print("Rows deleted:",cursor.rowcount)
                conn.close()
            def aggregate_query_demo():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                cursor.execute("SELECT AVG(marks),MAX(marks),MIN(marks) FROM student")
                row=cursor.fetchone()
                print("Average:",row[0],"Maximum:",row[1],"Minimum:",row[2])
                conn.close()
            def commit_and_rollback_demo():
                import mysql.connector
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="school")
                cursor=conn.cursor()
                try:
                    rollno=int(input("Enter roll number to update:"))
                    marks=float(input("Enter new marks:"))
                    cursor.execute("UPDATE student SET marks=%s WHERE rollno=%s",(marks,rollno))
                    conn.commit()
                    print("Changes saved permanently using commit()")
                except Exception as e:
                    conn.rollback()
                    print("Error occurred, changes undone using rollback():",e)
                conn.close()
            print()
            print("NOTE: code only — nothing is executed against a database.")
            ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for CONNECT,CURSOR,EXECUTE,FETCHALL\nPRESS 2 for FETCHONE AND ROWCOUNT\nPRESS 3 for PARAMETERISED INSERT QUERY(%s)\nPRESS 4 for UPDATE USING CURSOR AND COMMIT\nPRESS 5 for QUERY BUILT USING format()\nPRESS 6 for FETCHMANY DEMO\nPRESS 7 for PARAMETERISED SELECT(SEARCH BY CITY)\nPRESS 8 for INSERTING MULTIPLE ROWS USING executemany()\nPRESS 9 for PARAMETERISED DELETE QUERY\nPRESS 10 for AGGREGATE QUERY THROUGH PYTHON(AVG,MAX,MIN)\nPRESS 11 for COMMIT AND ROLLBACK DEMO:"))
            if ch==1:
                _show_code(connect_cursor_execute_fetchall)
            elif ch==2:
                _show_code(fetchone_and_rowcount)
            elif ch==3:
                _show_code(parameterised_insert)
            elif ch==4:
                _show_code(update_using_cursor_commit)
            elif ch==5:
                _show_code(format_specifier_demo)
            elif ch==6:
                _show_code(fetchmany_demo)
            elif ch==7:
                _show_code(parameterised_select_search)
            elif ch==8:
                _show_code(executemany_demo)
            elif ch==9:
                _show_code(delete_using_parameterised_query)
            elif ch==10:
                _show_code(aggregate_query_demo)
            elif ch==11:
                _show_code(commit_and_rollback_demo)

        def miscellaneous_programs():
            def dice_simulator():
                import random
                print()
                a=input("Roll the dice?(Y/N):")
                while a in "Yy":
                    print("You rolled:",random.randint(1,6))
                    a=input("Roll again?(Y/N):")
            def prime_number_check():
                print()
                a=int(input("Enter a number:"))
                b=True
                if a<2:
                    b=False
                else:
                    for c in range(2,int(a**0.5)+1):
                        if a%c==0:
                            b=False
                            break
                if b:
                    print(a,"is a prime number")
                else:
                    print(a,"is not a prime number")
            def palindrome_check():
                print()
                a=input("Enter a string:")
                b=a.replace(" ","").lower()
                if b==b[::-1]:
                    print(a,"is a palindrome")
                else:
                    print(a,"is not a palindrome")
            def bubble_sort_demo():
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                c=len(b)
                for d in range(c-1):
                    for e in range(c-1-d):
                        if b[e]>b[e+1]:
                            b[e],b[e+1]=b[e+1],b[e]
                print("Sorted list using bubble sort:",b)
            def matrix_addition():
                print()
                a=int(input("Enter number of rows:"))
                b=int(input("Enter number of columns:"))
                print("Enter elements of first matrix:")
                c=[[int(input("Element ["+str(i)+"]["+str(j)+"]:")) for j in range(b)] for i in range(a)]
                print("Enter elements of second matrix:")
                d=[[int(input("Element ["+str(i)+"]["+str(j)+"]:")) for j in range(b)] for i in range(a)]
                e=[[c[i][j]+d[i][j] for j in range(b)] for i in range(a)]
                print("Sum of the two matrices:")
                for f in e:
                    print(f)
            def linear_search_demo():
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                c=int(input("Enter number to search:"))
                d=-1
                for e in range(len(b)):
                    if b[e]==c:
                        d=e
                        break
                if d==-1:
                    print("Number not found")
                else:
                    print("Number found at index:",d)
            def armstrong_number_check():
                print()
                a=int(input("Enter a number:"))
                b=len(str(a))
                c=a
                d=0
                while c>0:
                    e=c%10
                    d+=e**b
                    c=c//10
                if d==a:
                    print(a,"is an Armstrong number")
                else:
                    print(a,"is not an Armstrong number")
            def selection_sort_demo():
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                c=len(b)
                for d in range(c-1):
                    e=d
                    for f in range(d+1,c):
                        if b[f]<b[e]:
                            e=f
                    b[d],b[e]=b[e],b[d]
                print("Sorted list using selection sort:",b)
            def binary_search_iterative_demo():
                print()
                a=input("Enter numbers in ascending order, separated by space:")
                b=[int(i) for i in a.split()]
                c=int(input("Enter number to search:"))
                d=0
                e=len(b)-1
                f=-1
                while d<=e:
                    g=(d+e)//2
                    if b[g]==c:
                        f=g
                        break
                    elif b[g]<c:
                        d=g+1
                    else:
                        e=g-1
                if f==-1:
                    print("Number not found")
                else:
                    print("Number found at index:",f,"(iterative binary search)")
            def insertion_sort_demo():
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                for c in range(1,len(b)):
                    d=b[c]
                    e=c-1
                    while e>=0 and b[e]>d:
                        b[e+1]=b[e]
                        e-=1
                    b[e+1]=d
                print("Sorted list using insertion sort:",b)
            def word_frequency_counter_demo():
                print()
                a=input("Enter a sentence:")
                b=a.lower().split()
                c={}
                for d in b:
                    e=d.strip(".,!?")
                    if e in c:
                        c[e]+=1
                    else:
                        c[e]=1
                print("Word frequency count:")
                for f,g in c.items():
                    print(f,":",g)
            print()
            ch=int(input("WHAT DO YOU WANT TO SEE\nPRESS 1 for RANDOM NUMBER GENERATOR(DICE SIMULATOR)\nPRESS 2 for PRIME NUMBER CHECK\nPRESS 3 for PALINDROME CHECK\nPRESS 4 for BUBBLE SORT\nPRESS 5 for MATRIX ADDITION\nPRESS 6 for LINEAR SEARCH\nPRESS 7 for ARMSTRONG NUMBER CHECK\nPRESS 8 for SELECTION SORT\nPRESS 9 for BINARY SEARCH(ITERATIVE)\nPRESS 10 for INSERTION SORT\nPRESS 11 for WORD FREQUENCY COUNTER:"))
            if ch==1:
                _code_or_continue(dice_simulator)
            elif ch==2:
                _code_or_continue(prime_number_check)
            elif ch==3:
                _code_or_continue(palindrome_check)
            elif ch==4:
                _code_or_continue(bubble_sort_demo)
            elif ch==5:
                _code_or_continue(matrix_addition)
            elif ch==6:
                _code_or_continue(linear_search_demo)
            elif ch==7:
                _code_or_continue(armstrong_number_check)
            elif ch==8:
                _code_or_continue(selection_sort_demo)
            elif ch==9:
                _code_or_continue(binary_search_iterative_demo)
            elif ch==10:
                _code_or_continue(insertion_sort_demo)
            elif ch==11:
                _code_or_continue(word_frequency_counter_demo)

        while True:
            print()
            print("CLASS 12 CS GPT")
            print()
            choose=int(input("WHAT DO YOU WANT TO EXPLORE\nPRESS 1 for FUNCTION TYPES\nPRESS 2 for FUNCTION ARGUMENTS\nPRESS 3 for FUNCTION RETURN VALUES\nPRESS 4 for SCOPE OF VARIABLES\nPRESS 5 for RECURSION\nPRESS 6 for EXCEPTION HANDLING\nPRESS 7 for TEXT FILE HANDLING\nPRESS 8 for BINARY FILE HANDLING\nPRESS 9 for CSV FILE HANDLING\nPRESS 10 for STACK\nPRESS 11 for SQL - DDL AND DML\nPRESS 12 for SQL - QUERIES\nPRESS 13 for PYTHON-SQL CONNECTIVITY\nPRESS 14 for MISCELLANEOUS PROGRAMS:"))
            if choose==1:
                function_types()
            elif choose==2:
                function_arguments()
            elif choose==3:
                function_return_values()
            elif choose==4:
                function_scope()
            elif choose==5:
                recursion()
            elif choose==6:
                exception_handling()
            elif choose==7:
                text_file_handling()
            elif choose==8:
                binary_file_handling()
            elif choose==9:
                csv_file_handling()
            elif choose==10:
                stack_operations()
            elif choose==11:
                sql_ddl_dml()
            elif choose==12:
                sql_queries()
            elif choose==13:
                python_sql_connectivity()
            elif choose==14:
                miscellaneous_programs()
            else:
                print("Out of range")
            print()
            c=input("DO YOU WANT TO CONTINUE(Y/N):")
            if c in "Nn":
                break
    except TypeError:
        print("\033[31mUSE APPROPRIATE DATA TYPE\033[0m")
        print("\033[31mTRY AGAIN\033[0m")
    except ZeroDivisionError:
        print("\033[31mYOU CAN'T DIVIDE BY ZERO\033[0m")
        print("\033[31mTRY AGAIN\033[0m")
    except:
        print("\033[31mTRY AGAIN\033[0m")


# =============================================================================
# The VS Code-styled terminal — a native Tkinter window (no browser)
# =============================================================================

COLORS = dict(
    editor_bg="#1e1e1e", titlebar_bg="#323233", tab_bg="#2d2d2d",
    tab_active_bg="#1e1e1e", panel_header_bg="#252526", border="#3c3c3c",
    text="#cccccc", text_dim="#858585", accent="#007acc",
    white="#d4d4d4", red="#f14c4c",
)

# Matches the \033[31m ... \033[0m codes the tool prints on errors.
_ANSI_RE = re.compile(r"\x1b\[(\d+)m")


def _pick_mono_font(root: tk.Tk) -> str:
    preferred = ["Cascadia Code", "Consolas", "Menlo", "SF Mono", "DejaVu Sans Mono", "Courier New"]
    available = set(tkfont.families(root))
    for name in preferred:
        if name in available:
            return name
    return "TkFixedFont"


class TerminalApp:
    """Native window styled like a VS Code terminal. Runs the tool on
    a background thread and bridges its input()/print() calls to the
    on-screen Text widget."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.output_queue: "queue.Queue[str]" = queue.Queue()
        self.input_queue: "queue.Queue[str | None]" = queue.Queue()
        self._build_ui()
        self._current_tag = None  # active ANSI color tag, if any
        self.root.after(30, self._poll_output)
        self.worker = threading.Thread(target=self._run_worker, daemon=True)
        self.worker.start()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ---- UI construction -------------------------------------------------
    def _build_ui(self) -> None:
        root = self.root
        root.title("Class 12 CS GPT")
        root.configure(bg="#0e0e0e")
        root.geometry("900x640")

        mono = _pick_mono_font(root)

        window = tk.Frame(root, bg=COLORS["editor_bg"], highlightthickness=1,
                           highlightbackground="#000000")
        window.pack(fill="both", expand=True, padx=24, pady=24)

        # Titlebar with traffic-light dots
        titlebar = tk.Frame(window, bg=COLORS["titlebar_bg"], height=32)
        titlebar.pack(fill="x", side="top")
        titlebar.pack_propagate(False)
        dots = tk.Frame(titlebar, bg=COLORS["titlebar_bg"])
        dots.pack(side="left", padx=12)
        for color in ("#ff5f56", "#ffbd2e", "#27c93f"):
            c = tk.Canvas(dots, width=12, height=12, bg=COLORS["titlebar_bg"], highlightthickness=0)
            c.create_oval(1, 1, 11, 11, fill=color, outline="")
            c.pack(side="left", padx=4)
        tk.Label(titlebar, text="Class 12 CS GPT", bg=COLORS["titlebar_bg"],
                 fg=COLORS["text_dim"], font=(mono, 10)).pack(side="left", expand=True)
        tk.Frame(titlebar, bg=COLORS["titlebar_bg"], width=84).pack(side="right")

        # Tab bar
        tabbar = tk.Frame(window, bg=COLORS["tab_bg"])
        tabbar.pack(fill="x", side="top")
        tk.Label(tabbar, text="\u25cf Class 12 CS GPT", bg=COLORS["tab_bg"], fg=COLORS["text_dim"],
                 font=(mono, 10), padx=14, pady=6).pack(side="left")
        tk.Label(tabbar, text="\u25b6 Terminal", bg=COLORS["tab_active_bg"], fg=COLORS["text"],
                 font=(mono, 10), padx=14, pady=6).pack(side="left")
        tk.Frame(tabbar, bg=COLORS["border"], height=1).pack(fill="x", side="bottom")

        # Panel header
        panel = tk.Frame(window, bg=COLORS["panel_header_bg"], height=32)
        panel.pack(fill="x", side="top")
        panel.pack_propagate(False)
        tabs = tk.Frame(panel, bg=COLORS["panel_header_bg"])
        tabs.pack(side="left", padx=12)
        for i, label in enumerate(["PROBLEMS", "OUTPUT", "DEBUG CONSOLE", "TERMINAL"]):
            fg = COLORS["text"] if label == "TERMINAL" else COLORS["text_dim"]
            tk.Label(tabs, text=label, bg=COLORS["panel_header_bg"], fg=fg,
                     font=(mono, 9)).pack(side="left", padx=9)

        # Terminal text area
        self.text = tk.Text(
            window, bg=COLORS["editor_bg"], fg=COLORS["white"], insertbackground=COLORS["white"],
            font=(mono, 12), wrap="word", relief="flat", padx=16, pady=12, undo=False,
        )
        self.text.pack(fill="both", expand=True, side="top")
        self.text.tag_configure("error", foreground=COLORS["red"])
        self.input_start = "1.0"  # plain text-index snapshot, not a moving mark

        # Status bar
        status = tk.Frame(window, bg=COLORS["accent"], height=22)
        status.pack(fill="x", side="bottom")
        status.pack_propagate(False)
        tk.Label(status, text="\u2713 main", bg=COLORS["accent"], fg="white", font=(mono, 9)).pack(side="left", padx=10)
        tk.Label(status, text="Python", bg=COLORS["accent"], fg="white", font=(mono, 9)).pack(side="left", padx=10)
        tk.Label(status, text="UTF-8", bg=COLORS["accent"], fg="white", font=(mono, 9)).pack(side="right", padx=10)

        self.text.bind("<Return>", self._on_return)
        self.text.bind("<BackSpace>", self._on_backspace)
        self.text.bind("<Key>", self._on_key)
        self.text.focus_set()

    # ---- keyboard handling -------------------------------------------------
    def _clamp_cursor(self) -> None:
        if self.text.compare("insert", "<", self.input_start):
            self.text.mark_set("insert", "end")

    def _on_key(self, event: tk.Event) -> str | None:
        if event.keysym in ("Return", "BackSpace", "Left", "Up", "Down",
                             "Home", "End", "Shift_L", "Shift_R",
                             "Control_L", "Control_R", "Tab"):
            return None
        self._clamp_cursor()
        return None

    def _on_backspace(self, event: tk.Event) -> str | None:
        if self.text.compare("insert", "<=", self.input_start):
            return "break"
        return None

    def _on_return(self, event: tk.Event) -> str:
        line = self.text.get(self.input_start, "end-1c")
        self.text.insert("end", "\n")
        self.input_start = self.text.index("end-1c")
        self.text.see("end")
        self.input_queue.put(line)
        return "break"

    # ---- output handling ----------------------------------------------
    def _poll_output(self) -> None:
        try:
            while True:
                chunk = self.output_queue.get_nowait()
                self._write(chunk)
        except queue.Empty:
            pass
        self.root.after(30, self._poll_output)

    def _write(self, chunk: str) -> None:
        pos = 0
        for m in _ANSI_RE.finditer(chunk):
            if m.start() > pos:
                self._insert(chunk[pos:m.start()])
            code = m.group(1)
            self._current_tag = "error" if code == "31" else None
            pos = m.end()
        if pos < len(chunk):
            self._insert(chunk[pos:])
        self.input_start = self.text.index("end-1c")
        self.text.see("end")

    def _insert(self, text: str) -> None:
        if not text:
            return
        if self._current_tag:
            self.text.insert("end", text, self._current_tag)
        else:
            self.text.insert("end", text)

    # ---- stdio bridge (used by the tool thread) ---------------------
    class _Out:
        def __init__(self, q): self.q = q
        def write(self, s):
            if s:
                self.q.put(s)
            return len(s)
        def flush(self): pass

    class _In:
        def __init__(self, q): self.q = q
        def readline(self, *_a):
            line = self.q.get()
            if line is None:
                raise EOFError("window closed")
            return line + "\n"

    def _run_worker(self) -> None:
        old_out, old_in = sys.stdout, sys.stdin
        sys.stdout = TerminalApp._Out(self.output_queue)
        sys.stdin = TerminalApp._In(self.input_queue)
        try:
            cs12()
        except EOFError:
            pass
        except Exception as exc:  # noqa: BLE001 - show it, don't crash silently
            self.output_queue.put(f"\n[error] {exc}\n")
        finally:
            sys.stdout, sys.stdin = old_out, old_in
            self.output_queue.put("\n[Session ended — close the window to exit]\n")

    def _on_close(self) -> None:
        self.input_queue.put(None)  # unblock a pending input() so the thread can exit
        self.root.destroy()


# =============================================================================
# Entry point
# =============================================================================

def main() -> None:
    root = tk.Tk()
    TerminalApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
