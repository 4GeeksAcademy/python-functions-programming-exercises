import io, sys, pytest, os, re, mock

@pytest.mark.it("Declare de function render_person")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"def render_person\(.*\)\:")
        assert bool(regex.search(content)) == True


@pytest.mark.it('The function render_person must exist')
def test_for_functon_existence(capsys, app):
    assert callable(app.render_person)

@pytest.mark.it('The function render_person must accept 5 parameters')
def test_for_file_output(capsys, app):
    assert app.render_person('ax','b','c','d','e') == "ax is a d years old e born in b with c eyes"
    