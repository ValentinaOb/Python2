import math

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
    
    signs=[",",".","!","?"]
    
    str='Hello, Bye'
    str1='Hello, Bye? How, Bye!!! Hello! Hello. Are! Bye? Hello, Bye. You?'
    s=""
    s1=""

    for i in str:
        if i not in signs:
            s += i

    for i in str1:
        if i not in signs:
            s1 += i

    print ("S: ", s)
    print ("S1: ", s1)

    s2=s.split(' ')
    s3=s1.split(' ')

    for i in s3[:]:
        if i in s2:
            s3.remove(i)
    r=""
    for i in s3:
        r+=(i)+" "

    print ("Result: ", r)

    #
    
    print ("\nInput s (del): ")
    text = input()
    print ("Input s1: ")
    text1 = input()

    t=""
    t1=""
    
    for i in text:
        if i not in signs:
            t += i

    for i in text1:
        if i not in signs:
            t1 += i

    print ("T: ", t)
    print ("T1: ", t1)

    t2=t.split(' ')
    t3=t1.split(' ')

    for i in t3[:]:
        if i in t2:
            t3.remove(i)
    r1=""
    for i in t3:
        r1+=(i)+" "

    print ("Result: ", r1)           
    
    
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