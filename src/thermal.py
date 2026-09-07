import math

def heat_rate(v_mps, rho, nose_r=1.0):
    return 1.83e-4*math.sqrt(rho/nose_r)*v_mps**3/1e4

def tps_margin(q, limit=500):
    return round(limit-max(q),1)
