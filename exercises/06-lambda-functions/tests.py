import io, sys, pytest, os, re, mock

@pytest.mark.it("Declar a function 'is_odd' as lambda")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"is_odd(\s*)=(\s*)lambda\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The function is_odd must exist')
def test_for_callable(capsys, app):
    assert callable(app.is_odd)

@pytest.mark.it('The function is_odd must receive one numbers and return true is odd or false otherwise')
def test_for_integer(capsys, app):
    assert app.is_odd(3) == True
    assert app.is_odd(2) == False