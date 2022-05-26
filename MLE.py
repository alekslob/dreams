# import wavelets as wave
from numpy import mat
from wavelets import WAVE
import math

def func(theta, x):                                                     #   ВХОД: ТЕТЫ, x - равный размер
    return sum(theta[i]*xi for i, xi in zip(range(len(theta)), x))

def getEst(e, chm, N):
    # z = forZ(chm, e, N)
    z = 0.71
    wave = WAVE(chm, z, [min(e),max(e)])
    return wave.func(e, N)

def getCoef(i):
    k = int(math.log(i-1, 2))
    return 2**(-k/2)

def forZ(chm, t, N):
    if chm ==1 or chm == 2:
        n = len(t)
        # m = max([-min(t), max(t)])
        w = WAVE(chm, 1, [int(min(t)-.5),int(max(t)+.5)])
        return ((2-math.sqrt(2))*math.sqrt(math.pi)*sum(sum(getCoef(i)*w.psi(ti, i) for i in range(2, N+1, 1)) for ti in t)/n + w.psi(0,1))**(-1/2)
    # else: return 0

class MLE(object):
    def __init__(self, countMembers):
        self.N = countMembers

    # def algFTLN(self, theta,X, Y, x, y, chm):
    #     m = len(Y)
    #     N = self.N[chm] #int(ip.membersOfRow.get())
    #     n = len(y)
        
    #     wave = WAVE(chm, 0.71, [-4, 4])
    #     ft = (1/n)**m
    #     for s in range(m):
    #         B = 0
    #         for j in range(n):
    #             for i in range(1, N+1, 1):
    #                 # t2 = 0.01
    #                 t1 = Y[s] - func(theta, X[s])
    #                 t2 = y[j] - func(theta, x[j])
    #                 B += wave.psi(t1, i)*wave.psi(t2, i)
    #         ft *= B
    #     ft = math.log(abs(ft))
    #     return -ft
    

    def algFT(self, theta,X, Y, x, y, chm):
        m = len(Y)
        N = self.N[chm]
        n = len(y)
        t1 = [ Yi - func(theta, Xi) for Yi, Xi in zip(Y, X)]
        t2 = [ yi - func(theta, xi) for yi, xi in zip(y, x)]
        
        z = forZ(chm, t2, N)
        wave = WAVE(chm, z, [int(min(t2)-0.5), int(max(t2)+.5)])
        ft = -m*math.log(n)
        B = wave.func(t2, N)
        # ft += sum(math.log(abs(b)) for b in B)
        for s in range(m):
            B = 0
            for i in range(1, N+1, 1):               
                B += wave.psi(t1[s], i)*sum(wave.psi(t2i, i) for t2i in t2)
            ft += math.log(abs(B))
        # ft = math.log(abs(ft))
        # print(-ft, theta)
        return -ft

    # solve(a*x+b,x) поиск решения x

    # def algFTLNf(self, theta,X, Y, x, y, chm):
    #     m = len(Y)
    #     N = self.N[chm] #int(ip.membersOfRow.get())
    #     n = len(y)
    #     wave = WAVE(chm)
    #     ft = [0]*len(theta)
    #     for k in range(len(ft)):
    #         for s in range(m):
    #             B = 0
    #             A = 0
    #             for j in range(n):
    #                 for i in range(1, N+1, 1):
    #                     # t1 = 0.01
    #                     t1 = Y[s] - func(theta, X[s])
    #                     t2 = y[j] - func(theta, x[j])
    #                     psi1 = wave.psi(t1, i)
    #                     psi2 = wave.psi(t2, i)
    #                     B += psi1*psi2
    #                     A += wave.psiDef(X[s][k], t1, i)*psi1 + wave.psiDef(x[j][k], t2, i)*psi2
    #         ft[k] += A/B
    #     return ft   

