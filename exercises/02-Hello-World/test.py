import io, sys, pytest

@pytest.mark.it('3. The printed value on the console should be "red"')
def test_for_file_output(capsys, app):
    app.hello()
    captured = capsys.readouterr()
    assert "red!\n" == captured.out

@pytest.mark.it('1. You should create a variable named variables_are_cool')
def test_variable_exists(app):
    try:
        assert app.myVariable == "Helo"
    except ImportError:
        raise ImportError("The variable 'myVariable' should exist on app.py")
