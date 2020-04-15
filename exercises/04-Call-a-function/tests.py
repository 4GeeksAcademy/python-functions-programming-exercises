import io, sys, pytest, os, re, mock

@pytest.mark.it("Create a function 'calculate_area'")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"def(\s*)calculate_area\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The function calculate_area must exist')
def test_for_callable(capsys, app):
    assert callable(app.calculate_area)

@pytest.mark.it('The function calculate_area must return an integer')
def test_for_integer(capsys, app):
    assert isinstance(app.calculate_area(3,4), int)

@pytest.mark.it('We tried the function sum with a=3 and b=4 and it did not return 7')
def test_for_return(capsys, app):
    assert app.calculate_area(3,4) == 12
    assert app.calculate_area(5,4) == 20

@pytest.mark.it('The variable square_area1 needs to be declared')
def test_for_existence1(capsys, app):
    app.square_area1
@pytest.mark.it('The variable square_area2 needs to be declared')
def test_for_existence2(capsys, app):
    app.square_area2
@pytest.mark.it('The variable square_area3 needs to be declared')
def test_for_existence3(capsys, app):
    app.square_area3

@pytest.mark.it('square_area1 needs to have as value the area of the first square')
def test_for_square_area_value1(capsys, app):
    assert app.square_area1 == 16

@pytest.mark.it('square_area2 needs to have as value the area of the second square')
def test_for_square_area_value2(capsys, app):
    assert app.square_area2 == 4

@pytest.mark.it('square_area3 needs to have as value the area of the third square')
def test_for_square_area_value3(capsys, app):
    assert app.square_area3 == 25

@pytest.mark.it("Create a function calculate_area must be called 3 times, one for each figure")
def test_call_calculate_area():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"=(\s*)calculate_area\(")
        assert bool(regex.search(content)) == True