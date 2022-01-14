def BMI():
    people_count = int(input("Input amount of people: "))
    answer = ""
    for i in range(people_count):
        weight = float(input("Enter weight (in kilograms): "))
        height = float(input("Enter height (in meters): "))
        calculation = weight / (height ** 2)
        if calculation < 18.5:
            answer = answer + "under "
        elif calculation >= 18.5 and calculation < 25:
            answer = answer + "normal "
        elif calculation >= 25 and calculation < 30:
            answer = answer + "over "
        else:
            answer = answer + "obese "
    print(answer)
BMI()
