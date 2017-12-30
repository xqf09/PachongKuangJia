#coding:utf-8
from HtmlDownloader import htmlDownloader
from UrlManager import UrlManager
from HtmlParser import htmlParser
from HtmlSave import htmlSave


class manage(object):

    def __init__(self):
        #创建一个url管理器
        self.urlManager=UrlManager()
        #创建一个下载器
        self.htmlDownload=htmlDownloader()
        #创建一个解析器
        self.htmlParser=htmlParser()
        #创建一个存储器
        self.htmlSave=htmlSave()

    def action(self):
        '''
        启动爬虫
        :return:
        '''
        #给url管理器设置一个根url地址
        root_url="https://baike.baidu.com/item/网络爬虫"
        self.urlManager.add_new_url(root_url)
        #设置爬虫次数
        n=0

        #询问url管理器是否有代取的url
        while self.urlManager.has_new_url() and n<10:
            n+=1
            #调用url管理器,获取未被抓取的url
            new_url=self.urlManager.get_new_url()
            #把它交给下载器去下载html代码:htmlstr
            htmlstr=self.htmlDownload.download(new_url)
            #把htmlstr的内容和交给解析器，解析器返回一个元祖
            #元祖的第一个值是当前页面关联的url,是一个set集合
            #元祖的第二个值是当前页面的数据，是一个字典
            urls,data=self.htmlParser.parser(new_url,htmlstr)
            #把关联的urls交给url管理器
            self.urlManager.add_new_urls(urls)
            #把数据交给存储器
            self.htmlSave.saveData(data)
            print "第%s个页面数据"%n


        #当爬取结束后将数据输出到html文件（展示）
        self.htmlSave.outPut()



if __name__=="__main__":
    #创建一个调度器对象
    m=manage()
    m.action()

