salary= input()
salary= float(salary)
tax_slab= 0 
if salary>=0 and salary<=20000:
    tax_slab=2
elif salary>=20001 and salary<=50000:
    tax_slab=5
elif salary>=50001 and salary<=100000:
    tax_slab=7
elif salary>=100000:
    tax_slab=10


print(tax_slab)



