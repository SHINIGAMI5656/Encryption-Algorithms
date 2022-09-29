try:
	#convert lowercase letters to numbers
	lt_n=dict(zip('abcdefghijklmnopqrstuvexyz',range(1,27)))
	#convert numbers to lowercase letters
	ln_t=dict(zip(range(1,27),'abcdefghijklmnopqrstuvexyz'))

	#convert upercase letters to numbers
	ut_n=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(1,27)))
	#convert numbers to uppercase letters
	un_t=dict(zip(range(1,27),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	mode=input("press e for encryption d for decryption ")
	l=[]

	#code for encryption 
	if(mode=='e'):
		shift=int(input('enter the number by which digits should be shifted '))
		plain_text=input("enter text for encryption ")
		for i in plain_text:
			if(i.isupper()):
				tmp=ut_n[i]+shift
				tmp=tmp%26
				l.append(un_t[tmp])
			elif(i.islower()):
				tmp=lt_n[i]+shift
				tmp=tmp%26
				l.append(ln_t[tmp])
		print("".join(l))

	#code for decryption
	elif(mode=='d'):
		shift=int(input('enter the number by which digits should be shifted '))
		plain_text=input("enter text for encryption ")
		for i in plain_text:
			if(i.isupper()):
				tmp=ut_n[i]-shift
				tmp=tmp%26
				l.append(un_t[tmp])
			elif(i.islower()):
				tmp=lt_n[i]-shift
				tmp=tmp%26	
				l.append(ln_t[tmp])
		print("".join(l))

except ValueError:
	print("Enter a valid integer value")