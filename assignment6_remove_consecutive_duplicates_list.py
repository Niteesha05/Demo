from itertools import groupby
test_list=[1,2,6,9,7,6,6,8,8,9,9,9,4]
print('the original list is :'+str(test_list))
res=[i[0] for i in groupby(test_list)]
print("the list after removing consecutives duplicates:"+str(res))
