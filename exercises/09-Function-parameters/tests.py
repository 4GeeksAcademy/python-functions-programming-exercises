import io, sys, pytest, os, re, mock

@pytest.mark.it("Declare de function render_person")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"def render_person\(.*\)\:")
        assert bool(regex.search(content)) == True


@pytest.mark.it('The function render_person must exist')
def test_for_functon_existence(capsys):
    from app import render_person

@pytest.mark.it('The function render_person must accept 5 parameters')
def test_for_file_output(capsys):
    from app import render_person
    render_person(1,2,3,4,5)

@pytest.mark.it('The function render_person must concatenate in the proper order, params don\'t follow the same order as the output')
def test_for_function_output(capsys):
    from app import render_person
    render_person('a','b','c',4,'d') == "a is a 4 years old d born in b with c eyes"