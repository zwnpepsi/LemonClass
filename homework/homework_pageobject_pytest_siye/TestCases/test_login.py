# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# @Time    : 2017/12/3 14:37
# @Author  : SiYe
# @PROJECT_NAME    : LemonClass
# @File    : test_login.py
# @Software: PyCharm
#-------------------------------------------------------------------------------


#测试登录功能
class TestLogin():

    #测试登录成功功能
    @pytest.mark.usefixtures("init_testlogin_driver")
    @pytest.mark.smoke
    def test_login_ok(self,init_testlogin_driver):
        try:
            init_testlogin_driver[1].login(web_url, login_username_ok,login_password_ok)
            #验证
            homepage=HomePage(init_testlogin_driver[0])
            nickname=homepage.get_nickname()
            assert check_nickname in nickname
        except AssertionError as e:
            img_name = "test_login_ok_error.png"
            init_testlogin_driver[0].save_screenshot(image_path + "/" + img_name)
            print('登录测试不通过！异常原因是：%s' % e)
            raise e

    #测试不输入密码进行登录操作
    @pytest.mark.usefixtures("init_testlogin_driver")
    @pytest.mark.smoke
    def test_login_noPassword(self,init_testlogin_driver):
        try:
            init_testlogin_driver[1].login(web_url,login_username_ok,"")
            #验证
            password_info = init_testlogin_driver[1].get_password_info()
            assert check_noPassword_Info in password_info
        except AssertionError as e:
            img_name = "test_login_noPassword_error.png"
            init_testlogin_driver[0].save_screenshot(image_path + "/" + img_name)
            print('登录测试不通过！异常原因是：%s' % e)
            raise e

    #测试不输入用户名进行登录操作
    @pytest.mark.usefixtures("init_testlogin_driver")
    @pytest.mark.smoke
    def test_login_noUsername(self,init_testlogin_driver):
        try:
            init_testlogin_driver[1].login(web_url,"",login_password_ok)
            #验证
            username_info = init_testlogin_driver[1].get_username_info()
            assert check_noUsername_Info in username_info
        except AssertionError as e:
            img_name = "test_login_noUsername_error.png"
            init_testlogin_driver[0].save_screenshot(image_path + "/" + img_name)
            print('登录测试不通过！异常原因是：%s' % e)
            raise e

    #测试输入非法的用户名进行登录操作
    @pytest.mark.usefixtures("init_testlogin_driver")
    @pytest.mark.smoke
    def test_login_incorrectUsername(self,init_testlogin_driver):
        try:
            init_testlogin_driver[1].login(web_url,login_username_wrong,login_password_ok)
            #验证
            error_info = init_testlogin_driver[1].get_error_info()
            assert check_wrongUsername_Info in error_info
        except AssertionError as e:
            img_name = "test_login_incorrectUsername_error.png"
            init_testlogin_driver[0].save_screenshot(image_path + "/" + img_name)
            print('登录测试不通过！异常原因是：%s' % e)
            raise e

    #测试输入非法的密码进行登录操作
    @pytest.mark.usefixtures("init_testlogin_driver")
    @pytest.mark.smoke
    def test_login_incorrectPassword(self,init_testlogin_driver):
        try:
            init_testlogin_driver[1].login(web_url,login_username_ok,login_password_wrong)
            #验证
            error_info = init_testlogin_driver[1].get_error_info()
            assert check_wrongPassword_Info in error_info
        except AssertionError as e:
            img_name = "test_login_incorrectPassword_error.png"
            init_testlogin_driver[0].save_screenshot(image_path + "/" + img_name)
            print('登录测试不通过！异常原因是：%s' % e)
            raise e

# if __name__ =='__main__':
#     # suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin)
#     # unittest.TextTestRunner().run(suite)


