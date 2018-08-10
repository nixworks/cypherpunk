from math import log1p, sqrt

def birthday(probability_exponent, bits):
    probability = 10.0**probability_exponent
    outputs = 2.0**bits
    return sqrt(2.0*outputs*-log1p(-probability))
