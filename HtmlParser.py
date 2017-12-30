#coding:utf-8
#HTML解析器
from  bs4 import  BeautifulSoup
import re
import urlparse

class htmlParser(object):

    def parser(self,page_url,html):
        '''
        解析html
        :param page_url:要解析页面的url
        :param html:要解析页面代码
        :return:
        '''
        #若有一个没有传值，则返回，什么也不做
        if page_url is None or html is None:
            return
        soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
        #调用get_data解析当前页面所有数据
        datas=self.get_datas(page_url,soup)
        # 调用get_data解析当前页面关联的地址
        urls = self.get_urls(page_url, soup)

        return urls,datas

    def get_datas(self,page_url,soup):
        '''
        解析当前页需要的数据
        :param page_url:要解析页面的url
        :param html:要解析页面代码
        :return:
        '''
        try:
            #定义一个字典存储当前页数据
            datas={}
            datas['url']=page_url
            h1=soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find('h1')
            datas['title']=h1.string
            div=soup.find("div",class_="lemma-summary")
            #仅获取标签中的文本内容get_text()
            datas['msg']=div.get_text()
            print datas
            return datas
        except:
            pass
            #若有不存在class，会出错，以此避免中断

    def get_urls(self,page_url,soup):
        '''
        解析当前页关联url
        :param page_url:要解析页面的url
        :param html:要解析页面代码
        :return:
        '''
        #set集合存储新的url
        new_urls=set()
        a_s=soup.find_all("a",href=re.compile("/item/.+"))
        for a in a_s:
            href=a.attrs.get("href")
            full_url=urlparse.urljoin(page_url,href)
            new_urls.add(full_url)
            print full_url
        return new_urls