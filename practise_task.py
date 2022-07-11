# firstStudent = int(input("enter first student Number: "))
# secondStudent = int(input("enter first student Number: "))
# thirdStudent= int(input("enter first student Number: "))
# fourthStudent = int(input("enter first student Number: "))

# number = {firstStudent, secondStudent, thirdStudent, fourthStudent}


# print(number)

# hello = {18, "18"}


# s = set()
# s.add(5)
# s.add(20.0)
# s.add("20")
# print(s)

# a = (7,0,8,0,0,9)
# print(a.count(0))

# translator = {
#     "shoshi":"শশী",
#     "Shuvo":"শুভ"
# }

# print(translator)

# number1 = int(input("enter first number: "))
# number2 = int(input("enter second number: "))
# number3 = int(input("enter third number: "))
# number4 = int(input("enter fourth number: "))


# if(number1>number2 and number1 > number3 and number1 > number4):
#     print("number 1 is big")
# elif(number2 > number3 and number2 > number4):
#     print("number 2 is big")
# elif(number3>number4):
#     print("number 3 is big")
# else:
#     print("number 4 is big")


# names = ["shuvo", "shoshi", "liza"]

# name = input("enter your name: ")

# if(name in names):
#     print("User allready exist")
# else:
#     names.append(name)
#     print(names)

# number = int(input("kon ghorer namota lagbo: "))
# for i in range(1, 11):
#     print(f"{number} X {i} = {number*i}")

# names = ["Shuvo", "Shohsi", "Liza", "Aliar", "Kibria", "Sunny"]

# for name in names:
#     if name.startswith("L"):
#         print("hello " + name)


# number = int(input("enter number to check it's prime or not: "))
# prime = True

# for i in range(2, number):
#     if(number%i==0):
#         prime=False
#         break
# if prime:
#     print("this is a prime number")
# else:
#     print("this is not a prime number")

# for i in range(2, 19):
#     print(i+i)


# number = int(input("which number factorial you want? enter the number: "))
# factorial = 1

# for i in range(1, number+1):
#     factorial = factorial * i
#     print(factorial)


# for i in range(100):
#     print("*" * i)




n = 3

for i in range(3):
    print(" " * (n-i-1))
    print("*" * (2*i+1))
    print(" " * (n-i-1))