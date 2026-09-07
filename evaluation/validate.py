from src.trajectory import simulate_abort
from src.core import g_load
traj=simulate_abort(0)
print(f"points {len(traj)} max_alt {max(p['alt'] for p in traj)}")
print("g", g_load(800,8000))
