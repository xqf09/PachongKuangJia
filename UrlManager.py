#coding:utf-8

#URL管理器

class UrlManager(object):


    #构造函数
    def __init__(self):
        #创建一个集合，存储没有被爬取的url
        self.new_urls=set()
        # 创建一个集合，存储已经被爬取的url
        self.old_urls = set()


    def has_new_url(self):
        '''
        判断是否有未被爬取的url
        :return: 返回一个布尔值，true表示有，false表示没有
        '''
        return self.new_urls_size()!=0


    def old_urls_size(self):
        '''
        返回已经被爬取的url的个数
        :return:

        '''
        return len(self.old_urls)

    def new_urls_size(self):
        '''
        返回未被爬取的url的个数
        :return:
        '''
        return len(self.new_urls)



    def get_new_url(self):
        '''
        获取一个未被爬取的url，并从未被爬取的集合中移除该url,且添加到已爬取的url集合
        :return:
        '''
        #获取一个未被爬取的url，并从未被爬取的集合中移除该url,pop()：取出并移除
        url=self.new_urls.pop()
        #添加到已爬取的url集合
        self.old_urls.add(url)
        return url



    def add_new_url(self,url):
        '''
        给未被爬取的url集合添加一个url
        :return:添加一个url
        '''
        if url is None:
            return
        #判断已被抓去和未被抓取的url中是否存在该url
        if url not in self.old_urls and url not in self.new_urls:
            self.new_urls.add(url)


    def add_new_urls(self,urls):
        '''
        给未被爬取的url集合添加多个url
        :return:返回
        :param urls :一个url集合
        '''
        if urls is None:
            return
        #调用add_new_url()函数
        for url in urls:
            self.add_new_url(url)