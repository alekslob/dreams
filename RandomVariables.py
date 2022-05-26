import random as rnd

class RandomVariables(object):
    def __init__(self,
                nPoint,
                parametrs):
        self.nPoint = nPoint
        self.expectation = parametrs[0]
        self.variance = parametrs[1]
        self.lambd = parametrs[2]
        self.k = parametrs[3]
        self.alf = parametrs[4]

        # self.normal = self.normalRandom()
        # self.exponential = self.exponentialRandom()
        # self.gamma = self.gammaRandom()
        # self.beta = self.betaRandom()

    def getFunction(self, chooseDistribution):
        if chooseDistribution == 0:
            return self.normal()
        elif chooseDistribution == 1:
            return self.exponential()
        elif chooseDistribution == 2:
            return self.gamma()
        elif chooseDistribution == 3:
            return self.gamma()

    def normal(self):
        return [rnd.normalvariate(self.expectation,self.variance) for i in range(self.nPoint + 1)]

    def exponential(self):
        return sorted([rnd.expovariate(self.lambd) for i in range(self.nPoint + 1)])
    
    # todo: разобраться с k и alf
    def gamma(self):
        return sorted([rnd.gammavariate(self.k, self.alf) for i in range(self.nPoint + 1)])

    def beta(self):
        return sorted([rnd.betavariate(2,2) for i in range(self.nPoint + 1)])