# 字典 keys values
goodman = {
    'xingming': 'laiyubin',
    'sex': 'man',
    'height': '169cm',
    'weight': '57kg',
    'info': 'it'
}

print('The goodman is ', goodman['xingming'])

# 删除一对键值-值配对
del goodman['info']
print(goodman)
# print('\n hahaha\n'.format(len(goodman)))

# 添加一对键值-值配对
goodman['aihao'] = 'basketball'
if 'aihao' in goodman:
    print('laiyubin love ', goodman['aihao'])

