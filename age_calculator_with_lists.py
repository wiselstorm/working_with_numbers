names=[]
birth_years=[]
calculation=[]
maximum_lenght=2
current_year=int(input("Enter the current year\n"))

while len(names)<maximum_lenght:

    names.append(input("Enter your name\n"))
    birth_years.append(int(input("Enter your birth year\n")))
    print(birth_years)
    calculation.append(current_year-birth_years[-1])

print(calculation)




