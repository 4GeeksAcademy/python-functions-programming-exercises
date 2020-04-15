import io, sys, pytest, os, re

@pytest.mark.it("Use the print function")
def test_output():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert content.find("print(") > 0

@pytest.mark.it('The printed value on the console should be "Hello World"')
def test_for_file_output(capsys, app):
    app()
    captured = capsys.readouterr()
    assert "Hello World\n" == captured.out