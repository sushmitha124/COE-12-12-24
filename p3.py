
p_score=int(input("Enter project score"))
i_score=int(input("Enter internal score"))
e_score=int(input("Enter external score"))
if(p_score>=50 and i_score>=50 and e_score>=50):
    total=((70*p_score)/100)+((10*i_score)/100)+((20*e_score)/100)
    if(total>=90):
        print("A grade")
    elif(total>80):
        print("B grade")
    else:
        print("C grade")
else:
    if(p_score<50):
        print("failed in project")
    if(i_score<50):
        print("failed in internal")
    if(e_score < 50):
        print("failed in external")