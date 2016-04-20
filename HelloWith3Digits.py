#Simple Greeting App


name = raw_input("Enter name: ")
namelen = len(name)
namelenminus = len(name)-3
print "Good morning, " + name + "!",
print "Your name is " + str(len(name)) + " characters and the last 3 characters of your name are " + name[namelenminus:namelen] 
