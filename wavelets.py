import math

class WAVE(object):
    def __init__(self, chm, z, cd):
        self.chm = chm
        self.z = z
        self.c = cd[0]
        self.d = cd[1]

    def func(self, e, N):
        # w = WAVE(2,z, [-4,4])
        n = len(e)
        width = self.d - self.c
        size = 100
        X = [self.c + i/(size)*width for i in range(size+1)]
        f = [0]*(size+1)
        # for s in range(size):
        #     for ei in e:
        #         f[s] += sum(self.psi(X[s], i)*self.psi(ei, i) for i in range(1, N+1))/n
        for s in range(size+1):
            for i in range(1, N+1):
                p1 = self.psi(X[s], i)
                f[s] += sum(self.psi(ej, i)*p1/n for ej in e)
        return f

    def getCoef(self, i):
        k = int(math.log(i-1, 2))
        return 2**(-k/2)

    def psi(self, t, i):
        if i == 1: return self.startPoint()
        else:    
            if self.chm == 2:
                return self.DOGWave(t, i)
    
    def startPoint(self):
        c = self.c
        d = self.d
        stp = math.sqrt(1/(d - c))
        if self.chm ==2:
            return stp*self.z#1.031/math.sqrt(2)

    def DOGWave(self, t, i):
        c = self.c
        d = self.d     
        k = int(math.log(i-1, 2))
        z = self.z
        # z = 1.031/math.sqrt(2)
        j = i - 2**k
        t = (t-c)/(d - c)
        t = pow(2,k)*t - (j-1)
        return z*(2**(k/2))*math.sqrt(1/(d - c))*((math.exp(-t*t/2)) - math.exp(-t*t/8)/2)
