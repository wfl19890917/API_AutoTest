#读取多条测试用例
#1、导入requests模块
import  requests
from other.do_excel import read_data
from other.do_excel import write_data
from other.do_excel import count_case
from openpyxl.styles import Font
from openpyxl.styles.colors import RED
COOKIE=None
def http_request2(method,url,data):
    if  method=='get':
        print('发起一个get请求')
        result=requests.get(url,data,cookies=COOKIE)
    else:
        print('发起一个post请求')
        result=requests.post(url,data,cookies=COOKIE)
    return result   #返回响应体
   # return result.json()  resultxlsx果：结果是字典类型：{'status': 1, 'code': '10001', 'data': None, 'msg': '登录成功'}
#从Excel读取到多条测试数据
sheets=['getuser','getuser2','setmoney','setmoney2','uploadfile']
for sheet in sheets:
    max_row=count_case(sheet)
    print(max_row)
    for case_id in range(1,max_row):
        data=read_data(sheet,case_id)
        print('读取到第{}条测试用例:'.format(data[0]))
        print('测试数据 ',data)
        #print(type(data[2]))
        #调用函数发起http请求
        result=http_request2(data[3],data[4],data[5])
        print('响应结果为 ',result.json())
        if result.cookies:
                COOKIE=result.cookies
            #将测试实际结果写入excel
            #write_data(case_id+1,6,result['code'])
        #对比测试结果和期望结果
        resultxlsxult.json().get('code')==data[8]:
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
            