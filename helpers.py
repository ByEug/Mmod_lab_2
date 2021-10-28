import math


def get_free_probability(p, n, m, beta):
    p0 = 1

    for k in range(1, n + 1):
        p0 += p ** k / math.factorial(k)

    sum = 0
    i = 1
    while i <= m:
        p_up = p ** i
        l = 1
        compos = 1
        while l <= i:
            compos *= (n + l * beta)
            l += 1
        sum += p_up / compos
        i += 1

    p0 += ((p ** n) / math.factorial(n)) * sum
    return 1 / p0


def get_pn_probability(p, n, m, beta):
    p0 = get_free_probability(p, n, m, beta)
    return p0 * (p ** n) / math.factorial(n)


def get_state_probs(rho, n, m, beta):
    p0 = get_free_probability(rho, n, m, beta)
    probs = [p0]

    for k in range(1, n + 1):
        probs.append(rho ** k / math.factorial(k) * p0)

    pn = get_pn_probability(rho, n, m, beta)
    for i in range(1, m + 1):
        l = 1
        compos = 1
        while l <= i:
            compos *= (n + l * beta)
            l += 1
        probs.append(pn * (rho ** i) / compos)

    return probs


def get_cancel_prob(p, n, m, beta):
    pn = get_pn_probability(p, n, m, beta)
    l = 1
    denominator = 1
    while l <= m:
        denominator *= (n + l * beta)
        l += 1
    return pn * (p ** m) / denominator


def get_theor_interval_len(n, m, probs):
    sum = 0
    for i in range(0, m):
        sum += ((i + 1) * probs[n + 1 + i])
    return sum


def get_theor_channel_loaded(n, m, probs):
    sum = 0

    for k in range(0, n):
        sum += probs[k + 1] * (k + 1)

    for i in range(0, m):
        sum += n * probs[n + i + 1]

    return sum


def get_overall_request_time(theor_relative_bandwidth, mu, t):
    return theor_relative_bandwidth / mu + t
