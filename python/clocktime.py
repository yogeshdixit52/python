time = int(input("Enter curret time : "))
hr = int(input("Enter no. of hrs : "))
time2 = (time + (hr%24))%24
print("Time at which alarm will ring : ",time2,"hrs")
