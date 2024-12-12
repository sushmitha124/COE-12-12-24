basic=int(input("Enter basic salary"))
if (basic<10000) :
    HRA = (67*basic)/100
    DA = (73*basic)/100
elif (basic<20000):
    HRA = (69 * basic) / 100
    DA = (76 * basic) / 100
else:
    HRA = (73 * basic) / 100
    DA = (89 * basic) / 100
GS = HRA + DA + basic
print("The final gross salary is",GS)

