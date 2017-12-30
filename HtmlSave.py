#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import codecs
#编码转换模块

#存储器
class htmlSave(object):

    #定义一个构造函数
    def __init__(self):
        self.datas=[]


    #存储数据函数(或存储在数据库中)
    def saveData(self,dicData):
        if dicData is not None:
            self.datas.append(dicData)

    #将数据输出到文件(html文件)
    def outPut(self):
        f=codecs.open("baike.html","w",encoding="utf-8")
        f.write("<html>")
        f.write("<body>")
        f.write("<table border='1'>")
        f.write("<tr><td>标题</td><td>简介</td><td>链接</td></tr>")
        for data in self.datas:
            f.write("<tr>")
            f.write("<td width=100>%s</td>"%data["title"])
            f.write("<td width=500>%s</td>"%data["msg"])
            f.write("<td width=100>%s</td>"%data["url"])
            f.write("</tr>")
        f.write("</table>")
        f.write("</body>")
        f.write("</html>")