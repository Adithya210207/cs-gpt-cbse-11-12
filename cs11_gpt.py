"""
@Author:Adithya v
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


# =============================================================================
# The calculator itself — unchanged from the original
# =============================================================================

def cs():
    try:
        def perfect_number():
            def finding_perfect_number():
               print()
               a=int(input("Enter the number:"))
               b=[]
               for i in range(1,a+1):
                   if a%i==0:
                       b.append(i)
               c=0
               for z in b:
                   c+=z
               c=c-a
               print(c)
               if c==a:
                   print("it is a perfect number")
               else:
                   print("it is not a perfect number")
            def perfect_numbers_in_a_particular_range():
                print()
                a=input("Enter the range(start limit:stop limit):")
                aa=a.split(":")
                b=[]
                for k in aa:
                    d=""
                    c=k.split()
                    for j in c:
                        d+=j
                    b.append(int(d))
                e=b[0]
                f=b[1]
                g=[]
                for a in range(e,f+1):
                    h=[]
                    for i in range(1,a+1):
                        if a%i==0:
                            h.append(i)
                    c=0
                    for z in h:
                        c+=z
                    c=c-a
                    if c==a:
                        g.append(a)
                print("All perfect numbers in that particular range is:")
                for i in g:
                    print(i)
            print()
            ch=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for VERIFING A PERFECT NUMBER \nPRESS 2 for FINDING PERFECT NUMBERS IN A PARTICLAR RANGE:"))
            if ch==1:
                _code_or_continue(finding_perfect_number)
            elif ch==2:
                _code_or_continue(perfect_numbers_in_a_particular_range)
        def neon_number():
            def neon_numbers_in_a_particular_range():
                print()
                a=input("Enter the range(start limit:stop limit):")
                aa=a.split(":")
                b=[]
                for k in aa:
                    d=""
                    c=k.split()
                    for j in c:
                        d+=j
                    b.append(int(d))
                e=b[0]
                f=b[1]
                g=[]
                for i in range(e,f+1):
                    s=0
                    h=i**2
                    for j in str(h):
                        s+=int(j)
                    if s==i:
                        g.append(i)
                print("All neon numbers in that particular range is:")
                for i in g:
                    print(i)
            def finding_neon_number():
                print()
                a=int(input("Enter  the number:"))
                b=a**2
                c=str(b)
                d=0
                for i in c:
                    d+=int(i)
                if d==a:
                    print("It is a neon number")
                else:
                    print("It is not a neon number")
            print()
            ch=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for VERIFING A NEON NUMBER \nPRESS 2 for FINDING NEON NUMBERS IN A PARTICLAR RANGE:"))
            if ch==1:
                _code_or_continue(finding_neon_number)
            elif ch==2:
                _code_or_continue(neon_numbers_in_a_particular_range)
        def armstrong_number():
            def finding_armstrong_number():
                print()
                a=input("Enter the number:")
                b=int(a)
                c=0
                D="It is a Armstrong number"
                E="It is not a Armstrong number"
                for i in a:
                    c+=int(i)**3
                if c==b:
                    print(D)
                else :
                    print(E)
            def armstrong_numbers_in_a_particular_range():
                print()
                a=input("Enter the range(start limit:stop limit):")
                aa=a.split(":")
                b=[]
                for k in aa:
                    d=""
                    c=k.split()
                    for j in c:
                        d+=j
                    b.append(int(d))
                e=b[0]
                f=b[1]
                g=[]
                for i in range(e,f+1):
                    h=0
                    k=i
                    for j in str(i):
                        h+=int(j)**3
                    if h==k:
                        g.append(i)
                print("All armstrong numbers in that particular range is:")
                for l in g:
                    print(l)
            def sum_of_armstrong_numbers_in_a_particular_range():
                print()
                a=input("Enter the range(start limit:stop limit):")
                aa=a.split(":")
                b=[]
                s=0
                for k in aa:
                    d=""
                    c=k.split()
                    for j in c:
                        d+=j
                    b.append(int(d))
                e=b[0]
                f=b[1]
                g=[]
                for i in range(e,f+1):
                    h=0
                    k=i
                    for j in str(i):
                        h+=int(j)**3
                    if h==k:
                        g.append(i)
                print("All armstrong numbers in that particular range is:")
                for l in g:
                    print(l)
                    s+=l
                print("Sum of all prime numbers in that range=",s)
            print()
            ch=int(input("WHAT DO YOU WANT TO CALCULATE \nPRESS 1 for VERIFING A ARMSTRONG NUMBER \nPRESS 2 for FINDING ARMSTRONG NUMBERS IN A PARTICLAR RANGE \nPRESS 3 for FINDING SUM OF ARMSTRONG NUMBERS IN A PARTICLAR RANGE:"))
            if ch==1:
                _code_or_continue(finding_armstrong_number)
            elif ch==2:
                _code_or_continue(armstrong_numbers_in_a_particular_range)
            elif ch==3:
                _code_or_continue(sum_of_armstrong_numbers_in_a_particular_range)
        def prime_numbers():
            def finding_prime_number():
                print()
                n=int(input("Enter the number:"))
                A="It is a prime number"
                B="It is not a prime number"
                lim=int(n/2)+1
                for i in range(2,lim):
                    rem=n%i
                    if rem==0:
                        print(B)
                        break
                    else:
                        print(A)
            def prime_numbers_in_a_particular_range():
                print()
                a=input("Enter the range(start limit:stop limit):")
                aa=a.split(":")
                b=[]
                for k in aa:
                    d=""
                    c=k.split()
                    for j in c:
                        d+=j
                    b.append(int(d))
                e=b[0]
                f=b[1]
                g=[]
                for i in range(e,f+1):
                    h=[]
                    for j in range (1,i+1):
                        if i%j==0:
                            h.append(j)
                    if h==[1,i]:
                        g.append(i)
                print("All prime numbers in that particular range is:")
                for l in g:
                    print(l)
            def sum_of_prime_numbers_in_a_particular_range():
                print()
                a=input("Enter the range(start limit:stop limit):")
                aa=a.split(":")
                b=[]
                s=0
                for k in aa:
                    d=""
                    c=k.split()
                    for j in c:
                        d+=j
                    b.append(int(d))
                e=b[0]
                f=b[1]
                g=[]
                for i in range(e,f+1):
                    h=[]
                    for j in range (1,i+1):
                        if i%j==0:
                            h.append(j)
                    if h==[1,i]:
                        g.append(i)
                print("All prime numbers in that particular range is:")
                for l in g:
                    print(l)
                    s+=i
                print("Sum of all prime numbers in that range=",s) 
            print()
            ch=int(input("WHAT DO YOU WANT TO CALCULATE \nPRESS 1 for VERIFING A PRIME NUMBER \nPRESS 2 for FINDING PRIME NUMBERS IN A PARTICLAR RANGE \nPRESS 3 for FINDING SUM OF PRIME NUMBERS IN A PARTICLAR RANGE:"))
            if ch==1:
                _code_or_continue(finding_prime_number)
            elif ch==2:
                _code_or_continue(prime_numbers_in_a_particular_range)
            elif ch==3:
                _code_or_continue(sum_of_prime_numbers_in_a_particular_range)
        def class_10_percentage_calculator():
            l=0
            m=0
            sci=0
            ssc=0
            s=0
            n=0
            e=0
            t=0
            h=0
            sans=0
            while True:
                print()
                ch=int(input("PRESS 1 for  Language \nPRESS 2 for Maths\nPRESS 3 for Sciences \nPRESS 4 for Social Science:"))
                if ch==1:
                    if l<3:
                        print()
                        chh=int(input("PRESS 1 for  English \nPRESS 2 for Tamil\nPRESS 3 for Hindi \nPRESS 4 for Sanskrit:"))
                        if chh==1:
                            if e<1:
                                print()
                                c=float(input("Enter the English Marks:"))
                                s+=c
                                e+=1
                                n+=1
                            else:
                                print()
                                print("Already selected English")           
                        if chh==2:
                            if t<1:
                                print()
                                c=float(input("Enter the Tamil Marks:"))
                                s+=c
                                t=+1
                                n+=1
                            else:
                                print()
                                print("Already selected Tamil")       
                        if chh==3:
                            if h<1:
                                print()
                                c=float(input("Enter the Hindi Marks:"))
                                s+=c
                                h=+1
                                n+=1
                            else:
                                print()
                                print("Already selected Hindi") 
                        if chh==4:
                            if sans<1:
                                print()
                                c=float(input("Enter the Sanskrit Marks:"))
                                s+=c
                                sans+=1
                                n+=1
                            else:
                                print()
                                print("Already selected Sanskrit")     
                        l+=1
                    else:
                        print()
                        print("Already selected two languages") 
                if ch==2:
                    if m<1:
                        print()
                        c=float(input("Enter the Maths Marks:"))
                        s+=c
                        m+=1
                        n+=1
                    else:
                        print()
                        print("Already selected Maths")
                if ch==3:
                    if sci<1:
                        print()
                        c=float(input("Enter the Science Marks:"))
                        s+=c
                        sci+=1
                        n+=1
                    else:
                        print()
                        print("Already selected Science")
                if ch==4:
                    if ssc<1:
                        print()
                        c=float(input("Enter the Social Science Marks:"))
                        s+=c
                        ssc=+1
                        n+=1
                    else:
                        print()
                        print("Already selected Social science")
                if n==5:
                    break  
            print()
            print("Total mark=",s)
            p=s/5
            print("Percentage=",p)
            if p>85:
                print("A")
            elif p<85 and p>=75:
                print("B")
            elif p<75 and p>=50:
                print("C")    
            elif p>30 and p<=50:
                print("D")
            elif p<30:
                print("Reappear")  
        def calculator():
            print()
            def add():
                n=int(input("Enter the no. of terms you want to add:"))
                c=0
                for i in range(n):
                    a=int(input("Enter the number:"))
                    c+=a
                print("Answer=",c)
            def sub():
                n=int(input("Enter the no. of terms you want to subtract:"))
                c=0
                for i in range(n):
                    a=int(input("Enter the number:"))
                    c-=a
                print("Answer=",c)
            def mul():
                n=int(input("Enter the no. of terms you want to multiply:"))
                c=1
                for i in range(n):
                    a=int(input("Enter the number:"))
                    c*=a
                print("Answer=",c)
            def div():
                n=int(input("Enter the no. of terms you want to divid:"))
                cc=0
                c=int(input("Enter the first number(it cannot be zero):"))
                while cc<n:
                    a=int(input("Enter the next number:"))
                    if a!=0:
                        c/=a
                    else:
                        print("we cannot divide by zero")
                        n+=1
                    ch=input("Do u want to contnue(y/n):")
                    if ch in "nN": 
                        break
                    cc+=1
                print("Answer=",c)
            def square():
                side=float(input('Enter the length:'))
                area1=side*side
                print('Area of square=',area1)
            def rectangle():
                a1=float(input('Enter the lenght:'))
                b1=float(input('Enter the breadth:'))
                area2=a1*b1
                print('Area of rectangle=',area2)
            def trianle():
                a4=float(input("Enter the base:"))
                b4=float(input("Enter the hight:"))
                area4=(1/2)*a4*b4
                print('Area of Triangle=',area4)
            def circle():
                r=float(input('Enter the radius:'))
                area3=3.14*r**2
                print("Area of circle=",area3)
            def semicircle():
                r=float(input('Enter the radius:'))
                area=(3.14*r**2)*1/2
                print("Area of Semi-circle=",area)
            def parallelogram():
                a2=float(input('Enter the base:'))
                h1=float(input('Enter the height:'))
                area4=a2*h1
                print('Area of parallelogram=',area4)
            def trapezium():
                a3=float(input('Enter the base1:'))
                b3=float(input('Enter the base2:'))
                h2=float(input('Enter the height:'))
                area5=((a3+b3)/2)*h2
                print('Area of trapezium=',area5)
            def rhombus():
                a=float(input('Enter the diagonal1:'))
                b=float(input('Enter the diagonal2:'))
                area=1/2*a*b
                print("Area of Rhombus=",area)
            def diamond():
                a=float(input('Enter the diagonal1:'))
                b=float(input('Enter the diagonal2:'))
                area=1/2*a*b
                print("Area of Diamond=",area)
            def pentagon():
                import math
                a=float(input('Enter the length:'))
                b=math.sqrt(5)
                d=math.sqrt(5*(5+2*b))
                area=1/4*(a**2)*d
                print("Area of Pentagon=",area)
            def hexagon():
                import math
                a=float(input('Enter the length:'))
                b=math.sqrt(3)
                d=(3*b)*1/2*(a**2)
                print("Area of Hexagon=",d)
            def heptagon():
                a=float(input('Enter the length:'))
                area=3.63391*a*a
                print("Area of Heptagon=",area)
            def octagon():
                import math
                a=float(input('Enter the length:'))
                b=math.sqrt(2)
                e=1+b
                d=2*e
                area=d*(a**2)
                print("Area of Octagon",area)
            def nonagon():
                a=float(input('Enter the length:'))
                area=6.18182*a*a
                print("Area of Nonagon=",area)
            def decagon():
                a=float(input('Enter the length:'))
                area=7.69421*a*a
                print("Area of decagon=",area)
            def polygon():
                a=float(input('Enter the length of an apothem:'))
                b=float(input("Enter the perimeter:"))
                area=(1/2)*a*b
                print("Area  of polygon=",area)
            def VOLcube():
                a=float(input('Enter the length:'))
                vol=a**3
                print("Volume of Cube=",vol)
            def CSAcube():
                a=float(input('Enter the length:'))
                area=4*a**2
                print("Curved surface Area of Cube=",area)
            def TSAcube():
                a=float(input("Enter the length:"))
                area=6*a**2
                print("Total Surface Area of Cube:",area)
            def VOLcuboid():
                a=float(input('Enter the length:'))
                b=float(input('Enter the breadth:'))
                d=float(input('Enter the height:'))
                vol=a*b*d
                print("Volume of cuboid =",vol)
            def CSAcuboid():
                a=float(input('Enter the length:'))
                b=float(input('Enter the breadth:'))
                d=float(input('Enter the height:'))
                area=2*d*(a+b)
                print("Curved surface Area of cuboid=",area)
            def TSAcuboid():
                a=float(input('Enter the length:'))
                b=float(input('Enter the breadth:'))
                d=float(input('Enter the height:'))
                area=2*(a*b+b*d+a*d)
                print("Total Surface Area of Cuboid=",area)
            def VOLcone():
                a=float(input('Enter the radius:'))
                b=float(input('Enter the height:'))
                vol=3.14*(a**3)*(b/3)
                print("Volume of cone=",vol)
            def CSAcone():
                a=float(input('Enter the radius:'))
                b=float(input('Enter the slant height:'))
                area=3.14*a*b
                print("Curved Surface Area of cone=",area)
            def TSAcone():
                a=float(input('Enter the radius:'))
                b=float(input('Enter the slant height:'))
                area=3.14*a*(a+b)
                print("Curved Surface Area of cone=",area)
            def VOLcylinder():
                a=float(input('Enter the radius:'))
                b=float(input('Enter the height:'))
                vol=3.14*a*a*b
                print("Volume of Cylinder=",vol)
            def CSAcylinder():
                a=float(input('Enter the radius:'))
                b=float(input('Enter the height:'))
                area=2*3.14*a*b
                print("Curved Surface Area of Cylinder=",area)
            def TSAcylinder():
                a=float(input('Enter the radius:'))
                b=float(input('Enter the height:'))
                area=2*3.14*a*(a+b)
                print("Total Surface Area of Cylinder=",area)
            def VOLsphere():
                a=float(input('Enter the radius:'))
                vol=(4/3)*3.14*a**3
                print("volume of Sphere=",vol)
            def CSAsphere():
                a=float(input('Enter the radius:'))
                area=4*3.14*a**2
                print("Curved Surface Area of Sphere=",area)
            def TSAsphere():
                a=float(input('Enter the radius:'))
                area=4*3.14*a**2
                print("Total Surface Area of Sphere=",area)
            def VOLhemisphere():
                a=float(input('Enter the radius:'))
                vol=(2/3)*3.14*a**3
                print("volume of hemisphere=",vol)
            def CSAhemisphere():
                a=float(input('Enter the radius:'))
                area=2*3.14*a**2
                print("Curved Surface Area of Hemisphere=",area)
            def TSAhemisphere():
                a=float(input('Enter the radius:'))
                area=3*3.14*a**2
                print("Total Surface Area of Hemisphere=",area)
            def VOLpyramid():
                a=float(input('Enter the base length:'))
                b=float(input('Enter the base width:'))
                d=float(input('Enter the pyramid height:'))
                vol=(a*b*d)/3
                print("Volume of pyramid=",vol)
            def CSApyramid():
                a=float(input('Enter the base perimeter:'))
                b=float(input('Enter the slant heght:'))
                area=(1/2)*a*b
                print("Curved Surface Area of Pyramid",area)
            def TSApyramid():
                a=float(input('Enter the base length:'))
                b=float(input('Enter the base width:'))
                d=float(input('Enter the pyramid height:'))
                area=(1/2)*a*b+d
                print("Total Surface Area of Pyramid",area)
            def oval():
                a=float(input('Enter the length of major axis:')) 
                b=float(input('Enter the length of minor axis:'))
                area=3.14*a*b
                print("Area of Oval=",area)
            def ellipse():
                a=float(input('Enter the length of major axis:'))
                b=float(input('Enter the length of minor axis:'))
                area=3.14*a*b
                print("Area of Ellipse=",area)
            def kite():
                a=float(input('Enter the diagonal1:'))
                b=float(input('Enter the diagonal2:'))
                area=1/2*a*b
                print("Area of Kite=",area)
            def sin():
                import math
                a=int(input("Enter the degree:"))
                b=math.sin(a)
                print('Sin ',a,"=",b)
            def cos():
                import math
                a=int(input("Enter the degree:"))
                b=math.cos(a)
                print("Cos ",a,"=",b)
            def tan():
                import math
                a=int(input("Enter the degree:"))
                b=math.tan(a)
                print("Tan ",a,"=",b)
            def cosec():
                import math
                a=int(input("Enter the degree:"))
                b=1/math.sin(a)
                print("Cosec ",a,"=",b)
            def sec():
                import math
                a=int(input("Enter the degree:"))
                b=1/math.cos(a)
                print("Sec ",a,"=",b)
            def cot():
                import math
                a=int(input("Enter the degree:"))
                b=1/math.tan(a)
                print("Cot ",a,"=",b)
            def asin():
                import math
                a=int(input("Enter the degree:"))
                b=math.asin(a)
                print('Sin inverse',a,"=",b)
            def acos():
                import math
                a=int(input("Enter the degree:"))
                b=math.acos(a)
                print("Cos inverse",a,"=",b)
            def atan():
                import math
                a=int(input("Enter the degree:"))
                b=math.atan(a)
                print("Tan inverse",a,"=",b)
            def acosec():
                import math
                a=int(input("Enter the degree:"))
                b=math.asin(1/a)
                print("Cosec inverse",a,"=",b)
            def asec():
                import math
                a=int(input("Enter the degree:"))
                b=math.acos(1/a)
                print("Sec inverse",a,"=",b)
            def acot():
                import math
                a=int(input("Enter the degree:"))
                b=math.atan(1/a)
                print("Cot inverse",a,"=",b)
            def sinh():
                import math
                a=int(input("Enter the degree:"))
                b=math.sinh(a)
                print('Hyperbolic Sin ',a,"=",b)
            def cosh():
                import math
                a=int(input("Enter the degree:"))
                b=math.cosh(a)
                print("Hyperbolic Cos ",a,"=",b)
            def tanh():
                import math
                a=int(input("Enter the degree:"))
                b=math.tanh(a)
                print("Hyperbolic Tan ",a,"=",b)
            def cosech():
                import math
                a=int(input("Enter the degree:"))
                b=1/math.sinh(a)
                print("Hyperbolic Cosec ",a,"=",b)
            def sech():
                import math
                a=int(input("Enter the degree:"))
                b=1/math.cosh(a)
                print("Hyperbolic Sec ",a,"=",b)
            def coth():
                import math
                a=int(input("Enter the degree:"))
                b=1/math.tanh(a)
                print("Hyperbolic Cot ",a,"=",b)
            def asinh():
                import math
                a=int(input("Enter the degree:"))
                b=math.asinh(a)
                print('Inverse hyperbolic Sin ',a,"=",b)
            def acosh():
                import math
                a=int(input("Enter the degree:"))
                b=math.acosh(a)
                print("Inverse hyperbolic Cos ",a,"=",b)
            def atanh():
                import math
                a=int(input("Enter the degree:"))
                b=math.atanh(a)
                print("Inverse hyperbolic Tan ",a,"=",b)
            def acosech():
                import math
                a=int(input("Enter the degree:"))
                b=math.asinh(1/a)
                print("Inverse hyperbolic Cosec ",a,"=",b)
            def asech():
                import math
                a=int(input("Enter the degree:"))
                b=math.acosh(1/a)
                print("Inverse hyperbolic Sec ",a,"=",b)
            def acoth():
                import math
                a=int(input("Enter the degree:"))
                b=math.atanh(1/a)
                print("Inverse hyperbolic Cot ",a,"=",b)
            def percentage():
                a=float(input("Enter the value:"))
                b=float(input("Enter the max value:"))
                d=(a/b)*100
                print("percentage=",d)
            def power():
                a=float(input("Enter the number:"))
                b=float(input("Enter the power:"))
                d=a**b
                print("Answer=",d)
            def Square_root():
                import math
                a=float(input("Enter the number:"))
                b=math.sqrt(a)
                print("Square Root=",b)
            def cube_root():
                a=float(input("Enter the number:"))
                b=a**(1/3)
                print("Square Root=",b)
            def log():
                import math
                a=float(input("Enter the value:"))
                b=float(input("Enter the base:"))
                d=math.log(a,b)
                print("Log value=",d)
            def antilog():
                import math
                a=float(input("Enter the exponent:"))
                b=float(input("Enter the base:"))
                d=math.pow(b,a)
                print("Antilog value=",d)
            print("THE CALCULATOR")
            print()
            ch=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for SIMPLE CALCULATION\nPress 2 for AREA OF 2D SHAPES\nPRESS 3 for AREA OR VOLUME OF 3D SHAPES\nPRESS 4 for TRIGONOMETRIC VALUES\nPRESS 5 for INVERSE TRIGONOMETRIC VALUES\nPRESS 6 for HYPERBOLIC TRIGONOMETRIC VALUES\nPRESS 7 for INVERSE HYPERBOLIC TRIGONOMETRIC VALUES\nPRESS 8 for PERCENTAGE\nPRESS 9 for POWER\nPRESS 10 for SQUARE ROOT\nPRESS 11 for CUBE ROOT\nPRESS 12 for LOG\nPRESS 13 for ANTILOG:"))   
            print()
            if ch==1:
                ch1=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for ADDITION/nPRESS 2 for SUBTRACTION\nPRESS 3 for MULTIPLICATION\nPRESS 4 for DIVISION:"))
                print()
                if ch1==1:
                    _code_or_continue(add)
                elif ch1==2:
                    _code_or_continue(sub)
                elif ch1==3:
                    _code_or_continue(mul)
                elif ch1==4:
                    _code_or_continue(div)
                else:
                    print("Out of range")   
            elif ch==2:
                ch2=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for SQUARE\nPREESS 2 for RECTANGLE\nPRESS 3 for TRIANGLE\nPRESS 4 for CIRCLE\nPRESS 5 for SEMI-CIRCLE\nPRESS 6 for PARALLELOGRAM\nPRESS 7 for TRAPEZIUM\nPRESS 8 for RHOMBUS\nPRESS 9 for DIAMOND\nPRESS 10 for KITE\nPRESS 11 for OVAL\nPRESS 12 for ELLIPSE\nPRESS 13 for PENTAGON\nPRESS 14 for HEXAGON\nPRESS 15 for HEPTAGON\nPRESS 16 for OCTAGON\nPRESS 17 for NONAGON\nPRESS 18 for DECAGON\nPRESS 19 for POLYGON:"))
                print()
                if ch2==1:
                    _code_or_continue(square)
                elif ch2==2:
                    _code_or_continue(rectangle)
                elif ch2==3:
                    _code_or_continue(trianle)
                elif ch2==4:
                    _code_or_continue(circle)
                elif ch2==5:
                    _code_or_continue(semicircle)
                elif ch2==6:
                    _code_or_continue(parallelogram)
                elif ch2==7:
                    _code_or_continue(trapezium)
                elif ch2==8:
                    _code_or_continue(rhombus)
                elif ch2==9:
                    _code_or_continue(diamond)
                elif ch2==10:
                    _code_or_continue(kite)
                elif ch2==11:
                    _code_or_continue(oval)
                elif ch2==12:
                    _code_or_continue(ellipse)
                elif ch2==13:
                    _code_or_continue(pentagon)
                elif ch2==14:
                    _code_or_continue(hexagon)
                elif ch2==15:
                    _code_or_continue(heptagon)
                elif ch2==16:
                    _code_or_continue(octagon)
                elif ch2==17:
                    _code_or_continue(nonagon)
                elif ch2==18:
                    _code_or_continue(decagon)
                elif ch2==19:
                    _code_or_continue(polygon)
                else:
                    print("Out of range")
            elif ch==3:
                ch3=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for VOLUME\nPRESS 2 for CURVED SURFACE AREA\nPRESS 3 for TOTAL SURFACE AREA:"))
                print()
                if ch3==1:
                    ch3a=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for CUBE\nPRESS 2 for CUBOID\nPRESS 3 for CYLINDER\nPRESS 4 for CONE\nPRESS 5 for PYRAMID\nPRESS 6 for SPHERE\nPRESS 7 for HEMISPHERE:"))
                    if ch3a==1:
                        _code_or_continue(VOLcube)
                    elif ch3a==2:
                        _code_or_continue(VOLcuboid)
                    elif ch3a==3:
                        _code_or_continue(VOLcylinder)
                    elif ch3a==4:
                        _code_or_continue(VOLcone)
                    elif ch3a==5:
                        _code_or_continue(VOLpyramid)
                    elif ch3a==6:
                        _code_or_continue(VOLsphere)
                    elif ch3a==7:
                        _code_or_continue(VOLhemisphere)
                    else:
                        print("Out of range")
                if ch3==2:
                    ch3b=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for CUBE\nPRESS 2 for CUBOID\nPRESS 3 for CYLINDER\nPRESS 4 for CONE\nPRESS 5 for PYRAMID\nPRESS 6 for SPHERE\nPRESS 7 for HEMISPHERE:"))
                    if ch3b==1:
                        _code_or_continue(CSAcube)
                    elif ch3b==2:
                        _code_or_continue(CSAcuboid)
                    elif ch3b==3:
                        _code_or_continue(CSAcylinder)
                    elif ch3b==4:
                        _code_or_continue(CSAcone)
                    elif ch3b==5:
                        _code_or_continue(CSApyramid)
                    elif ch3b==6:
                        _code_or_continue(CSAsphere)
                    elif ch3b==7:
                        _code_or_continue(CSAhemisphere)
                    else:
                        print("Out of range")
                if ch3==3:
                    ch3C=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for CUBE\nPRESS 2 for CUBOID\nPRESS 3 for CYLINDER\nPRESS 4 for CONE\nPRESS 5 for PYRAMID\nPRESS 6 for SPHERE\nPRESS 7 for HEMISPHERE:"))
                    if ch3C==1:
                        _code_or_continue(TSAcube)
                    elif ch3C==2:
                        _code_or_continue(TSAcuboid)
                    elif ch3C==3:
                        _code_or_continue(TSAcylinder)
                    elif ch3C==4:
                        _code_or_continue(TSAcone)
                    elif ch3C==5:
                        _code_or_continue(TSApyramid)
                    elif ch3C==6:
                        _code_or_continue(TSAsphere)
                    elif ch3C==7:
                        _code_or_continue(TSAhemisphere)
                    else:
                        print("Out of range")
            elif ch==4:
                ch4=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for SIN\nPRESS 2 for COS\nPRESS 3 for TAN\nPRESS 4 for COSEC\nPRESS 5 for SEC\nPRESS 6 for COT:"))
                print()
                if ch4==1:
                    _code_or_continue(sin)
                elif ch4==2:
                    _code_or_continue(cos)
                elif ch4==3:
                    _code_or_continue(tan)
                elif ch4==4:
                    _code_or_continue(cosec)
                elif ch4==5:
                    _code_or_continue(sec)
                elif ch4==6:
                    _code_or_continue(cot)
                else:
                    print("Out of range")
            elif ch==5:
                ch4=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for SIN INVERSE\nPRESS 2 for COS INVERSE\nPRESS 3 for TAN INVERSE\nPRESS 4 for COSEC INVERSE\nPRESS 5 for SEC INVERSE\nPRESS 6 for COT INVERSE:"))
                print()
                if ch4==1:
                    _code_or_continue(asin)
                elif ch4==2:
                    _code_or_continue(acos)
                elif ch4==3:
                    _code_or_continue(atan)
                elif ch4==4:
                    _code_or_continue(acosec)
                elif ch4==5:
                    _code_or_continue(asec)
                elif ch4==6:
                    _code_or_continue(acot)
                else:
                    print("Out of range")
            elif ch==6:
                ch4=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for HYPERBOLIC SIN\nPRESS 2 for HYPERBOLIC COS\nPRESS 3 for HYPERBOLIC TAN\nPRESS 4 for HYPERBOLIC COSEC\nPRESS 5 for HYPERBOLIC SEC\nPRESS 6 for HYPERBOLIC COT:"))
                print()
                if ch4==1:
                    _code_or_continue(sinh)
                elif ch4==2:
                    _code_or_continue(cosh)
                elif ch4==3:
                    _code_or_continue(tanh)
                elif ch4==4:
                    _code_or_continue(cosech)
                elif ch4==5:
                    _code_or_continue(sech)
                elif ch4==6:
                    _code_or_continue(coth)
                else:
                    print("Out of range")
            elif ch==7:
                ch4=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for INVERSE HYPERBOLIC SIN\nPRESS 2 for INVERSE HYPERBOLIC COS\nPRESS 3 for INVERSE HYPERBOLIC TAN\nPRESS 4 for INVERSE HYPERBOLIC COSEC\nPRESS 5 for INVERSE HYPERBOLIC SEC\nPRESS 6 for INVERSE HYPERBOLIC COT:"))
                print()
                if ch4==1:
                    _code_or_continue(asinh)
                elif ch4==2:
                    _code_or_continue(acosh)
                elif ch4==3:
                    _code_or_continue(atanh)
                elif ch4==4:
                    _code_or_continue(acosech)
                elif ch4==5:
                    _code_or_continue(asech)
                elif ch4==6:
                    _code_or_continue(acoth)
                else:
                    print("Out of range")
            elif ch==8:
                _code_or_continue(percentage)
            elif ch==9:
                _code_or_continue(power)
            elif ch==10:
                _code_or_continue(Square_root)
            elif ch==11:
                _code_or_continue(cube_root)
            elif ch==12:
                _code_or_continue(log)
            elif ch==13:
                _code_or_continue(antilog)
            else:
                print("Out of range")
        def palindrome():
            print()
            a=input("ENTER:")
            pal=a
            b=a[::-1]
            C="It is a Palindrome"
            D="It is not a Palindrome"
            if b==pal:
                print(C)
            else:
                print(D)
        def Greatest_number():
            print()
            a=input("Enter numbers which should be seperatered with comma:")
            aa=a.split(",")
            list(aa)
            b=0
            for i in aa:
                if int(i)>b:
                    b=int(i)
            print("The Greatest number=",b)
        def vote_eligibility():
            print()
            a=int(input("Enter your age:"))
            B="You are Eligibile for Voting"
            C="You are not Eligibile for Voting"
            if a>18:
                print(B)
            else:
                print(C)
        def factorial():
            print()
            n=int(input("Enter the number:"))
            fact=1 
            while n>0:
                fact*=n
                n-=1
            print("Factorial=",fact)
        def odd_or_even():
            print()
            a=int(input("Enter the number:"))
            B="Even numnber"
            C="Odd number"
            if a%2==0:
                print(B)
            else:
                print(C)
        def tables():
            print()
            n=int(input("Enter the number:"))
            for i in range(1,21):
                print(n,"x",i,"=",n*i)
        def pattern():
            def Character_square_pattern():
                a=input("Enter the character you want in the pattern:")
                n=int(input("Enter the number of lines:"))
                for i in range(n):
                    for j in range(n):
                        print(a,end=" ")
                    print()
            def CONSTANT_NUMBER_square_pattern():
                a=input("Enter the number you want in the pattern:")
                n=int(input("Enter the number of lines:"))
                for i in range(n):
                    for j in range(n):
                        print(a,end=" ")
                    print()
            def INCREASING_NUMBER_square_pattern():
                a=int(input("Enter the number you want in the pattern:"))
                n=int(input("Enter the number of lines:"))
                for i in range(n):
                    for j in range(n):
                        print(a,end=" ")
                        a+=1
                    print()
            def CHARATER_diamond_pattern():
                a=input("Enter the character you want in the pattern:")
                row=int(input("Enter the number of lines:"))
                k=2*row-2
                for i in range(0,row):    
                    for j in range(0,k):
                        print(end=" ")
                    k-=1
                    for j in range(0,i+1):
                        print(a,end=" ")
                    print()
                k=2*row-2
                for i in range(row,-1,-1):    
                    for j in range(k,0,-1):
                        print(end=" ")
                    k+=1
                    for j in range(0,i+1):
                        print(a,end=" ")
                    print()
            def CONSTANT_number_diamond_pattern():
                a=input("Enter the number you want in the pattern:")
                row=int(input("Enter the number of lines:"))
                k=2*row-2
                for i in range(0,row):    
                    for j in range(0,k):
                        print(end=" ")
                    k-=1
                    for j in range(0,i+1):
                        print(a,end=" ")
                    print()
                k=2*row-2
                for i in range(row,-1,-1):    
                    for j in range(k,0,-1):
                        print(end=" ")
                    k+=1
                    for j in range(0,i+1):
                        print(a,end=" ")
                    print()
            def INCREASING_number_diamond_pattern():
                a=int(input("Enter the number you want in the pattern:"))
                row=int(input("Enter the number of lines:"))
                k=2*row-2
                for i in range(0,row):    
                    for j in range(0,k):
                        print(end=" ")
                    k-=1
                    for j in range(0,i+1):
                        print(a,end=" ")
                        a+=1
                    print()
                k=2*row-2
                for i in range(row,-1,-1):    
                    for j in range(k,0,-1):
                        print(end=" ")
                    k+=1
                    for j in range(0,i+1):
                        print(a,end="")
                        a-=1
                    print()
            def CHARACTER_right_aligned_triangle_pattern():
                ch=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for INCREASE(RHS)\nPRESS 2 for DECREASE(RHS)\nPRESS 3 for INCREASE(lHS)\nPRESS 4 for DECREASE(LHS):"))
                if ch==1:
                    a=input("Enter the character you want in the pattern:")
                    n=int(input("Enter the number of lines:"))
                    for i in range(1,n+1):
                        for j in range(1,i+1):
                            print(a,end=" ")
                        print()
                elif ch==2:
                    a=input("Enter the character you want in the pattern:")
                    n=int(input("Enter the number of lines:"))
                    for i in range(n,0,-1):
                        for j in range(1,i+1):
                            print(a,end=" ")
                        print()
                elif ch==3:
                    a=input("Enter the character you want in the pattern:")
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(0,row):    
                        for j in range(0,k):
                            print(end=" ")
                        k-=1
                        for j in range(0,i+1):
                            print(a,end="")
                        print()
                elif ch==4:
                    a=input("Enter the character you want in the pattern:")
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(row,-1,-1):    
                        for j in range(k,0,-1):
                            print(end=" ")
                        k+=1
                        for j in range(0,i+1):
                            print(a,end="")
                        print()
                else:
                    print("Out of range")
            def CONSTANT_number_right_aligned_triangle_pattern():
                ch=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for INCREASE(RHS)\nPRESS 2 for DECREASE(RHS)\nPRESS 3 for INCREASE(lHS)\nPRESS 4 for DECREASE(LHS):"))
                if ch==1:
                    a=input("Enter the number you want in the pattern:")
                    n=int(input("Enter the number of lines:"))
                    for i in range(1,n+1):
                        for j in range(1,i+1):
                            print(a,end=" ")
                        print()
                elif ch==2:
                    a=input("Enter the number you want in the pattern:")
                    n=int(input("Enter the number of lines:"))
                    for i in range(n,0,-1):
                        for j in range(1,i+1):
                            print(a,end=" ")
                        print()
                elif ch==3:
                    a=input("Enter the number you want in the pattern:")
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(0,row):    
                        for j in range(0,k):
                            print(end=" ")
                        k-=1
                        for j in range(0,i+1):
                            print(a,end="")
                        print()
                elif ch==4:
                    a=input("Enter the number you want in the pattern:")
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(row,-1,-1):    
                        for j in range(k,0,-1):
                            print(end=" ")
                        k+=1
                        for j in range(0,i+1):
                            print(a,end="")
                        print()
                else:
                    print("Out of range")
            def INCREASING_number_right_aligned_triangle_pattern():
                ch=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for INCREASE(RHS)\nPRESS 2 for DECREASE(RHS)\nPRESS 3 for INCREASE(lHS)\nPRESS 4 for DECREASE(LHS):"))
                if ch==1:
                    a=int(input("Enter the starting number you want in the pattern:"))
                    n=int(input("Enter the number of lines:"))
                    for i in range(1,n+1):
                        for j in range(1,i+1):
                            print(a,end=" ")
                            n+=1
                        print()
                elif ch==2:
                    a=int(input("Enter the starting number you want in the pattern:"))
                    n=int(input("Enter the number of lines:"))
                    for i in range(n,0,-1):
                        for j in range(1,i+1):
                            print(a,end=" ")
                            a+=1
                        print()
                elif ch==3:
                    a=int(input("Enter the starting number you want in the pattern:"))
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(0,row):    
                        for j in range(0,k):
                            print(end=" ")
                        k-=1
                        for j in range(0,i+1):
                            print(a,end="")
                            a+=1
                        print()
                elif ch==4:
                    a=int(input("Enter the starting number you want in the pattern:"))
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(row,-1,-1):    
                        for j in range(k,0,-1):
                            print(end=" ")
                        k+=1
                        for j in range(0,i+1):
                            print(a,end="")
                            a+=1
                        print()
                else:
                    print("Out of range")
            def CHARATER_trangle_pattern():
                ch=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for NORMAL\nPRESS 2 for UPSIDEDOWN:"))
                if ch==1:
                    a=input("Enter the character you want in the pattern:")
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(0,row):    
                        for j in range(0,k):
                            print(end=" ")
                        k-=1
                        for j in range(0,i+1):
                            print(a,end=" ")
                        print()
                elif ch==2:
                    a=input("Enter the character you want in the pattern:")
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(row,-1,-1):    
                        for j in range(k,0,-1):
                            print(end=" ")
                        k+=1
                        for j in range(0,i+1):
                            print(a,end=" ")
                        print()
                else:
                    print("Out of range")
            def CONSTANT_number_trangle_pattern():
                ch=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for NORMAL\nPRESS 2 for UPSIDEDOWN:"))
                if ch==1:
                    a=input("Enter the number you want in the pattern:")
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(0,row):    
                        for j in range(0,k):
                            print(end=" ")
                        k-=1
                        for j in range(0,i+1):
                            print(a,end=" ")
                        print()
                elif ch==2:
                    a=input("Enter the number you want in the pattern:")
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(row,-1,-1):    
                        for j in range(k,0,-1):
                            print(end=" ")
                        k+=1
                        for j in range(0,i+1):
                            print(a,end=" ")
                        print()
                else:
                    print("Out of range")
            def INCREASING_number_trangle_pattern():
                ch=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for NORMAL\nPRESS 2 for UPSIDEDOWN:"))
                if ch==1:
                    a=int(input("Enter the starting number you want in the pattern:"))
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(0,row):    
                        for j in range(0,k):
                            print(end=" ")
                        k-=1
                        for j in range(0,i+1):
                            print(a,end=" ")
                            a+=1
                        print()
                elif ch==2:
                    a=int(input("Enter the starting number you want in the pattern:"))
                    row=int(input("Enter the number of lines:"))
                    k=2*row-2
                    for i in range(row,-1,-1):    
                        for j in range(k,0,-1):
                            print(end=" ")
                        k+=1
                        for j in range(0,i+1):
                            print(a,end="")
                            a+=1
                        print()
                else:
                    print("Out of range")
            print()
            cho=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for RIGHT ALIGNED TRIANGLE PATTERN\nPRESS 2 for TRIANGLE PATTERN\nPRESS 3 for DIAMOND PATTERN:\nPRESS 4 for SQUARE PATTERN:"))
            print()
            if cho==1:
                chh=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for CHARACTER RIGHT ALIGNED TRIANGLE PATTERN\nPRESS 2 for CONSTANT NUMBER RIGHT ALIGNED TRIANGLE PATTERN\nPRESS 3 for INCREASING NUMBER RIGHT ALIGNED TRIANGLE PATTERN:"))
                print()
                if chh==1:
                    _code_or_continue(CHARACTER_right_aligned_triangle_pattern)
                elif chh==2:
                    _code_or_continue(CONSTANT_number_right_aligned_triangle_pattern)
                elif chh==3:
                    _code_or_continue(INCREASING_number_right_aligned_triangle_pattern)
                else:
                    print("Out of range")
            elif cho==2:
                chh=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for CHARACTER TRIANGLE PATTERN\nPRESS 2 for CONSTANT NUMBER TRIANGLE PATTERN\nPRESS 3 for INCREASING NUMBER TRIANGLE PATTERN:"))
                print()
                if chh==1:
                    _code_or_continue(CHARATER_trangle_pattern)
                elif chh==2:
                    _code_or_continue(CONSTANT_number_trangle_pattern)
                elif chh==3:
                    _code_or_continue(INCREASING_number_trangle_pattern)
                else:
                    print("Out of range")
            elif cho==3:
                chh=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for CHARACTER DIAMOND PATTERN\nPRESS 2 for CONSTANT NUMBER DIAMOND PATTERN\nPRESS 3 for INCREASING NUMBER DIAMOND PATTERN:"))
                print()
                if chh==1:
                    _code_or_continue(CHARATER_diamond_pattern)
                if chh==2:
                    _code_or_continue(CONSTANT_number_diamond_pattern)
                if chh==3:
                    _code_or_continue(INCREASING_number_diamond_pattern)
                else:
                    print("Out of range")
            elif cho==4:
                chh=int(input("WHAT DO YOU WANT TO CALCULATE\nPRESS 1 for CHARACTER SQUARE PATTERN\nPRESS 2 for CONSTANT NUMBER SQUARE PATTERN\nPRESS 3 for INCREASING NUMBER SQUARE PATTERN:"))
                print()
                if chh==1:
                    _code_or_continue(Character_square_pattern)
                if chh==2:
                    _code_or_continue(CONSTANT_NUMBER_square_pattern)
                if chh==3:
                    _code_or_continue(INCREASING_NUMBER_square_pattern)
                else:
                    print("Out of range")
        def dice_game():
           print()
           n=int(input("Enter the number of chances:"))
           win_msg="you won"
           lose_msg='you lose'
           for i in range(n):
               print()
               num1=int(input('enter the first number:'))
               num2=int(input('enter the second numbe:'))
               import random
               a=random.randint(1,6)
               b=random.randint(1,6)
               if num1==a and num2==b:
                   print('the computers random numbers are',a,',',b)
                   print(win_msg)
                   break
               elif num1==b and num2==a:
                   print('the computers random numbers are',a,',',b)
                   print(win_msg)
                   break
               else:
                   print('the computers random numbers are',a,',',b)
                   print(lose_msg)
               n-=1
           print('game over')
        def data_types():
            def number_datatype():
                def integer_operations():
                    print()
                    a=int(input("Enter an integer:"))
                    print("Type of the variable=",type(a))
                    print("Absolute value=",abs(a))
                    print("Value after negation=",-a)
                    print("Square using pow()=",pow(a,2))
                    print("Floor division by 2=",a//2)
                    print("Modulus by 2=",a%2)
                def float_operations():
                    print()
                    a=float(input("Enter a float number:"))
                    print("Type of the variable=",type(a))
                    print("Rounded to 2 decimal places=",round(a,2))
                    print("Absolute value=",abs(a))
                    print("Integer part using int()=",int(a))
                    print("Square using pow()=",pow(a,2))
                def complex_operations():
                    print()
                    a=complex(input("Enter a complex number(eg:2+3j):"))
                    print("Type of the variable=",type(a))
                    print("Real part=",a.real)
                    print("Imaginary part=",a.imag)
                    print("Conjugate=",a.conjugate())
                def number_type_conversion():
                    print()
                    a=input("Enter a number:")
                    print("As integer=",int(float(a)))
                    print("As float=",float(a))
                    print("As complex=",complex(a))
                    print("As string=",str(a))
                print()
                ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for INTEGER FUNCTIONS\nPRESS 2 for FLOAT FUNCTIONS\nPRESS 3 for COMPLEX NUMBER FUNCTIONS\nPRESS 4 for TYPE CONVERSION:"))
                if ch==1:
                    _code_or_continue(integer_operations)
                elif ch==2:
                    _code_or_continue(float_operations)
                elif ch==3:
                    _code_or_continue(complex_operations)
                elif ch==4:
                    _code_or_continue(number_type_conversion)
                else:
                    print("Out of range")
            def string_datatype():
                def string_length_and_indexing():
                    print()
                    a=input("Enter a string:")
                    print("Length=",len(a))
                    print("First character=",a[0])
                    print("Last character=",a[-1])
                def string_slicing():
                    print()
                    a=input("Enter a string:")
                    s=int(input("Enter the start index:"))
                    e=int(input("Enter the end index:"))
                    print("Sliced string=",a[s:e])
                    print("Reversed string=",a[::-1])
                def string_case_conversion():
                    print()
                    a=input("Enter a string:")
                    print("Uppercase=",a.upper())
                    print("Lowercase=",a.lower())
                    print("Titlecase=",a.title())
                    print("Swapcase=",a.swapcase())
                    print("Capitalized=",a.capitalize())
                def string_search_and_count():
                    print()
                    a=input("Enter a string:")
                    b=input("Enter the substring to search:")
                    print("Find (index or -1)=",a.find(b))
                    print("Count of occurrences=",a.count(b))
                    print("Starts with substring=",a.startswith(b))
                    print("Ends with substring=",a.endswith(b))
                def string_replace_and_strip():
                    print()
                    a=input("Enter a string:")
                    old=input("Enter the substring to replace:")
                    new=input("Enter the new substring:")
                    print("After replace=",a.replace(old,new))
                    print("After strip=",a.strip())
                def string_split_and_join():
                    print()
                    a=input("Enter a sentence:")
                    b=a.split()
                    print("Split into words=",b)
                    c="-".join(b)
                    print("Joined with '-'=",c)
                def string_type_checks():
                    print()
                    a=input("Enter a string:")
                    print("isalpha()=",a.isalpha())
                    print("isdigit()=",a.isdigit())
                    print("isalnum()=",a.isalnum())
                    print("isupper()=",a.isupper())
                    print("islower()=",a.islower())
                    print("isspace()=",a.isspace())
                def string_membership_and_concat():
                    print()
                    a=input("Enter a string:")
                    b=input("Enter another string:")
                    c=input("Enter a substring to check membership:")
                    print("Concatenation=",a+b)
                    print("Repetition(x3)=",a*3)
                    print(c,"in",a,"=",c in a)
                print()
                ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for LENGTH AND INDEXING\nPRESS 2 for SLICING\nPRESS 3 for CASE CONVERSION\nPRESS 4 for SEARCH AND COUNT\nPRESS 5 for REPLACE AND STRIP\nPRESS 6 for SPLIT AND JOIN\nPRESS 7 for TYPE CHECKS\nPRESS 8 for MEMBERSHIP AND CONCATENATION:"))
                if ch==1:
                    _code_or_continue(string_length_and_indexing)
                elif ch==2:
                    _code_or_continue(string_slicing)
                elif ch==3:
                    _code_or_continue(string_case_conversion)
                elif ch==4:
                    _code_or_continue(string_search_and_count)
                elif ch==5:
                    _code_or_continue(string_replace_and_strip)
                elif ch==6:
                    _code_or_continue(string_split_and_join)
                elif ch==7:
                    _code_or_continue(string_type_checks)
                elif ch==8:
                    _code_or_continue(string_membership_and_concat)
                else:
                    print("Out of range")
            def list_datatype():
                def list_creation_and_access():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=[int(i) for i in a.split()]
                    print("List=",b)
                    print("First element=",b[0])
                    print("Last element=",b[-1])
                    print("Length=",len(b))
                def list_add_elements():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=[int(i) for i in a.split()]
                    n=int(input("Enter a number to append:"))
                    b.append(n)
                    print("After append=",b)
                    p=int(input("Enter the position to insert at:"))
                    v=int(input("Enter the value to insert:"))
                    b.insert(p,v)
                    print("After insert=",b)
                def list_remove_elements():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=[int(i) for i in a.split()]
                    n=int(input("Enter the number to remove:"))
                    if n in b:
                        b.remove(n)
                    print("After remove=",b)
                    b.pop()
                    print("After pop(last element)=",b)
                def list_sort_and_reverse():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=[int(i) for i in a.split()]
                    b.sort()
                    print("Sorted list=",b)
                    b.reverse()
                    print("Reversed list=",b)
                def list_search_and_count():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=[int(i) for i in a.split()]
                    n=int(input("Enter the number to search:"))
                    if n in b:
                        print("Index=",b.index(n))
                    else:
                        print("Not found")
                    print("Count of occurrences=",b.count(n))
                def list_slicing():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=[int(i) for i in a.split()]
                    s=int(input("Enter the start index:"))
                    e=int(input("Enter the end index:"))
                    print("Sliced list=",b[s:e])
                print()
                ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for CREATION AND ACCESS\nPRESS 2 for ADDING ELEMENTS\nPRESS 3 for REMOVING ELEMENTS\nPRESS 4 for SORT AND REVERSE\nPRESS 5 for SEARCH AND COUNT\nPRESS 6 for SLICING:"))
                if ch==1:
                    _code_or_continue(list_creation_and_access)
                elif ch==2:
                    _code_or_continue(list_add_elements)
                elif ch==3:
                    _code_or_continue(list_remove_elements)
                elif ch==4:
                    _code_or_continue(list_sort_and_reverse)
                elif ch==5:
                    _code_or_continue(list_search_and_count)
                elif ch==6:
                    _code_or_continue(list_slicing)
                else:
                    print("Out of range")
            def tuple_datatype():
                def tuple_creation_and_access():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=tuple(int(i) for i in a.split())
                    print("Tuple=",b)
                    print("First element=",b[0])
                    print("Last element=",b[-1])
                    print("Length=",len(b))
                def tuple_search_and_count():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=tuple(int(i) for i in a.split())
                    n=int(input("Enter the number to search:"))
                    if n in b:
                        print("Index=",b.index(n))
                    else:
                        print("Not found")
                    print("Count of occurrences=",b.count(n))
                def tuple_slicing_and_concat():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=tuple(int(i) for i in a.split())
                    s=int(input("Enter the start index:"))
                    e=int(input("Enter the end index:"))
                    print("Sliced tuple=",b[s:e])
                    c=input("Enter another set of numbers separated by space:")
                    d=tuple(int(i) for i in c.split())
                    print("Concatenated tuple=",b+d)
                print()
                ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for CREATION AND ACCESS\nPRESS 2 for SEARCH AND COUNT\nPRESS 3 for SLICING AND CONCATENATION:"))
                if ch==1:
                    _code_or_continue(tuple_creation_and_access)
                elif ch==2:
                    _code_or_continue(tuple_search_and_count)
                elif ch==3:
                    _code_or_continue(tuple_slicing_and_concat)
                else:
                    print("Out of range")
            def dictionary_datatype():
                def dictionary_creation_and_access():
                    print()
                    d={}
                    n=int(input("Enter the number of key-value pairs:"))
                    for i in range(n):
                        k=input("Enter the key:")
                        v=input("Enter the value:")
                        d[k]=v
                    print("Dictionary=",d)
                    k=input("Enter a key to access its value:")
                    print("Value=",d.get(k,"Key not found"))
                def dictionary_add_and_update():
                    print()
                    d={}
                    n=int(input("Enter the number of key-value pairs:"))
                    for i in range(n):
                        k=input("Enter the key:")
                        v=input("Enter the value:")
                        d[k]=v
                    k=input("Enter a new key to add/update:")
                    v=input("Enter its value:")
                    d[k]=v
                    print("Updated dictionary=",d)
                def dictionary_remove():
                    print()
                    d={}
                    n=int(input("Enter the number of key-value pairs:"))
                    for i in range(n):
                        k=input("Enter the key:")
                        v=input("Enter the value:")
                        d[k]=v
                    k=input("Enter the key to remove:")
                    if k in d:
                        d.pop(k)
                    print("After removal=",d)
                def dictionary_keys_values_items():
                    print()
                    d={}
                    n=int(input("Enter the number of key-value pairs:"))
                    for i in range(n):
                        k=input("Enter the key:")
                        v=input("Enter the value:")
                        d[k]=v
                    print("Keys=",list(d.keys()))
                    print("Values=",list(d.values()))
                    print("Items=",list(d.items()))
                print()
                ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for CREATION AND ACCESS\nPRESS 2 for ADD AND UPDATE\nPRESS 3 for REMOVE\nPRESS 4 for KEYS, VALUES AND ITEMS:"))
                if ch==1:
                    _code_or_continue(dictionary_creation_and_access)
                elif ch==2:
                    _code_or_continue(dictionary_add_and_update)
                elif ch==3:
                    _code_or_continue(dictionary_remove)
                elif ch==4:
                    _code_or_continue(dictionary_keys_values_items)
                else:
                    print("Out of range")
            def set_datatype():
                def set_creation_and_add():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=set(int(i) for i in a.split())
                    print("Set=",b)
                    n=int(input("Enter a number to add:"))
                    b.add(n)
                    print("After add=",b)
                def set_remove():
                    print()
                    a=input("Enter numbers separated by space:")
                    b=set(int(i) for i in a.split())
                    n=int(input("Enter the number to remove:"))
                    b.discard(n)
                    print("After remove=",b)
                def set_union_intersection_difference():
                    print()
                    a=input("Enter the first set of numbers separated by space:")
                    b=set(int(i) for i in a.split())
                    c=input("Enter the second set of numbers separated by space:")
                    d=set(int(i) for i in c.split())
                    print("Union=",b|d)
                    print("Intersection=",b&d)
                    print("Difference(first-second)=",b-d)
                    print("Symmetric difference=",b^d)
                def set_subset_and_superset():
                    print()
                    a=input("Enter the first set of numbers separated by space:")
                    b=set(int(i) for i in a.split())
                    c=input("Enter the second set of numbers separated by space:")
                    d=set(int(i) for i in c.split())
                    print("Is first a subset of second=",b.issubset(d))
                    print("Is first a superset of second=",b.issuperset(d))
                print()
                ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for CREATION AND ADD\nPRESS 2 for REMOVE\nPRESS 3 for UNION, INTERSECTION AND DIFFERENCE\nPRESS 4 for SUBSET AND SUPERSET:"))
                if ch==1:
                    _code_or_continue(set_creation_and_add)
                elif ch==2:
                    _code_or_continue(set_remove)
                elif ch==3:
                    _code_or_continue(set_union_intersection_difference)
                elif ch==4:
                    _code_or_continue(set_subset_and_superset)
                else:
                    print("Out of range")
            def boolean_datatype():
                def boolean_comparisons():
                    print()
                    a=int(input("Enter the first number:"))
                    b=int(input("Enter the second number:"))
                    print("a==b=",a==b)
                    print("a!=b=",a!=b)
                    print("a>b=",a>b)
                    print("a<b=",a<b)
                    print("a>=b=",a>=b)
                    print("a<=b=",a<=b)
                def boolean_logical_operators():
                    print()
                    a=input("Enter True or False for the first value:")
                    b=input("Enter True or False for the second value:")
                    x=a.strip()=="True"
                    y=b.strip()=="True"
                    print("x and y=",x and y)
                    print("x or y=",x or y)
                    print("not x=",not x)
                print()
                ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for COMPARISON OPERATORS\nPRESS 2 for LOGICAL OPERATORS:"))
                if ch==1:
                    _code_or_continue(boolean_comparisons)
                elif ch==2:
                    _code_or_continue(boolean_logical_operators)
                else:
                    print("Out of range")
            print()
            ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for NUMBER (int,float,complex)\nPRESS 2 for STRING\nPRESS 3 for LIST\nPRESS 4 for TUPLE\nPRESS 5 for DICTIONARY\nPRESS 6 for SET\nPRESS 7 for BOOLEAN:"))
            if ch==1:
                number_datatype()
            elif ch==2:
                string_datatype()
            elif ch==3:
                list_datatype()
            elif ch==4:
                tuple_datatype()
            elif ch==5:
                dictionary_datatype()
            elif ch==6:
                set_datatype()
            elif ch==7:
                boolean_datatype()
            else:
                print("Out of range")
        def module_functions():
            def math_module():
                def math_power_and_roots():
                    print()
                    import math
                    a=float(input("Enter the number:"))
                    b=float(input("Enter the power:"))
                    print("Power using math.pow()=",math.pow(a,b))
                    print("Square root using math.sqrt()=",math.sqrt(a))
                    print("Factorial using math.factorial()=",math.factorial(int(a)))
                def math_ceil_floor_and_fabs():
                    print()
                    import math
                    a=float(input("Enter a number:"))
                    print("Ceil value using math.ceil()=",math.ceil(a))
                    print("Floor value using math.floor()=",math.floor(a))
                    print("Absolute value using math.fabs()=",math.fabs(a))
                    print("Truncated value using math.trunc()=",math.trunc(a))
                def math_gcd_and_log():
                    print()
                    import math
                    a=int(input("Enter the first number:"))
                    b=int(input("Enter the second number:"))
                    print("GCD using math.gcd()=",math.gcd(a,b))
                    c=float(input("Enter a number for logarithm:"))
                    print("Natural log using math.log()=",math.log(c))
                    print("Log base 10 using math.log10()=",math.log10(c))
                    print("Log base 2 using math.log2()=",math.log2(c))
                def math_constants():
                    print()
                    import math
                    print("Value of pi=",math.pi)
                    print("Value of e=",math.e)
                    print("Value of tau=",math.tau)
                    print("Value of infinity=",math.inf)
                print()
                ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for POWER AND SQUARE ROOT\nPRESS 2 for CEIL, FLOOR AND FABS\nPRESS 3 for GCD AND LOGARITHM\nPRESS 4 for CONSTANTS:"))
                if ch==1:
                    _code_or_continue(math_power_and_roots)
                elif ch==2:
                    _code_or_continue(math_ceil_floor_and_fabs)
                elif ch==3:
                    _code_or_continue(math_gcd_and_log)
                elif ch==4:
                    _code_or_continue(math_constants)
                else:
                    print("Out of range")
            def random_module():
                def random_integer_and_float():
                    print()
                    import random
                    a=int(input("Enter the lower limit:"))
                    b=int(input("Enter the upper limit:"))
                    print("Random integer using random.randint()=",random.randint(a,b))
                    print("Random float(0 to 1) using random.random()=",random.random())
                    print("Random float using random.uniform()=",random.uniform(a,b))
                def random_choice_and_sample():
                    print()
                    import random
                    a=input("Enter numbers separated by space:")
                    b=[int(i) for i in a.split()]
                    print("Random choice using random.choice()=",random.choice(b))
                    n=int(input("Enter how many random samples to pick:"))
                    print("Random sample using random.sample()=",random.sample(b,n))
                def random_shuffle_and_randrange():
                    print()
                    import random
                    a=input("Enter numbers separated by space:")
                    b=[int(i) for i in a.split()]
                    random.shuffle(b)
                    print("Shuffled list using random.shuffle()=",b)
                    c=int(input("Enter the range limit for randrange():"))
                    print("Random number using random.randrange()=",random.randrange(c))
                print()
                ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for RANDOM INTEGER AND FLOAT\nPRESS 2 for RANDOM CHOICE AND SAMPLE\nPRESS 3 for SHUFFLE AND RANDRANGE:"))
                if ch==1:
                    _code_or_continue(random_integer_and_float)
                elif ch==2:
                    _code_or_continue(random_choice_and_sample)
                elif ch==3:
                    _code_or_continue(random_shuffle_and_randrange)
                else:
                    print("Out of range")
            def statistics_module():
                def statistics_mean_median_mode():
                    print()
                    import statistics
                    a=input("Enter numbers separated by space:")
                    b=[float(i) for i in a.split()]
                    print("Mean using statistics.mean()=",statistics.mean(b))
                    print("Median using statistics.median()=",statistics.median(b))
                    print("Mode using statistics.mode()=",statistics.mode(b))
                def statistics_variance_and_stdev():
                    print()
                    import statistics
                    a=input("Enter numbers separated by space:")
                    b=[float(i) for i in a.split()]
                    print("Variance using statistics.variance()=",statistics.variance(b))
                    print("Standard deviation using statistics.stdev()=",statistics.stdev(b))
                print()
                ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for MEAN, MEDIAN AND MODE\nPRESS 2 for VARIANCE AND STANDARD DEVIATION:"))
                if ch==1:
                    _code_or_continue(statistics_mean_median_mode)
                elif ch==2:
                    _code_or_continue(statistics_variance_and_stdev)
                else:
                    print("Out of range")
            print()
            ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for MATH MODULE\nPRESS 2 for RANDOM MODULE\nPRESS 3 for STATISTICS MODULE:"))
            if ch==1:
                math_module()
            elif ch==2:
                random_module()
            elif ch==3:
                statistics_module()
            else:
                print("Out of range")
        def sorting():
            def bubble_sort():
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                n=len(b)
                for i in range(n-1):
                    for j in range(n-1-i):
                        if b[j]>b[j+1]:
                            b[j],b[j+1]=b[j+1],b[j]
                print("Sorted list(ascending)=",b)
            def selection_sort():
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                n=len(b)
                for i in range(n-1):
                    m=i
                    for j in range(i+1,n):
                        if b[j]<b[m]:
                            m=j
                    b[i],b[m]=b[m],b[i]
                print("Sorted list(ascending)=",b)
            def insertion_sort():
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                n=len(b)
                for i in range(1,n):
                    k=b[i]
                    j=i-1
                    while j>=0 and b[j]>k:
                        b[j+1]=b[j]
                        j-=1
                    b[j+1]=k
                print("Sorted list(ascending)=",b)
            def sort_descending():
                print()
                a=input("Enter numbers separated by space:")
                b=[int(i) for i in a.split()]
                n=len(b)
                for i in range(n-1):
                    for j in range(n-1-i):
                        if b[j]<b[j+1]:
                            b[j],b[j+1]=b[j+1],b[j]
                print("Sorted list(descending)=",b)
            print()
            ch=int(input("WHAT DO YOU WANT TO DO\nPRESS 1 for BUBBLE SORT\nPRESS 2 for SELECTION SORT\nPRESS 3 for INSERTION SORT\nPRESS 4 for DESCENDING ORDER SORT:"))
            if ch==1:
                _code_or_continue(bubble_sort)
            elif ch==2:
                _code_or_continue(selection_sort)
            elif ch==3:
                _code_or_continue(insertion_sort)
            elif ch==4:
                _code_or_continue(sort_descending)
            else:
                print("Out of range")
        while True:
            print()
            print("CLASS 11 CS GPT")
            print()
            choose=int(input("WHAT DO YOU WANT TO CALCULATOR\nPRESS  1 for CALCULATOR\nPRESS  2 for PALINDROME IDENTIFIER \nPRESS  3 for GREATEST NUMBER\nPRESS  4 for VOTE ELIGIBILITY\nPRESS  5 for FACTORIAL\nPRESS  6 for EVEN OR ODD\nPRESS  7 for TABLES\nPRESS  8 for PATTERN\nPRESS  9 for DICE GAME \nPRESS 10 for CLASS 10 PERCENTAGE CALCULATOR \nPRESS 11 for PRIME NUMBER \nPRESS 12 for ARMSTRONG NUMBER \nPRESS 13 for NEON NUMBER \nPRESS 14 for PERFECT NUMBER \nPRESS 15 for DATA TYPES \nPRESS 16 for MODULE \nPRESS 17 for SORTING:"))
            if choose==1:
                calculator()
            elif choose==2:
                _code_or_continue(palindrome)
            elif choose==3:
                _code_or_continue(Greatest_number)
            elif choose==4:
                _code_or_continue(vote_eligibility)
            elif choose==5:
                _code_or_continue(factorial)
            elif choose==6:
                _code_or_continue(odd_or_even)
            elif choose==7:
                _code_or_continue(tables)
            elif choose==8:
                pattern()
            elif choose==9:
                _code_or_continue(dice_game)
            elif choose==10:
                _code_or_continue(class_10_percentage_calculator)
            elif choose==11:
                prime_numbers()
            elif choose==12:
                armstrong_number()
            elif choose==13:
                neon_number()
            elif choose==14:
                perfect_number()
            elif choose==15:
                data_types()
            elif choose==16:
                module_functions()
            elif choose==17:
                sorting()
            else:
                print("Out of range")
            print()
            c=input(("DO YOU WANT TO CONTINUE(Y/N):"))
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
# 11. The VS Code-styled terminal — now a native Tkinter window (no browser)
# =============================================================================

COLORS = dict(
    editor_bg="#1e1e1e", titlebar_bg="#323233", tab_bg="#2d2d2d",
    tab_active_bg="#1e1e1e", panel_header_bg="#252526", border="#3c3c3c",
    text="#cccccc", text_dim="#858585", accent="#007acc",
    white="#d4d4d4", red="#f14c4c",
)

# Matches the \033[31m ... \033[0m codes the calculator prints on errors.
_ANSI_RE = re.compile(r"\x1b\[(\d+)m")


def _pick_mono_font(root: tk.Tk) -> str:
    preferred = ["Cascadia Code", "Consolas", "Menlo", "SF Mono", "DejaVu Sans Mono", "Courier New"]
    available = set(tkfont.families(root))
    for name in preferred:
        if name in available:
            return name
    return "TkFixedFont"


class TerminalApp:
    """Native window styled like a VS Code terminal. Runs the calculator on
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
        root.title("Class 11 CS GPT")
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
        tk.Label(titlebar, text="Class 11 CS GPT", bg=COLORS["titlebar_bg"],
                 fg=COLORS["text_dim"], font=(mono, 10)).pack(side="left", expand=True)
        tk.Frame(titlebar, bg=COLORS["titlebar_bg"], width=84).pack(side="right")

        # Tab bar
        tabbar = tk.Frame(window, bg=COLORS["tab_bg"])
        tabbar.pack(fill="x", side="top")
        tk.Label(tabbar, text="\u25cf Class 11 CS GPT", bg=COLORS["tab_bg"], fg=COLORS["text_dim"],
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

    # ---- stdio bridge (used by the calculator thread) ---------------------
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
            cs()
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
