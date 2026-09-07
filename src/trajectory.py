import math

def simulate_abort(alt0=0, v0=0, dt=0.5, steps=40):
    alt=alt0; v=v0; traj=[]
    for i in range(steps):
        v+= (800*1000/8000-9.81)*dt*0.3
        alt+= v*dt
        q=0.5*1.225*max(0,1-alt/50000)*v*v/1000
        traj.append({"t":round(i*dt,1),"alt":round(alt,1),"vel":round(v,1),"q":round(q,2)})
        if alt>15000:
            break
    return traj
