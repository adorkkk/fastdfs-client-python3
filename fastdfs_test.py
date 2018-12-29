# -*- coding: utf-8 -*-
# @File  : fastdfs_test.py
# @Author: yz
# @Date  : 2018-12-29
# @Desc  :

from fdfs_client.client import *
import os
import configparser
import string

basepath = os.path.dirname(__file__)

if __name__ == '__main__':
    conf = os.path.join(basepath, './', 'client.conf')
    client = Fdfs_client('./client.conf')
    #ret = client.upload_by_filename('./index1.jpg')
    #ret =  client.delete_file('group1/M00/00/00/wKhLh1wbjR-APsnPAAaeK-lrzfQ9921.jpg')
    with open('./index1.jpg','rb') as f:
        buffer = f.read()
        ret = client.upload_appender_by_buffer(buffer,'jpg')

    print(ret)