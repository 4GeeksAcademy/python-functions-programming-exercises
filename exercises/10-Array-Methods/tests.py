import io, sys, pytest, os, re, mock

@pytest.mark.it("Declare the function sort_names")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"def sort_names\(.*\)\:")
        assert bool(regex.search(content)) == True


@pytest.mark.it('The function sort_names must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.sort_names)

@pytest.mark.it('The function sort_names must accept 1 parameter and return a sorted one')
def test_for_file_output(capsys):
    import app
    captured = capsys.readouterr()
    assert "['Bob', 'Dilan', 'John', 'Kenny', 'Tom']\n" == captured.out









