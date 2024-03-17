import pytest
from module import Site, Site2 , Site3
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def email_input():
    return "//*[@id='login']/div[1]/label/input"

@pytest.fixture()
def password_input():
    return "//*[@id='login']/div[2]/label/input"

@pytest.fixture()
def submit():
    return "button"

@pytest.fixture()
def error():
    return "//*[@id='app']/main/div/div/div[2]/h2"

@pytest.fixture()
def error_result():
    return "401"

@pytest.fixture()
def login_result():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'

@pytest.fixture()
def site():
    site_instance = Site(testdata['address'])
    yield site_instance
    site_instance.close()

@pytest.fixture()
def site2():
    site_instance = Site2(testdata['url'])
    yield site_instance
    site_instance.close()

@pytest.fixture()
def site3():
    site_instance = Site3(testdata['url2'])
    yield site_instance
    site_instance.close()



