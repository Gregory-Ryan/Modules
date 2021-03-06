import math
from decimal import Decimal

def Re_s(z) :
    #Finds real part of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    sr = str(z)
    if sr[len(sr) - 1] == 'i' :
        for count in range(0, len(sr)) :
            place = sr[count]
            if_e = sr[count - 1]
            if place == '+' :
                if if_e == 'e' :
                    continue
                else :
                    sr2 = sr[0 : count - 1]
                    sr22 = Decimal(sr2)
                    return sr22
        return 0
    else :
        zz = Decimal(z)
        return zz
    
def Im_s(z) :
    #Finds the imaginary part of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    sr = str(z)
    if sr[len(sr) - 1] == 'i' :
        for count in range(0, len(sr)) :
            place = sr[count]
            if_e = sr[count - 1]
            if place == '+' :
                if if_e == 'e' :
                    continue
                else :
                    sr2 = sr[count + 1 : len(sr) - 1]
                    if sr2 == ' ' :
                        fin = Decimal(1)
                    elif sr2 == ' -' :
                        fin = Decimal(-1)
                    else :
                        fin = Decimal(sr2)
                    return fin
        sr22 = sr[0 : len(sr) - 1]
        if sr22 == '' :
            return Decimal(1)
        elif sr22 == '-' :
            return Decimal(-1)
        else :
            return Decimal(sr22)
    else :
        return 0

def Re(z) :
    if not type(z) == tuple:
        z = (Re_s(z),Im_s(z))
    (x,y) = z
    return Decimal(x)

def Im(z) :
    if not type(z) == tuple:
        z = (Re_s(z),Im_s(z))
    (x,y) = z
    return Decimal(y)

def conj(z) :
    return (Re(z),- Im(z))

def I(z):
    return (Re(z),Im(z))

def I_s(z) :
    #Takes the Re(z) and the Im(z) and turns it into a complex number(repersented by a string)
    #x is the Re(z) and y is the Im(z)
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    if y == 0 :
        z = str(Decimal(x))
    elif x == 0 :
        if y == 1 :
            z = 'i'
        elif y == -1 :
            z = '-i'
        else :
            z = str(Decimal(y)) + 'i'
    else : 
        if y == 1 :
            z = str(Decimal(x)) + " " + "+" + " " + 'i'
        elif y == -1 :
            z = str(Decimal(x)) + " " + "+" + " " + '-i'
        else :
            z = str(Decimal(x)) + " " + "+" + " " + str(Decimal(y)) + 'i'
    return z

def conj_s(z) :
    #Takes the Re(z) and the Im(z) and turns it into z_bar(repersented by a string)
    #x is the Re(z) and y is the Im(z)
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    if y == 0 :
        z = str(Decimal(x))
    elif x == 0 :
        if y == 1 :
            z = '-i'
        elif y == -1 :
            z = 'i'
        else :
            z = '-' + str(Decimal(x)) + 'i'
    else :
        if y == 1 :
            z = str(Decimal(x)) + " " + "" + " " + '-i'
        elif y == -1 :
            z = str(Decimal(x)) + " " + "" + " " + 'i'
        else :
            if y[0,1] == '-' :
                z = str(Decimal(x)) + " " + "+" + " " + str(Decimal(y)) + 'i'
            else:
                z = str(Decimal(x)) + " " + "+" + " " + "-" + str(Decimal(y)) + 'i'
    return z

def neg(z) :
    #Makes the complex number negitive
    #The input is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    z1 = (-x,-y)
    return z1
    
def add(z,z1) :
    #Adds two complex numbers
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    x1 = Re(z1)
    y1 = Im(z1)
    u = x + x1
    v = y + y1 
    z2 = (u,v)
    return z2

def subt(z,z1) :
    #Finds the difference between two complex numbers (z - z1)
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    x1 = Re(z1)
    y1 = Im(z1)
    u = x - x1
    v = y - y1 
    z2 = (u,v)
    return z2

