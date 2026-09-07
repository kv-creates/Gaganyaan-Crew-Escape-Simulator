from src.thermal import heat_rate
def test_heat():
    assert heat_rate(500,0.5)>0
