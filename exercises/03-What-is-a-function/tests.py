import io, sys, pytest, os, re, mock


@pytest.mark.it("Create a function 'sum'")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"def(\s*)sum\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The function sum must exist')
def test_for_callable(capsys, app):
    assert callable(app.sum)

@pytest.mark.it('The function sum must return an integer (the sum of a+b)')
def test_for_integer(capsys, app):
    assert isinstance(app.sum(3,4), int)

@pytest.mark.it('We tried the function sum with a=3 and b=4 and it did not return 7')
def test_for_return(capsys, app):
    assert app.sum(3,4) == 7

@pytest.mark.it('The variable super_duper needs to be declared')
def test_for_existence(capsys, app):
    app.super_duper

@pytest.mark.it('The variable super_duper needs to have as value the result of the sum of the two numbers')
def test_for_file_output(capsys, app):
    assert app.super_duper == (3445324+53454423)