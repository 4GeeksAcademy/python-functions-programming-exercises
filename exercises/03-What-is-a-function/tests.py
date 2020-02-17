import io, sys, pytest, os, re, mock


@pytest.mark.it('The variable super_duper needs to be declared')
def test_for_existence(capsys, app):
    app.super_duper

@pytest.mark.it('The variable super_duper needs to have as value the result of the sum of the two numbers')
def test_for_file_output(capsys, app):
    assert app.super_duper == (3445324+53454423)