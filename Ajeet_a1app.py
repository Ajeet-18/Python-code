import Ajeet_a1
old=str(input('Enter old currency:')).upper().strip()
new=str(input('Enter new currency:')).upper().strip()
amt=float(input('Enter ammount:'))
# DO NOT modify the following code
# if the source currency is not valid, quit
if(not(Ajeet_a1.is_currency(old))):
	print(old," is not a valid currency")
	quit()
# if the target currency is not valid, quit
if(not(Ajeet_a1.is_currency(new))):
	print(new," is not a valid currency")
	quit()

print(f'You can exchange {amt} {old} for {Ajeet_a1.exchange(old,new,amt)} {new}.')

