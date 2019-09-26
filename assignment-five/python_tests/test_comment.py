import pytest
import main

def test_File():
    commentReady = main.getAssignmentStatus()
    assert commentReady == 'Graded'

def test_placeFail():
    commentReadyFail = main.getAssignmentStatusFail()
    assert commentReadyFail == 'Graded'