def multi(z,z1) :
    #Multiplys two complex numbers
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    x1 = Re(z1)
    y1 = Im(z1)
    u = x * x1 - y * y1
    v = x1 * y + x * y1 
    z2 = (u,v)
    return z2

def sqr(z) :
    #Squares a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = x ** 2 - y ** 2
    v = 2 * x * y
    z1 = (u,v)
    return z1

def Arg(z) :
    #Finds the principal argument of a complex number
    #The input is a string in the form x + yi
    #The output is in radians
    x = Re(z)
    y = Im(z)
    t = Decimal(math.atan2(y,x))
    return t

def arg(z) :
    #Finds the argument of a complex number
    #The input is a string in the form x + yi
    #The output is in radians
    x = Re(z)
    y = Im(z)
    t = Decimal(math.atan(y/x))
    return t

def mod(z) :
    #Find the magnitude/norm/modulus of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    z1 = Decimal(math.sqrt(x ** 2 + y ** 2))
    return z1

def Log(z) :
    #Finds the principal log of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = math.log(mod(z))
    v = Arg(z)
    z1 = (u,v)
    return z1

def log(z) :
    #Finds the log of a complex numjber
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = math.log(mod(z))
    v = arg(z)
    z1 = (u,v)
    return z1

def eul(r,t) :
    #r is the radius and t is the angle in radians(they must be real)
    #The output is a string in the form x + yi
    u = Decimal(float(r) * math.cos(t))
    v = Decimal(float(r) * math.sin(t))
    z1 = (u,v)
    return z1

def eul_c(r,z) :
    #r is the radius and t is the angle in radians(they can be complex)
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = Decimal(math.exp(-y)) * Decimal(math.cos(x))
    v = Decimal(math.exp(-y)) * Decimal(math.sin(x))
    z1 = (u,v)
    z2 = multi(r,z1)
    return z2

def power(z,p) :
    #Puts a complex number to the power of a number(it can be complex)
    #z is a string in the form x + yi and p is the power(it can be complex)
    #The output is a string in the form x + yi
    x = Re(p)
    y = Im(p)
    r = multi(mod(z) ** x, eul_c(1,y * Decimal(math.log(mod(z))))) 
    t = Arg(z)
    pow = multi(t,p)
    z1 = eul_c(r, pow)
    return z1

def div(z,z1) :
    #Divides a complex number by an other complex number (z/z1)
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    r = mod(z) / mod(z1)
    t = Arg(z) - Arg(z1)
    z2 = eul(r,t)
    return z2

def sqrt(z) :
    z1 = power(z,0.5)
    return z1

def sin(z) :
    #Finds the sine of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = eul(math.exp(-y), x)
    v = eul(math.exp(-y), -x)
    s = subt(u,v)
    z1 = multi(s, '-0.5i')
    return z1

def csc(z) :
    #Finds the cosecant of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = sin(z)
    z1 = div(1,u)
    return z1

def cos(z) :
    #Finds the cosine of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = eul(math.exp(-y), x)
    v = eul(math.exp(-y), -x)
    s = add(u,v)
    z1 = multi(s, '0.5')
    return z1

def sec(z) :
    #Finds the secant of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = cos(z)
    z1 = div(1,u)
    return z1

def tan(z) :
    #Finds the tangent of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    s = sin(z)
    c = cos(z)
    z1 = div(s,c)
    return z1

def cot(z) :
    #Finds the cotangent of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = tan(z)
    z1 = div(1,u)
    return z1

def sinh(z) :
    #Finds the hyperbolic sine of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = eul(math.exp(-x), y)
    v = eul(math.exp(-x), -y)
    s = subt(u,v)
    z1 = multi(s, '0.5')
    return z1

def csch(z) :
    #Finds the hyperbolic cosecant of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = sinh(z)
    z1 = div(1,u)
    return z1

