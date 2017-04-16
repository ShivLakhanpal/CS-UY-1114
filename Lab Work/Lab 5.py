import turtle

#1a

print("----------Problem 1a----------")

n = int(input("Please enter a positive integer: "))
space = n-1
asterix = 1
count = 1
line = ""
while(count <= n):
    line += space * " " + asterix * "*"
    asterix += 2
    space -= 1
    count += 1
    print(line)
    line = ""

#1b
print("----------Problem 1b----------")

n = int(input("Please enter a positive integer: "))
percent = 1
dolla = n-1
hashtag = 0
count = 1
line = ''
while (count <= n):
    line = hashtag * '#' + percent * '%' + dolla * '$'
    hashtag += 1
    dolla -= 1
    count += 1

    print(line)
    line = ''


#2

print("----------Problem 2----------")

n = int(input("Please enter a positive integer: "))
i = 1
num = 0
while (i <= n):
    num += i**3
    i += 1
print(num)

#3
print("----------Problem 3----------")

string = input('Please enter an expression: ')
letter = input('Please enter a letter: ')
counter = 0
for curr_chr in string:
    if curr_chr == letter:
        counter +=1
while(curr_chr == letter):
    counter += 1
print ('Letter',letter,'appears',counter,'times in your string.')

#4
print("----------Problem 4----------")
n = input('Please enter a positive integer: ')
even = 0
odd = 0

for i in range(len(n)):
    if (int(n[i]) % 2 == 1):
        odd += 1
    else:
        even += 1
print('There are ' + str(even) + ' even digits and ' + str(odd) + ' odd digits in this number')

#4b
print("----------Problem 4b----------")





#5

print("----------Problem 5----------")

n = int(input("Please Enter a Positive Integer: "))
for i in range(n):
    turtle.forward(100)
    turtle.right(180-(180*(n-2))/n)

#6

print("----------Problem 6----------")

n = int(input("Please enter a positive integer"))
i < n

for i in range(1 < i < n):
    if (i < n):
        print(i**3 < n)
    














