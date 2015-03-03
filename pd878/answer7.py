#answer7

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = l1[:4]*4
l2.remove(l1[1])
l2.append(l1[2])
l2.sort()
print 'List =', l2


