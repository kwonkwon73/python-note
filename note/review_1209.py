name = '동수'
print("안녕 %s야" % name)

age = 20
print("나는 작년엔 %r살, 올해는 %r살이야" % (age-1, age))

year1 = '천'
year2 = 10000
print("우리 %r년 %r년 사이좋게 지내자" % (year1, year2))


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
