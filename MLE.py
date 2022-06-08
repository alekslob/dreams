# import wavelets as wave
from numpy import mat
from wavelets import WAVE
import math

def func(theta, x):                                                     #   ВХОД: ТЕТЫ, x - равный размер
    return sum(theta[i]*xi for i, xi in zip(range(len(theta)), x))

def getEst(e, chm, N):
    z = forZ(chm, e, N)
    # z = 0.71
    wave = WAVE(chm, z, [min(e),max(e)])
    return wave.func(e, N)

def forZ(chm, t, N):
    if chm == 2:
        n = len(t)
        c = math.ceil(min(t)-1)
        d = math.ceil(max(t))
        t = [(ti-c)/(d-c) for ti in t]
        w = WAVE(chm, 1, [math.ceil(min(t)-1), math.ceil(max(t))])
        koef = (2-math.sqrt(2))*math.sqrt(math.pi)
        # return 1/math.sqrt(sum(sum(w.psi(ti, i)/w.getCoef(i) for i in range(2, N+1, 1))*koef + 1 for ti in t)/n)
        return pow(sum(sum(w.psi(ti, i)/w.getCoef(i) for i in range(2, N+1, 1))*koef + 1 for ti in t)/n, -1/2)
    else: return 0


class MLE(object):
    def __init__(self, countMembers):
        self.N = countMembers

    def algFT(self, theta,X, Y, x, y, chm):
        N = self.N[chm]
        n = len(y)
        m = len(Y)#100
        t1 = [ Yi - func(theta, Xi) for Yi, Xi in zip(Y, X)]
        t2 = [ yi - func(theta, xi) for yi, xi in zip(y, x)]
        # c = math.ceil(min(t2)-1)
        # d = math.ceil(max(t2))
        # t1 = [c + i/(m)*(d - c) for i in range(m+1)]

        z = forZ(chm, t2, N)
        # z = 1
        wave = WAVE(chm, z, [math.ceil(min(t2)-1), math.ceil(max(t2))])

        ft = -m*math.log(n)
        for s in range(m):
            B = 0
            for i in range(1, N+1, 1):               
                B += wave.psi(t1[s], i)*sum(wave.psi(t2i, i) for t2i in t2)
            ft += math.log(abs(B))
        return -ft