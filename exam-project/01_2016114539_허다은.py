Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def rootfinding(a,b,c):
	D = b**2 - 4*a*c
	x1 = (-b + D**0.5)/(2*a)
	x2 = (-b - D**0.5)/(2*a)
	if D == 0:
		print('중근 x = ',x1)
	elif D > 0 :
		print('실근 2개 x1 = ',x1,', x2 = ',x2)
	else :
		print('복소수 2개 x1 = ',x1,', x2 = ',x2)

		
>>> 
