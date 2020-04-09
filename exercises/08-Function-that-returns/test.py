import io, sys, pytest, os, re, mock

@pytest.mark.it("Call the function dollar_to_euro passing the 137 dollars to get the amount in Euro")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"dollar_to_euro\(\s*\d+\s*\)")
        assert bool(regex.search(content)) == True


@pytest.mark.it("Call the function euro_to_yen passing the Euro converted amount to get the amount in Yen")
def test_euro_to_yen():
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"euro_to_yen\(")
        assert bool(regex.search(content)) == True


@pytest.mark.it('Print on the console the value of 137 dollars in yen')
def test_for_file_output(capsys):
    import app
    captured = capsys.readouterr()
    assert "15137.609500000002\n" == captured.out