import yaml
# from module import Site


with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)

# site = Site(testdata['address'])

def test_step1(email_input, password_input, submit, error, error_result, site):
    # x_selector1 = """//*[@id='login']/div[1]/label/input"""
    input1 = site.find_element('xpath', email_input)
    input1.send_keys('test')
    # x_selector2 = """//*[@id='login']/div[2]/label/input"""
    input2 = site.find_element('xpath', password_input)
    input2.send_keys('test')
    # btn_selector = 'button'
    btn = site.find_element('css', submit)
    btn.click()
    # x_selector3 = "//*[@id='app']/main/div/div/div[2]/h2"
    error_label = site.find_element('xpath', error)
    assert error_label.text == error_result

def test_step2(email_input, password_input, submit, login_result, site):
    input1 = site.find_element('xpath', email_input)
    input1.send_keys(testdata['username'])
    input2 = site.find_element('xpath', password_input)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', submit)
    btn.click()
    find_text = site.find_element('xpath', login_result).text
    assert f"Hello, {testdata['username']}" == find_text

def test_step3(email_input, password_input, submit, login_result, site, site2, site3):
    input1 = site.find_element('xpath', email_input)
    input1.send_keys(testdata['username'])
    input2 = site.find_element('xpath', password_input)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', submit)
    btn.click()
    btn2 = site.find_element('css', '#create-btn')
    btn2.click()
    input3 = site2.find_element('xpath', '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    input3.send_keys('some text in Title')
    input4 = site2.find_element('xpath', '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    input4.send_keys('some text in Description')
    input5 = site2.find_element('xpath', '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    input5.send_keys('some text in Content')
    btn3 = site2.find_element('css', '//*[@id="create-item"]/div/div/div[7]/div/button/div')
    btn3.click()
    find_text2 = site3.find_element('xpath', '''// * [ @ id="app"] / main / div / div / div[1] / div / div[3] / div[2] / div[1] / table / tbody / tr[1] / td[
        2]''')
    assert 'some text in Title' == find_text2







