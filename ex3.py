from decimal import Decimal
from fractions import Fraction
print "I ll be doing some math now"
print """lets check out these symbols: 
+     plus
-     minus
/     slash
*     asterisk
%     percent
<     less-than
>     greater-than
<=   less-than-equal
>=   greater-than-equal"""

print "plus", 9+8
print "minus",9-8
print "slash",9/3
print "slash, not whole no",9/4
print "asterisk",9*3
print "percent",9%3
print "less tahn ", 9<3
print "grater than",9>3
print "less than equal",9<=3
print "grater than equal",9>=3


print "lets do some floating point arithmetic"
print "9/2 without f.point", 9/2
print "9/2 with f.point", float(9)/2
print "9/2 with f.point, another way", 9/float(2)
print "9/2 with f.point, another way, one more", float(9)/float(2)
print "9/2 with f.point, another way, one more, this one is different(need to import decimal", Decimal(9)/2
print "9/2 with f.point, another way, one more, this one is different(need to import fractions", Fraction(9)/2
print "9/2 with f.point, another way, one more,without importing or typcasting", 9.0/2.0


