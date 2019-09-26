import pytest
import main

def test_login():
    username = main.getUsername()
    password = main.getPassword()
    assert username == 'admin' and password == 'password'

def test_loginFail():
    failUsername = main.getUserfail()
    failPassword = main.getPassfail()
    assert failUsername == 'admin' and failPassword == 'password'