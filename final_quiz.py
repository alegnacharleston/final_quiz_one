first_name = raw_input("What is your first name?")
last_name = raw_input("What is your last name?")
print "Hi", first_name, last_name
limit = raw_input("What would you like the maximum limit to be?")
for n in range(1, int(limit)+1):
    if n % 3 == 0 and n % 5 == 0:
        print str("fizzbuzz")
    if n % 3 == 0:
        print str("fizz")
    if n % 5 == 0:
        print str("buzz")
    else:
        print n
