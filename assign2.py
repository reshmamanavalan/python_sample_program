#pilot
alti=input("Enter the altitude:")
altitude=int(alti)
if altitude<=1000:
    print("safe to land")
elif altitude>1000 and altitude<5000:
    print("Bring down to 1000")
elif altitude>5000:
    print("Turn around")
