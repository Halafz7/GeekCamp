#n=3
#print(2<n<5)

#data = [['a',10],['b',50],['c',31],['d',20]]
#
#print('data awal = ', data)
#print(sorted(data, key = lambda x:x[1])[-2])

#def fungsi(**kwargs):
#    print(*args)
#
#def fungsi_arg(a,b,c):
#    print(a,b,c)
#
#a=[0,2,4]
#fungsi_arg(a)

#d={} #1
#for _ in range(int(raw_input())): #2
#    Name=raw_input() #3
#    Grade=float(raw_input()) #4
#    d[Name]=Grade #5
#v=d.values()#6
#second=sorted(list(set(v)))[1] #7
#second_lowest=[] #8
#for key,value in d.items():  #9
#    if value==second: #10
#        second_lowest.append(key) #11
#second_lowest.sort() #12
#for name in second_lowest: #13
#    print(name) #14

#a,b,c = student_marks[query_name]
#print('%.2f'%((a+b+c)/3))

#from urllib import response
#import requests

#response=requests.get('https://www.greetingsapi.com/random')
#json_data = response.json()
#print(json_data)

#response=requests.post('https://jsonplaceholder.typicode.com/posts',
#    data={
#    'title': 'foo',
#    'body': 'bar',
#    'userId': 1,
#    }
#)
#
#print(response.text)

#assert = mengecek input benar/salah
x=5
#assert x>2, 'x lebih kecil dari 2'
if x>2:
    pass
else:
    raise AssertionError['x lebih kecil dari 2']
print(x)

