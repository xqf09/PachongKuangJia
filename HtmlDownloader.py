#coding:utf-8
import requests
#HTML下载器

class htmlDownloader(object):

    def download(self,url):
        '''
        通过url地址下载数据并返回
        :param url:要爬取的url地址
        :return:
        '''
        if url is None:
            return
        user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'
        header={"User-Agent":user_agent}
        response=requests.get(url,headers=header)
        response.encoding='utf-8'
        return response.text

