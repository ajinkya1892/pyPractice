from sys import argv
script, user_name= argv
prompt=':>'
print "HI  %s,the script is at %s, "%(user_name,script)

print "wheere do you live %s ?"%user_name
location=raw_input(prompt)

print "Alright %s is nice place.."%location