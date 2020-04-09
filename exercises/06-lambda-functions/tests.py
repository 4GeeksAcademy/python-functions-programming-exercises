import io, sys, pytest, os, re, mock

@pytest.mark.it("Declare a function 'is_odd' as lambda")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"is_odd(\s*)=(\s*)lambda")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The function is_odd must exist')
def test_for_callable(capsys):
    import app as app
    assert callable(app.is_odd)

@pytest.mark.it('The function is_odd must receive one number and return true if is odd or false otherwise')
def test_for_integer(capsys):
    import app as app
    assert app.is_odd(3) == True

@pytest.mark.it('We tested the function with 2 and the result was not False')
def test_for_integer2(capsys):
    import app as app
    assert app.is_odd(2) == False