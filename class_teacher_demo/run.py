__author__ = 'zz'
#encoding=UTF-8
from National_day_task.task_five.httprequest import HttpRequest
from National_day_task.task_five.readdata import ReadData
from National_day_task.task_five.savedata import SaveData

http_request_obj=HttpRequest("http://119.23.241.154:8080")#生成一个http请求实例

read_data_obj=ReadData("E:\\test_data.txt")
result=read_data_obj.read_data()#返回所有的测试数据，是列表格式

save_data_obj=SaveData("E:\\test_result.txt")#存储测试数据的对象

for i in range(len(result)):#根据列表的元素个数，一个一个的来读取。
    test_data=result[i].split(",")#对列表的每个元素进行拆分，拆分后又是列表格式
    url=test_data[0]
    mobile=test_data[1]
    amount=test_data[2]
    http_method=test_data[3].strip("\n")
    recharge_data={"mobilephone":mobile,"amount":amount}

    if http_method=="GET":
        request_result=http_request_obj.get(url,recharge_data)
    else:
        request_result=http_request_obj.post(url,recharge_data)

    save_data_obj.save_data(request_result)





