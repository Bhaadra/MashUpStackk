def greeting():
    name=input("Enter Your Name:")
    age= int(input("Enter Your Age:"))
    age100=  100 - age
    year=2023+ age100
    print("Hello", name,"! You will be 100 years old by", year)
greeting()

