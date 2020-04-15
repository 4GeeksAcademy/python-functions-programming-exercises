import io, sys, pytest, os, re, mock

@pytest.mark.it("Create a function 'multi'")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"def(\s*)multi\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The function multi must exist')
def test_for_callable(capsys, app):
    assert callable(app.multi)

@pytest.mark.it('The function multi must receive two numbers and return their multiplication')
def test_for_integer(capsys, app):
    assert app.multi(3,4) == 12