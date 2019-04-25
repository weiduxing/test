from Common import Request, Assert, read_excel
import allure
# import pytest
request = Request.Request()
assertion = Assert.Assertions()
idsList=[]
excel_list = read_excel.read_excel_list('./document/test.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())
sku_id = {}
head = {}
url = 'http://192.168.1.137:8080/'
@allure.feature("商品模块")
class Test_sku:

    @allure.story("登录")
    def test_login(self):
        login_resp = request.post_request(url=url + 'admin/login',
                                          json={"username": "admin", "password": "123456"})
        resp_text = login_resp.text
        print(type(resp_text))
        resp_dict = login_resp.json()
        print(type(resp_dict))
        assertion.assert_code(login_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['message'], '成功')
        #
        data_dict = resp_dict['data']
        token = data_dict['token']
        tokenHead = data_dict['tokenHead']
        global head
        head = {'Authorization': tokenHead + token}

    @allure.story("获取商品分类")
    def test_get_sku(self):
        param = {'pageNum': '1','pageSize': '5'}
        get_sku_resp = request.get_request(url=url + 'productCategory/list/0', params=param, headers=head)
        resp_json = get_sku_resp.json()
        assertion.assert_code(get_sku_resp.status_code, 200)

        assertion.assert_in_text(resp_json['message'], '成功')

        json_data = resp_json['data']
        data_list = json_data['list']
        item = data_list[0]
        global sku_id
        sku_id = item['id']

    @allure.story("删除商品分类")
    def test_del_sku(self):
        del_sku_resp = request.post_request(url=url + 'productCategory/delete/' + str(sku_id), headers=head)
        resp_json = del_sku_resp.json()
        assertion.assert_code(del_sku_resp.status_code, 200)
        assertion.assert_in_text(resp_json['message'], '成功')
