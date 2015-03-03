#answer8

#task a
dic = {'first':[2,1],'second':[2,3],'third': [3,4]}
temp = dic['first']
dic['first'] = dic['third']
dic['third'] = temp

#task b
dic['third'].sort()

#task c
dic['fourth'] = dic['second']

#task d
del dic['second']

#final result
print dic