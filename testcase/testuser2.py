from base.read_excel import read_data
from base.write_excel import write_data
from base.count_excel import count_case
from base.http_request import http_request
import unittest
class testUser2(unittest.TestCase):
    def test_user2(self):
        sheets=['getuser2']
        for sheet in sheets:
            max_row=count_case(sheet)
            print("\n{}".format(max_row))
            for case_id in range(1,max_row):
                data=read_data(sheet,case_id)
                print('读取到第{}条测试用例:'.format(data[0]))
                print('测试数据 ',data)
                #print(type(data[2]))
                #调用函数发起http请求
                result=http_request(data[3],data[4],data[5])
                print('响应结果为 ',result.json())
                if result.cookies:
                    COOKIE=result.cookies
            #将测试实际结果写入excel
            #write_data(case_id+1,6,result['code'])
            #对比测试结果和期望结果
                if result.json().get('code')==data[8]:
                    if result.json().get('msg')==data[7]:
                        print('测试通过')
                #将用例执行结果写入Excel
                        write_data(sheet,case_id+1,11,'Pass',False)
                        write_data(sheet,case_id+1,12,str(result.json()),False)
                    else:
                        print('测试失败')
                        write_data(sheet,case_id+1,11,'Fail',True)
                        write_data(sheet,case_id+1,12,str(result.json()),False)      
                else:
                    print('测试失败')
                    write_data(sheet,case_id+1,11,'Fail',True)
                    write_data(sheet,case_id+1,12,str(result.json()),False)
if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(testUser2('test_user2'))
    unittest.TextTestRunner(verbosity=2).run(suite)