# for i in range(5):
#     print("Iteration:",i)

# count=0
# while count<5:
#     print("Count is:",count)
#     count+=1


# def greet(name):
#     print("Hello,"+name+"!!")
    
# greet("sanket")
# a=6+2
# b=6-2
# c=6*2
# d=6/2
# e=6%2
# f=6**2

# print("sum of 6+2 is :",a)
# print("substraction of 6-2 is :",b)
# print("sum of 6*2 is :",c)
# print("sum of 6/2 is :",d)
# print("sum of 6%2 is :",e)
# print("sum of 6**2 is :",f)

# a=(4+5)/3*2-1
# b=6/3+2*(3+2)
# print("value of a is ",a)
# print("value of b is ",b)

# length=int(input("Enter the length :"))
# width=int(input("Enter the breadth :"))
# # height=int(input("Enter the height :"))
# area=length*width

# print("Area of triangle is ",area)


# num1=int(input("Enter first value :"))
# num2=int(input("Enter second value :"))
# quotient=num1/num2
# reminder=num1%num2
# print("The quotient of two number is",quotient)
# print("The reminder of two number is",reminder)

# x=5
# y=9
# a=34
# b=43
# c=(x<y) or (a<b)
# print("Result upon applying "or" operator ",c)

# num1=int(input("Enter a number greater than 18 : "))
# if(num1>18):
#     print("corrected number")
# else:
#     print("Incorrected number")

# print("1.calculate area of square")
# print("2.calculate volume of a cube")
# choice=int(input("Enter your choice(1 or 2 ):"))
# side=int(input("Enter the side of length :"))
# if(choice==1):
#     print("the area of square is :",side*side)
# else:
#     print("The volume of the cube is :",side*side*side)



# data = {
#     "text": ["I don't love this product", "This is bad", "Amazing experience"],
#     "label": ["negetive", "negative", "positive"]
# }

# df = pd.DataFrame(data)
# print(df)




import pandas as pd

data = {
    "text": ["I love this product", "This is bad", "Amazing experience"],
    "label": ["positive", "negative", "positive"]
}

df = pd.DataFrame(data)
print(df)