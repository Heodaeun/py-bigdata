Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def ordering():
	a = input("숫자를 입력하시오. ex> 1,2,3,4,5\n")
	num = len(a)
	a = list(a)
	for i in range(num):
		for j in range(i,num):
			if a[i] > a[j]:
				a[i],a[j] = a[j],a[i]
	print(a)
