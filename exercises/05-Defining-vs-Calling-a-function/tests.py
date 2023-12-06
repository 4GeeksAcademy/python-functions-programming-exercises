import io, sys, pytest, os, re, mock

@pytest.mark.it("Create the function 'multi'")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"def\s*multi\s*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The function multi must exist')
def test_for_callable(capsys, app):
    assert callable(app.multi)

@pytest.mark.it('The function multi must return a value')
def test_for_return_something(capsys, app):
    assert app.multi(1, 1) == True

@pytest.mark.it('The function multi must receive two numbers and return their multiplication')
def test_for_integer(capsys, app):
    assert app.multi(3,4) == 12

@pytest.mark.it('The function multi must receive two numbers and return their multiplication. Testing with different values')
def test_for_function_return(capsys, app):
    assert app.multi(10, 6) == 60
