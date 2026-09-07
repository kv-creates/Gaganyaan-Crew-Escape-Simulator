import math

def abort_delta_v(thrust_kn=800, mass_kg=8000, burn_s=8):
    return thrust_kn*1000*burn_s/mass_kg

def g_load(thrust_kn, mass_kg, drag_n=0):
    a=(thrust_kn*1000+drag_n)/mass_kg/9.81
    return round(a,2)

def abort_success(g, q_kpa):
    return g<8 and q_kpa<60
