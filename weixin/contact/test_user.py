import pytest
import allure

@allure.link('https://www.baidu.com')
def test1():
    assert True

def test2():
    assert False


