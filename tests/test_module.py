from mypackage import mymodule

def test_hello():
    mymodule.hello(None)
    assert 1 == mymodule.one()
