str="bugs"
list=[1,6,8,9]
#%f for floating numbers
print('%s found %f in sanity testing'%(str,5))
for i in list:
    print('%f'%i)
# %a.bf(float point precision) should print the value float value
#if given floatvalue is 12.5678943 it prints the value 12.5678
print('the average is %0.4f'%(12.5678943))
print('the total is %0.0f'%(14.196))


x=44
y=12.678956
#To print multiple formats
print('the given number is %d \n Given number float value is %f'%(x,x))
print('The given float value is %f \n float value %2.2f'%(x,y))

#Exponential
print('exponent of %e'%(y))


#octal number
print('octal number %o'%(x))

#for binary
print("{0:b}".format(x))

#octal hexadecimal
print("{0:x}".format(x))