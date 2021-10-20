from auto.libs import spider_and_publish

if __name__ == '__main__':
    '''
    参数配置
    :parameter platform: 平台
    :parameter type: 类型 @spider.const.WEIBO_TYPE
    :parameter page: 共爬取页码
    '''
    params = {
        "platform": "weibo",
        "type": 1,
        "page": 5
    }
    spider_and_publish(**params)
