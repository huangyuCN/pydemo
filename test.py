import os

print "OS:",os.uname()

Names = ['adam', 'LISA', 'barT']


def nameck(Nm):
    Lnm = Nm.lower()
    Fst = Lnm[0]
    print 'Fst:', Fst, Fst.upper()
    return Fst.upper() + Lnm[1:]


print map(nameck, Names)


def prod(X):
    print 'X:', X

    def mutiadd(Y, Z):
        return Y * Z

    return reduce(mutiadd, X)


print prod([1, 2, 3])


def mutiadd(Y, Z):
    return Y * Z


print reduce(mutiadd, [1, 2, 3])


def ger(Y):
    if Y == 1:
        yield Y
    else:
        N = 0
        while Y - N > 0:
            yield Y - N
            N = N + 1


for x in ger(3):
    print 'x:', x


def su(N):
    def gerner(Y):
        if Y == 1:
            yield Y
        else:
            i = 0
            while Y - i >= 0:
                yield Y - i
                i = i + 1

    Ans = True
    for X in gerner(N):
        print 'X:', X
        if X > 1 and X < N and N % X == 0:
            return False
        else:
            Ans and True
    return Ans


print filter(su, [1, 2, 3, 4, 5])

print os.listdir('.')

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']