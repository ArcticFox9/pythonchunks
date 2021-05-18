

print ('Hello, world!')
#2 lines: Input, assignment


name = input('What is your name?\n')
print ('Hi, %s.' % name)
#3 lines: For loop, built-in enumerate function, new style formatting


friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
   print ("iteration {iteration} is {name}".format(iteration=i, name=name))
#4 lines: Fibonacci, tuple assignment


parents, babies = (1, 1)
while babies < 100:
   print ('This generation has {0} babies'.format(babies))
   parents, babies = (babies, parents + babies)


#5 lines: Functions


def greet(name):
    print ('Hello', name)

greet('Jack')
greet('Jill')
greet('Bob')
#6 lines: Import, regular expressions


import re
for test_string in ['555-555-1212', '666-666-5717', '72-5717awemowehindajuuungle']:
    if re.match(r'^\d{3}-\d{3}-\d{4}$', test_string):
        print (test_string, 'is a valid US local phone number')
    else:
        print (test_string, 'rejected')
#7 lines: Dictionaries, generator expressions


prices = {'apple': 0.40, 'banana': 0.50, 'feijoa': 0.20,}
my_purchase = {
    'apple': 4,
    'banana': 6,
    'feijoa': 2}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print ('I owe the grocer $%.2f' % grocery_bill)
