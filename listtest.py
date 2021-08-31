

a = [{"a":1,"b":2},{"a":1,"c":13},{"a":1,"c":312},{"a":11,"c":31},{"a":21,"c":3}]
# for i in a:
    # if i['a'] == 1:
    #     print("yaya")
    #     i['a']=10
    # else:
    #     a.remove(i) 
    # if i['a'] != 1:
    #     a.remove(i) 
c = [] 
def func(s,c):
    s['a'] = s['a']*4
    c.append("qw")
    return s    
a = [func(i,c) for i in a if i['a']==1]
print(a)
print('\n')
print(c)

