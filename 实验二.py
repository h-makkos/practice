#实验二1.用map函数
x=input('Please input:')
y=list(map(int,str(x)))
print(sum(y))


#实验二1.用while循环
x=int(input('Please input:'))
s=0
while True:
    s+=(x%10)
    x//=10
    if x==0:
        break
print(s)


#实验二2.并集、交集、差集
setA=eval(input('Please input setA:'))
setB=eval(input('Please input setB:'))
print(setA|setB,setA&setB,setA-setB)


#实验二3.输出二进制、八进制、十六进制
x=int(input('Please input a number:'))
print(bin(x),oct(x),hex(x))
