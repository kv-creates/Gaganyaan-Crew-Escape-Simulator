from src.trajectory import simulate_abort
def test_traj():
    assert len(simulate_abort(0))>5
