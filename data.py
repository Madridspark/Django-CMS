# -*- coding: utf-8 -*-
# @Date    : 2015-07-28 20:38:38
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
'''
create some records for demo database
'''
 
from winter.wsgi import *
from branch.models import Column, Article, FriendlyLink
 
 
def main():
    
    columns = Column.objects.all()
 
    for column in columns:
        # 创建 10 篇新闻
        for i in range(11, 101):
            article = Article.objects.get_or_create(
                title='{}_{}'.format(column.name, i),
                content='新闻详细内容： {} {}'.format(column.name, i)
            )[0]
 
            article.column.add(column)
 
 
if __name__ == '__main__':
    main()
    print("Done!")