age = 18
name = 'TOM'
weight = 75.5
stu_id = 1

#我的名字是x,今年是x歲了
print('我的名字是%s,今年是%d歲了' %(name, age))
print('我的名字是%s,明年是%d歲了' %(name, age+1))

# f'{表達式}'
print(f'我的名字是{name},今年是{age}歲了')
print(f'我的名字是{name},明年是{age+1}歲了')

# 6.我的名字是x,今年是x歲了, 體重是x公斤,學號是x
print('我的名字是%s,今年是%d歲了, 體重是%.2f公斤,學號是%03d' %(name, age, weight, stu_id))
print(f'我的名字是{name},今年是{age}歲了, 體重是{weight}公斤,學號是{stu_id}')