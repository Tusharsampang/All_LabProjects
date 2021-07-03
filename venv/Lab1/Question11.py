'''
11. Write a Python program to convert seconds to day, hour, minutes and seconds.
'''
second= int(input("Enter the times in seconds :"))
day= second/(24*60*60)  # day =24 , hour=60  , min=60
hour= second/(60*60)    # hour=60 mins ,  min=60sec
minutes= second/60    #minute= 60
print(f" {second} = {day} day \n {second} = {hour} hours \n {second}= {minutes} minutes")
