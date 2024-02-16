import math
import re

def suma(x,a,epsi):
    sum_v=0.0
    k=0
    term =1.0

    while abs(term)>=epsi:
        term = ((-1**k)*(x**(-3*k)))/((a**5)+math.factorial(k))
        sum_v+=term
        k+=1
        
    return sum_v,k


def ex ():

    a = float(input("A (a!=0): "))
    while(a==0): a = float(input())
        
    
    x = float(input("X (x!=0): "))
    while(x==0): x = float(input())

    e = float(input("E (e>0): "))
    while(e<0): e = float(input())
        
    
    sum,k=suma(x,a,e)
    print ("\nResult: ", sum)
    print ("K: ", k)
'''        
    k=0
    sum=0.0
    f=1.0

    while abs(f)>=e :
        f = ((-1**k)*(x**(-3*k)))/((a**5)+math.factorial(k))
        sum+=f
        k+=1 
 '''

    


def ex1 ():
    
    print ("X: ")
    x = int(input())
    while(x==0):
        x = int(input())

    print ("E (e>0): ")
    e = int(input())
    while(e<0):
        e = int(input())


    a0=x
    a=x
    an=1
    k=1
    r=1000
    
    while(k<100):
        a=(2/7)*an+(x/(3*(an**5)))
        r=a-an
        an=a
        k+=1
        
        if(r<e): break
            
        

    print ("\nA0: ", a0)
    print ("A1: ", r)
    print ("K: ", k)

def ex2 ():
    
    S=" Hello, Bye"
    print ("S: ", S)
    S1=" Hello, Bye? How, Bye!!! Hello! Hello. Are! Bye? Hello, Bye. You?"
    print ("S1: ", S1)

    words=" "
    words = re.split("[,.!?@#$%^*&()_+/-]", S)
    print ("W: ", words)

    wo = re.split("[,.!?@#$%^*&()_+/-]", S1)
   # print ("Wo: ", wo)
    
    
    for i in wo[:]:
        if (i in words):
           # print ("W: ", wo)  
            wo.remove(i)
    
   # print ("Wo: ", wo)
    
    r = ""

    for ele in wo:
        r += ele

    print ("R: ", r)        
    
    #

    print ("Input s (del): ")
    s = str(input())
    print ("Input s1: ")
    s1 = str(input())

    words1=" "
    words1 = re.split("[,.!?@#$%^*&()_+/-]", s)
    print ("W: ", words1)

    wo1 = re.split("[,.!?@#$%^*&()_+/-]", s1)
   # print ("Wo: ", wo1)
    
    
    for i in wo1[:]:
        if (i in words1):
           # print ("W: ", wo)  
            wo1.remove(i)
    
   # print ("Wo: ", wo1)
    
    r1 = ""

    for ele in wo1:
        r1 += ele

    print ("R: ", r1)            

def ex3 ():

    print ("S: ")
    s = str(input())
    
    s1=rev(s)
    status=comparison(s,s1)
    if(status==True): print ("Yes")
    else: print ("No") 
    
def comparison(s,s1):
        if (s1==s):
            return True
        else: return False

def rev(s):
    if len(s) == 0:
        return s
    else:
        return rev(s[1:]) + s[0]


print ("N: ")
n = int(input())

match n:
        case 1:
            ex()
        case 2:
            ex1()
        case 3:
            ex2()
        case 4:
            ex3()
        case default:
            print ("Error")