import pytest
import main

def test_instructAdd():
    occupationTitle = main.getOccup()
    assert occupationTitle == 'Instructor'

def test_instructAddFail():
    occupationTitleFail = main.getOccupFail()
    assert occupationTitleFail == 'Instructor'