def cosh(z) :
    #Finds the hyperbolic cosine of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    x = Re(z)
    y = Im(z)
    u = eul(math.exp(-x), y)
    v = eul(math.exp(-x), -y)
    s = add(u,v)
    z1 = multi(s, '0.5')
    return z1

def sech(z) :
    #Finds the hyperbolic secant of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = cosh(z)
    z1 = div(1,u)
    return z1

def tanh(z) :
    #Finds the hyperbolic tangent of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    s = sinh(z)
    c = cosh(z)
    z1 = div(s,c)
    return z1

def coth(z) :
    #Finds the hyperbolic cotangent of a complex number
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    u = tan(z)
    z1 = div(1,u)
    return z1

def acos(z) :
    if mod(Re(z)) == 1 :
        return div(math.pi,2)
    t = add(div(math.pi,2),multi('i',Log(add(multi('i',z),sqrt(subt(1,sqr(z)))))))
    return t

def asin(z) :
    if mod(Re(z)) == 1 :
        return 0
    t = multi('-i',Log(add(multi('i',z),sqrt(subt(1,sqr(z))))))
    return t

def atan(z) :
    t = multi('0.5i', subt(Log(subt(1,multi('i',z))),Log(add(1,multi('i',z)))))
    return t

def acot(z) :
    t = atan(div(1,z))
    return t

def acsc(z) :
    t = asin(div(1,z))
    return t

def asec(z) :
    t = acos(div(1,z))
    return t

def acosh(z) :
    t = Log(add(z,sqrt(subt(sqr(z),1))))
    return t

def asinh(z) :
    t = multi('i',asin(multi('-i',z)))
    return t

def atanh(z) :
    t = multi('-i',atan(multi('i',z)))
    return t

def acoth(z) :
    t = atanh(div(1,z))
    return t

def acsch(z) :
    t = asinh(div(1,z))
    return t

def asech(z) :
    t = acosh(div(1,z))
    return t

def gamma(z) :
    #Calculates the Gamma Function
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    if Re(z) % 1 == 0 and Re(z) <= 0 :
        return math.nan
    else:
        z1 = multi(div(1, z), div(power(2, z), add(1, z)))
        for i in range(2,10000) :
                z2 = div(power((1 + 1 / i), z), add(1, div(z, i)))
                z1 = multi(z1, z2)
                z3 = div(power((1 + 1 / (i + 1)), z), add(1, div(z, i + 1)))
                z4 = multi(z1, z3)
                if mod(subt(z4,multi(0.0000000999,z4))) <= mod(z1) <= mod(add(z4,multi(0.0000000999,z4)))   :
                    return z1
        return math.inf

def zeta(z) :
    #fix
    #Calculates the Riemann zeta function 
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    if Re(z) >= 1 :
        z1 = power(1,neg(z))
        for i in range(2,1000000) :
            z2 = power(i,neg(z))
            z1 = add(z1,z2)
            z3 = power(int(i + 1),neg(z))
            z4 = add(z1,z3)
            if mod(subt(z4,multi(0.00000000999,z4))) <= mod(z1) <= mod(add(z4,multi(0.00000000999,z4)))   :
                return z4 
        return math.inf
    elif Re(z) >= 0 :
        z1 = power(1,neg(z))
        for i in range(2,10000000) :
            z2 = multi((-1) ** (i - 1), power(i,neg(z)))
            z1 = add(z1,z2)
            z3 = multi((-1) ** i, power(int(i + 1),neg(z)))
            z4 = add(z1,z3)
            if Decimal(mod(subt(z4,multi(0.0000999,z4)))) <= Decimal(mod(z1)) <= Decimal(mod(add(z4,multi(0.0000999,z4))))   :
                print(div(z4,subt(1, power(2, subt(1, z)))))
                return div(z4,subt(1, power(2, subt(1, z)))) 
        return math.inf
    if Re(z) < 0 :
        z1 = multi(multi(power(math.pi, subt(z, 0.5)), div(gamma(div(subt(1, z), 2)), gamma(div(z,2)))), zeta(subt(1, z))) 
        return z1

