import requests
import xlwt
import urllib
import re
import os

for x in range(1,6):
    url = 'http://qc.wa.news.cn/nodeart/list?nid=115511&pgnum=%d&cnt=20&tp=1&orderby=0?callback=jQuery171044987159007428024_1612089583768&_=1612089588909' % x

    heders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    response=requests.get(url,timeout=5,headers=heders)
    response.encoding='utf-8'
    print(response.text)

    title=re.findall(r'Title(.*?),',response.text)
    time=re.findall(r'PubTime(.*?),',response.text)
    Abstract=re.findall(r'Abstract(.*?),',response.text)
    imgarray=re.findall(r'imgarray(.*?)],',response.text)

    index_to_delete = [1, 2, 4,5,7,8,10,11,13,14,16,17,19,20,22,23,25,26,28,29,31,32,34,35,37,38,40,41,43,44,46,47,49,50,52,53,55,56,58,59]

    my_dict = {}
    for index, value in enumerate(title):
        my_dict[index] = value

    for index in index_to_delete:
        my_dict.pop(index)

    result = list(my_dict.values())
    # re0=re.replace("jQuery17106364644705821323_1612070653271({\"status\":0,\"data\":{\"list\":[{\"DocID\":1127041494,""","")
    #
    # print(html0)
    print(title[0])
    print(time[0])
    print(Abstract[0])
    print(imgarray[0])
    print(result[0])
    new_title={}
    new_time={}
    new_Abstract={}
    new_imgarray={}
    for index in range(len(result)):
        str=result[index]
        str=str.replace("\":","")
        str = str.replace("\"", "")
        new_title[index]=str
    for index in range(len(time)):
        str=time[index]
        str=str.replace("\":","")
        str = str.replace("\"", "")
        new_time[index]=str
    for index in range(len(Abstract)):
        str=Abstract[index]
        str=str.replace("\":","")
        str = str.replace("\"", "")
        new_Abstract[index]=str
    for index in range(len(imgarray)):
        str=imgarray[index]
        str=str.replace("\":","")
        str = str.replace("[", "")
        new_imgarray[index]=str
    print(new_title)
    print(new_time)
    print(new_Abstract)
    print(new_imgarray)
    print(new_imgarray[0])
    Workbook = xlwt.Workbook(encoding='utf-8')
    k=1
    worksheet = Workbook.add_sheet("news1")
    rowTitles = ['题目', '时间', '主体']
    keys=['title','time','content']
    for index,title in enumerate(rowTitles):
        worksheet.write(0, index, title)
    for i in range(len(new_title)):
        worksheet.write(k,0,new_title[i])
        worksheet.write(k,1,new_time[i])
        worksheet.write(k,2,new_Abstract[i])
        k+=1#每存储一行 k值加1
        Workbook.save('news%d.xls'%x)#写完后调用save方法进行保存
    i=0
    for index in range(len(imgarray)):
        test=new_imgarray[index]
        nist = test.split(",")  # [a,b,c]
        for index in range(len(nist)):
            nist[index]=nist[index].replace("\"","")
            print(nist[index])
            dirname = "test%d"%x
            if not os.path.exists(dirname):
                os.mkdir(dirname)
            try:
                urllib.request.urlretrieve(nist[0],'D:/PyCharmWrokPlace/pachong/test%d/%s.jpg'%(x,i))
            except ValueError:
                i = i + 1
                break
            i = i + 1
            break
                



