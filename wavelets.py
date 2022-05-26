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

    def psi(self, t, i):
        
        
        if i == 1: return self.startPoint()
        else:    
            if self.chm == 0:
                return self.MorleWave(t, i)
            elif self.chm == 1:
                return self.MHWave(t, i)    
            elif self.chm == 2:
                return self.DOGWave(t, i)
            elif self.chm == 3:
                return self.LPWave(t, i)
            elif self.chm == 4:
                return self.FurieWave(t, i)
    
    
    def startPoint(self):
        c = self.c
        d = self.d
        stp = math.sqrt(1/(d - c))
        if self.chm == 0:
            return stp*math.sqrt(2/math.sqrt(math.pi))
        elif self.chm ==1:
            return stp*1.031/math.sqrt(2)
        elif self.chm ==2:
            return stp*1.031/math.sqrt(2)
        elif self.chm ==3:
            return stp
        elif self.chm ==4:
            return stp


    def MHWave(self, t,i):
        c = self.c
        d = self.d
        k = int(math.log(i-1, 2))
        # z = self.z#pow(*(2**(k/2))*(2-math.sqrt(2))*math.sqrt(math.pi), -1/2)
        z = 1.031/math.sqrt(2)
        j = i - 2**k
        t = (t-c)/(d-c)
        t = pow(2,k)*t - (j-1)
        return z*(2**(k/2))*math.sqrt(1/(d - c))*(1 - 2*t**2)*math.exp(-t**2)

    def MorleWave(self, t, i):
        c = self.c
        d = self.d
        z = math.sqrt(2)/pow(math.pi, 1/4)
        k = int(math.log(i-1, 2))
        j = i - 2**k
        t = t/(d - c)
        t = pow(2,k)*t - (j-1)
        return z*(2**(k/2))*math.sqrt(1/(d - c))*math.exp(-t*t/2)*math.cos(5*t)
    
    
    def DOGWave(self, t, i):
        c = self.c
        d = self.d
        pi = math.pi
        k = int(math.log(i-1, 2))
        # z =self.z
        z = 1.031/math.sqrt(2)
        j = i - 2**k
        t = (t-c)/(d - c)
        t = pow(2,k)*t - (j-1)
        return z*(2**(k/2))*math.sqrt(1/(d - c))*((math.exp(-t*t/2)) - math.exp(-t*t/8)/2)

    def LPWave(self, t, i):
        c = self.c
        d = self.d
        pi = math.pi
        k = int(math.log(i-1, 2))
        j = i - 2**k
        t = t/(d - c)
        t = pow(2,k)*t - (j-1)
        if abs(t) < 1e-4: 
            t = 1e-4
        return (2**(k/2))*math.sqrt(1/(d - c))*((math.sin(2*pi*t) - math.sin(pi*t))/(pi*t))

    def FurieWave(self, t, i):
        c = self.c
        d = self.d
        pi = math.pi
        k = int(math.log(i-1, 2))
        j = i - 2**k
        # t = (t-c)/(d - c)
        # t = pow(2,k)*t - (j-1)
        
        if (i % 2) == 0:
            return math.sqrt(2/(d - c))*math.sin(pi*i/2*(t*2/(d - c) + (d + c)/(d - c)))
        else:
            return math.sqrt(2/(d - c))*math.cos(pi*(i - 1)/2*(t*2/(d - c) + (d + c)/(d - c)))
    

    