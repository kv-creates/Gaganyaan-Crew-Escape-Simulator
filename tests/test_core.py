from src.core import abort_delta_v, g_load
def test_dv():
    assert abort_delta_v()>500
def test_g():
    assert g_load(800,8000)<15