def eta(z) :
    #fix
    #Calculates the Dirichlet Eta Function
    #The input is a string in the form x + yi
    #The output is a string in the form x + yi
    if Re(z) >= 1 :
        z1 = power(1,neg(z))
        for i in range(2,1000000) :
            z2 = power(i,neg(z))
            z1 = add(z1,z2)
            z3 = power(int(i + 1),neg(z))
            z4 = add(z1,z3)
            if mod(subt(z4,multi(0.00000000999,z4))) <= mod(z1) <= mod(add(z4,multi(0.00000000999,z4)))   :
                return multi(z4,subt(1, power(2, subt(1, z))))
        return math.inf
    elif Re(z) >= 0 :
        z1 = power(1,neg(z))
        for i in range(2,10000000) :
            z2 = multi((-1) ** (i - 1), power(i,neg(z)))
            z1 = add(z1,z2)
            z3 = multi((-1) ** i, power(int(i + 1),neg(z)))
            z4 = add(z1,z3)
            if mod(subt(z4,multi(0.0000999,z4))) <= mod(z1) <= mod(add(z4,multi(0.0000999,z4)))   :
                return z4
        return math.inf
    if Re(z) < 0 :
        z1 = multi(multi(power(math.pi, subt(z, 0.5)), div(gamma(div(subt(1, z), 2)), gamma(div(z,2)))), zeta(subt(1, z))) 
        return multi(z1,subt(1, power(2, subt(1, z))))

def F(z,n) :
    #fix
    #Calculates the Polylogarithm function
    z1 = div(z,power(1,n))
    for i in range(2,1000000) :
        z2 = div(power(z,i),power(i,n))
        z1 = add(z1,z2)
        z3 = div(power(z, Decimal(i + 1)), power(Decimal(i + 1),n))
        z4 = add(z1,z3)
        if mod(z1) > 10 ** 130 :
            return math.inf
        elif mod(subt(z4,multi(0.00000000999,z4))) <= mod(z1) <= mod(add(z4,multi(0.00000000999,z4)))   :
            return z4 
    return math.inf

def siegel(t) :
    #Calculates the Riemann siegel theta function
    z = (Decimal(0.25), Decimal(0.5 * t))
    z1 = Decimal(arg(gamma(z))) - 0.5 * t * Decimal(math.log(Decimal(math.pi)))
    return z1

def Z(t) :
    #Calculates the Riemann siegel function
    z = (0.5, t)
    z1 = multi(eul(1,siegel(t)), zeta(z))
    return z1

def B(n) :
    #calculates the bernoulli numbers
    z1 = multi(power(-1,add(n,1)),multi(n,zeta(subt(1,n))))
    return z1

def lamba(z) :
    if Im(z) == 0 and Re(z) == 1 :
        return math.nan
    else:
       z1 = multi(subt(1, power(2,neg(z))), zeta(z))
       return z1

def beta(z) :
    if Re(z) >= 1 :
        z1 = power(1,neg(z))
        for i in range(1,10000000) :
            z2 = multi((-1) ** (i), power(2*i + 1,neg(z)))
            z1 = add(z1,z2)
            z3 = multi((-1) ** (i + 1), power(2*(i + 1) + 1,neg(z)))
            z4 = add(z1,z3)
            if mod(subt(z4,multi(0.0000999,z4))) <= mod(z1) <= mod(add(z4,multi(0.0000999,z4)))   :
                return z4
        return math.inf
    else:
        z1 = div(beta(subt(1,z)),multi(multi(power(Decimal(2 / math.pi), z), sin(multi(math.pi /2, z))),gamma(z))) 

