from sys import argv

script,file_name=argv

txt=open(file_name)

print "Hello , here is your file %r:"%file_name
print txt.read()

print "file name again????"
file_name_again=raw_input('>')

txt_again=open(file_name_again)

print "here agin"
print txt_again.read().capitalize()