import numpy as np

class FourCal:
    # def __init__(self):
    #     self.first = 0
    #     self.second = 0
    #     self.result = 0
    def __init__(self, a = 0, b = 0):
        self.first = a
        self.second = b
        self.result = 0
    def setdata(self, a, b):
        self.first = a
        self.second = b
    def add(self):
        self.result = self.first + self.second
        return self.result
    def sub(self):
        self.result = self.first - self.second
        return self.result
    def mul(self):
        self.result = self.first * self.second
        return self.result
    def div(self):
        self.result = self.first / self.second
        return self.result

class MoreFourCal(FourCal):
     def pow(self):
         self.result = self.first ** self.second
         return self.result
class SafeFourCal(FourCal):
    def div(self):    #함수 오버라이딩 : 부모클래스에 있는 함수를 재정의해서 사용  
        if self.secon == 0:
            return 0
        else:
            return self.first/self.second

c = MoreFourCal(4, 2)
print(c.pow())

a = FourCal(4, 0)
print('{:.2f}'.format(a.div()))

# a = FourCal()
# b = FourCal(4, 6)
# a.setdata(200, 35)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print('{:.2f}'.format(a.div()))

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self,num):
        self.result -= num
        return self.result

    def mul(self,num):
        self.result *= num
        return self.result  

    def div(self,num):
        self.result /= num
        return self.result


# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.sub(2))
# print(cal1.mul(7))
# print(cal1.div(2))
#11번
# a = b = [1, 2, 3]
# a[1] = 4
# print(b)
#얕은 복사 

#10번
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# print(set(a))

#9번
# a = {'A':90, 'B':80, 'C':70}
# print(a.pop('B'))

#8번


#7번
#a = (1, 2, 3)
#b = a + (4,)
#print(b)

#6번
# str1 = ['Life', 'is', 'too', 'short']
# str2 = [str1[0] + " " + str1[1]+ " " +str1[2]+ " "+str1[3]]
# print(str2)

#5번
# num = [1, 3, 5, 4, 2]
# num.sort()
# num.reverse()
# print(num)

#4번
# a = "a:b:c:d".replace(':','#')
# print(a)

#3번
# pin = "881120-1068234"
# x = (pin[7:8])
# if(x == '1'):
#     print('남자')
# if(x == '2'):
#     print('여자')

#2번
# x = '881120-1068234'
# print(x[:6])  #생년월일
# print(x[7:14]) # 뒷자리 


#1번
# num = 13 
# if num % 2 == 0:
#     print('짝')
# else:
#     print('홀')


# num = [2, 4, 6, 8, 10]
# x = np.array(num)

# print(num*3)
# print(x*3)

# x = np.array([[4, 4, 4], [8, 8, 8]])
# print(x + 10)


# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# t3 = [7, 8, 9]

# y = t1 + t2
# print(y)

# print(len(t1))

# x = 11
# if x > 10: 
#     print(' x is ' ) # ... (A1)print('          larger than 10.') # ... (A2)else 
#     print('x is smaller than 11') # ... (B1)
# else:
#     print('y is')

# x = (1, 2, 3)

# y = list(x[0:2])
# print(y)
# print(type(y))
# del x
# print(x)
# x = [[1, 2, 3], [4, 5, 6],['Hi'],['what']]
# y = [10, 11, 12]
# z = [9, 8, 7]

# print(x[0])
# print(x[1:2])
# print(x[-3])
# print(x[1][0:2])

# print(x + y)
# print(z*3)
# #print(z + "hello")
# print(z[1] + 1)
# #z.sort(reverse = True)

# z.append(4)
# z.extend([1,2])
# print(z)
#z.remove()
# print(len(x))
# print(x[0][0])

# y = range(5, 10)

# a = list(y)
# print(a.pop()) #5, 6, 7, 8, 9
# print(a.insert(1, 10))
# print(a)

# a.clear()
# print(a)