def lerch(z,s,a) :
    if mod(z) > 1 and not ((Re(a) % 1 == 0 and Re(a) <= 0) and Im(a) == 0) :
        z1 = power(a,neg(s))
        for i in range(1,1000000) :
            z2 = multi(power(z,i),power(add(a,i),neg(s)))
            z1 = add(z1,z2)
            z3 = multi(power(z,int(i + 1)),power(add(a,int(i + 1)),neg(s)))
            z4 = add(z1,z3)
            if mod(subt(z4,multi(0.00000000999,z4))) <= mod(z1) <= mod(add(z4,multi(0.00000000999,z4)))   :
                return z4 
        return math.inf

def totient(n) :
    counter = 0
    gcd = 1
    for i in range(1, n) :
        for j in range(1,n) :
            if i % j == 0 and n % j == 0 :
                gcd = j
        if gcd == 1 :
            counter += 1
    return counter

def totient_num(n) :
    counter = 0
    gcd = 1
    value = []
    for i in range(1, n) :
        for j in range(1,n) :
            if i % j == 0 and n % j == 0 :
                gcd = j
        if gcd == 1 :
            value.append(i)
    return value

def div_sig(k,n):
    z1 = 0
    for i in range(1,n + 1) :
        if n % i == 0 :
            z1 += i ** k
    return z1

def divisors(n):
    z1 = []
    for i in range(1,n + 1) :
        if n % i == 0 :
            z1.append(i)
    return z1

def is_prime(n) :
    z1 = (n * div_sig(1,n) - 2) % totient(n)
    if z1 == 0 and n != 4 and n != 6 and n != 22 :
        return 'true'
    else:
        return 'false'

def tau(n) :
    if n > 0 :
        z1 = 0
        for i in range(1, n) :
            z1 += div_sig(5,i) * div_sig(5, n - i)
        z2 = 65 * div_sig(11,n) / 756 + 691 * div_sig(5,n) / 756 - 691 * z1 / 3
        return z2

def N(p) :
    n = totient(p)
    z = []
    for p1 in range(2, n) :
        if is_prime(p1) == 'true' :
            z.append(p1)
    for g in range(2,100) :
        e = 0
        for j in z :
            q = n / j
            f = int(g ** q)
            if q % 1 == 0 and (f - 1) % p == 0 :
                e += 1
                break                       
        if e != 0 :
            continue
        else:
            return g

def X(k,j,n) :
    if j == 1 :
        return 1
    gen = N(j)
    X_n = []
    F = []
    z = totient_num(j)
    z.reverse()
    z = z[0:len(z)-1]
    z.insert(1,1)
    for i in z :
        z1 = power(eul(1,2 * math.pi / totient(j)),i)
        X_n.append(z1)
    for v in z:
        F.append(power(X_n[k-1],v))
    for w in range(1,n + 1) :
        if not w in z:
            F.insert(w - 1, 0)
    return F[n-1]
        
def L(k,s,X1) :
    z1 = X(k,X1,1)
    for i in range(2,10000000) :
        z2 = div(X(k,X1,i),power(i,s))
        z1 = add(z1,z2)
        z3 = div(X(k,X1,(i + 1)),power((i + 1),s))
        z4 = add(z1,z3)
        if mod(subt(z4,multi(0.00000000999,z4))) <= mod(z1) <= mod(add(z4,multi(0.00000000999,z4)))   :
            return z4
    return math.inf

def H_n(n) :
    #Calculates the Harmonic Series the nth term
    z1 = 0
    for i in range(1, n + 1) :
        z2 = 1 / i
        z1 = z1 + z2
    return z1
    
def polygamma(n) :
    #Calculates the polygamma function (Only real int)
    z1 = 1 - math.log(2)
    for i in range(2,1000000) :
        z2 = 1 / i - math.log(1 + (1 / i))
        z1 = z1 + z2
    z3 = H_n(n - 1) - z1
    return z3
    
euler_c = - polygamma(1)

def pi(n) :
    z1 = n / math.log(n)
    z2 = 1.25506 * n / math.log(n)
    z3 = (z1 + z2 ) / 2
    return z3
