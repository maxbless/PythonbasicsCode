# 列表
shoplist = ['1', '2', '3', '4']
print('i have', len(shoplist), 'items to purchase')
print('these items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

shoplist.append('rice')
print('\nmy shoplist is now', shoplist)

shoplist.sort()
print('sorted shopping list is', shoplist)

print('the frist itme i will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('i bought the', olditem)
print('my shopping list is now', shoplist)
