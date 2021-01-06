import fetch
import update


a = 'Olivar Twist'
b = '200'
c = '50'

print(fetch.byfirstname(a))

c='50'
print(update.byqty(a,b,c))


if fetch.byfirstname(a)== -1:
    print('no more books left')
else:
    print(fetch.byfirstname(a)[2])
