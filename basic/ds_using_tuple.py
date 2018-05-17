'''元组：元组（Tuple） 用于将多个对象保存到一起。你可以将它们近似地看作列表，但是元组不能提
供列表类能够提供给你的广泛的功能。元组的一大特征类似于字符串，它们是不可变的，也
就是说，你不能编辑或更改元组。
'''
zoo = ('python', 'elephant', 'penguin')
print('number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))

print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo) - 1 +
      len(new_zoo[2]))
