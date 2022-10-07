import numpy as np
import random
import math

# parameters
m = 100000
n = 100
r = 1000
mu = 0.0
sigma = 0.2
trust = 0.95
k = 6

def create_array(m, n):
	# candidates = np.random.randint(m, size = n)
	candidates = random.sample(range(1, m), n)
	return candidates

def OPT(candidates, n):
	return max(candidates)

def classical(candidates, n):
	stopping = math.floor(n / math.e)
	candidates_sample = candidates[1 : stopping]
	highest_sample = max(candidates_sample)
	for i in range(stopping + 1, n):
		if (candidates[i] > highest_sample):
			return candidates[i]
	return 0

def accurate_predictor(candidates, n, trust):
    candidates_maxremoved = candidates.copy()
    candidates_maxremoved.remove(max(candidates_maxremoved))
    p = max(candidates_maxremoved)
    for i in candidates:
        if (i > p * trust):
            return i
    return 0

def erroneous_predictor(candidates, n, mu, sigma, trust):
    candidates_maxremoved = candidates.copy()
    candidates_maxremoved.remove(max(candidates_maxremoved))
    p = max(candidates_maxremoved)
    stddev = np.random.normal(mu, sigma, 1)[0]
    print(stddev)
    p = math.floor(p + p * stddev)
    # print(p)
    for i in candidates:
        if (i > p * trust):
            return i
    return 0

def KOPT(candidates, n, k):
    candidates_maxremoved = candidates.copy()
    sum = 0
    for i in range(k):
        sum = sum + max(candidates_maxremoved)
        candidates_maxremoved.remove(max(candidates_maxremoved))
    return sum

def Kclassical(candidates, n, k):
    stopping = np.random.binomial(n = n, p = 0.5, size  = 1)[0]
    sum = 0
    k1 = math.floor(k / 2) - 1
    candidates_sample = candidates.copy()
    candidates_sample = candidates_sample[1 : stopping]
    for i in range(k1):
        candidates_sample.remove(max(candidates_sample))
    highest_sample = max(candidates_sample)
    # print(stopping, highest_sample)
    for i in range(stopping + 1, n):
        if (candidates[i] > highest_sample and k > 0):
            sum = sum + candidates[i]
            k = k - 1
    return sum

def Kaccurate_predictor(candidates, n, k, trust):
    candidates_maxremoved = candidates.copy()
    for i in range(k):
        candidates_maxremoved.remove(max(candidates_maxremoved))
    p = max(candidates_maxremoved)
    sum = 0
    for i in candidates:
        if (i > p * trust and k > 0):
            sum = sum + i
            k = k - 1
    return sum

def Kerroneous_predictor(candidates, n, k, mu, sigma, trust):
    candidates_maxremoved = candidates.copy()
    for i in range(k):
        candidates_maxremoved.remove(max(candidates_maxremoved))
    p = max(candidates_maxremoved)
    stddev = np.random.normal(mu, sigma, 1)[0]
    print(stddev)
    p = math.floor(p + p * stddev)
    sum = 0
    for i in candidates:
        if (i > p * trust and k > 0):
            sum = sum + i
            k = k - 1
    return sum

def run_experiment(m, n, mu, sigma, trust):
    candidates = create_array(m, n)
    opt = OPT(candidates, n)
    alg1 = classical(candidates, n)
    alg2 = accurate_predictor(candidates, n, trust)
    alg3 = erroneous_predictor(candidates, n, mu, sigma, trust)
    
    Kopt = KOPT(candidates, n, k)
    Kalg1 = Kclassical(candidates, n, k)
    Kalg2 = Kaccurate_predictor(candidates, n, k, trust)
    Kalg3 = Kerroneous_predictor(candidates, n, k, mu, sigma, trust)
    print(np.argmax(candidates), opt, alg1, alg2, alg3,
        alg1 / opt, alg2 / opt, alg3 / opt,
        Kalg1 / Kopt, Kalg2 / Kopt, Kalg3 / Kopt)
    return alg1 / opt, alg2 / opt, alg3 / opt, Kalg1 / Kopt, Kalg2 / Kopt, Kalg3 / Kopt

cr1, cr2, cr3, cr4, cr5, cr6 = 0, 0, 0, 0, 0, 0
for i in range(r):
    a, b, c, d, e, f = run_experiment(m, n, mu, sigma, trust)
    cr1 = cr1 + a
    cr2 = cr2 + b
    cr3 = cr3 + c
    cr4 = cr4 + d
    cr5 = cr5 + e
    cr6 = cr6 + f
print(cr1 / r, cr2 / r, cr3 / r, cr4 / r, cr5 / r, cr6 / r)

