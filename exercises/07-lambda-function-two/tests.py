import io, sys, pytest, os, re, mock

@pytest.mark.it("Declare a function 'rapid' as lambda")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"rapid(\s*)=(\s*)lambda")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The function rapid must exist')
def test_for_callable(capsys):
    from app import rapid

@pytest.mark.it('The function rapid must receive one string and return the same but without the last letter and uppercase')
def test_for_integer(capsys):
    from app import rapid
    assert rapid("maria") == "mari"
    assert rapid("pepe") == "pep"