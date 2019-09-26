import pytest
import main

def test_File():
    uploadedFile = main.getFilename()
    assert uploadedFile == 'assignment.md'

def test_placeFail():
    uploadedFile = main.getFilefail()
    assert uploadedFile == 'assignment.md'
    