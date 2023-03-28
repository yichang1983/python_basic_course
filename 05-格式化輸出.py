age = 18
name = 'TOM'
weight = 75.5
stu_id = 1
stu_id2 = 1000

# 1. 今年我的年齡是x歲 -- 整數 %d
print('今年我的年齡是%d歲'% age)

# 2.我的名字是x  -- 字串 %s
print('我的名字是%s' % name)

# 3.我的體重是x公斤 -- 浮點數 %f
print('我的體重是%.2f公斤' % weight)

# 4.我的學號是x -- %d
print('我的學號是%d' %stu_id)

# 4.1 我的學號是001
print('我的學號是%03d' %stu_id)
print('我的學號是%03d' %stu_id2)

# 5.我的名字是x,今年是x歲了
print('我的名字是%s,今年是%d歲了' %(name, age))
print('我的名字是%s,明年是%d歲了' %(name, age+1))

# 6.我的名字是x,今年是x歲了, 體重是x公斤,學號是x
print('我的名字是%s,今年是%d歲了, 體重是%.2f公斤,學號是%03d' %(name, age, weight, stu_id))