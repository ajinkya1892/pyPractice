from sys import argv

script,filename=argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "opening the file..."

target=open(filename,'w')

print "truncating the file . goodbye"
target.truncate()

print "now am going to ask you 3 lines"

line1=raw_input("line 1 : ")
line2=raw_input("line 2 : ")
line3=raw_input("line 3 : ")

print "going to write this to file..."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "finally, closing it..."
target.close()