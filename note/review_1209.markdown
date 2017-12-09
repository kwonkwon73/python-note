####Date : 17.12.09 Sat
####Review :

####1. Formatters
Today I learned `Formatter` in Python.
But I think it is different Python2 and python3.
so I add some link for review later.
- https://www.python-course.eu/python3_formatted_output.php


(this time it is enough to know that some formatters have been used in python.)

now I can use `%r`, `%s`, `%d` with variables.
- `%r` : both string and number
- `%s` : with string
- `%d` : with number

####2. round()
If you use `round()` functions carelessly, It cause bugs. For example...
```
#convert pounds to kilos
kilos = 3
convert1 = kilos * 0.4535
convert2 = kilos * round(0.4535)
convert3 = kilos * round(0.4535, 3)

print("%skilos is %rpounds." % (kilos, convert1))
print("%skilos is %rpounds." % (kilos, convert2))
print("%skilos is %rpounds." % (kilos, convert3))

#results
#3kilos is 1.3605pounds.
#3kilos is 0pounds.
#3kilos is 1.362pounds.
```
