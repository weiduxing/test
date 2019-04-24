import allure
@allure.feature
class  Test_py:
    @allure.story('功能测试2')
    def test_demo1(self):
        a = 1
        b = 1
        assert a ==b

    @allure.story('功能测试2')
    def test_demo2(self):
        a = 2
        b = 2
        assert a != b