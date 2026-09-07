from fastapi import FastAPI
from .core import abort_delta_v, g_load
from .trajectory import simulate_abort
app=FastAPI(title="Gaganyaan")
@app.get("/health")
def h(): return {"status":"ok"}
@app.post("/abort")
def a(body: dict): return {"dv":abort_delta_v(),"traj":simulate_abort(body.get("alt",0))}
@app.get("/visual-data")
def v(): return simulate_abort(0)
