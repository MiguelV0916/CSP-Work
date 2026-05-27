#Major_Recommendor
#init
import pandas as pd

data = pd.read_csv("major.csv")

id = data['id'].tolist()
rank = data['Rank'].tolist()
major = data['Major'].tolist()
total = data['Total'].tolist()
major_cat = data['Major_category'].tolist()
employed = data['Employed'].tolist()
unemployed = data['Unemployed'].tolist()
rate = data['Unemployment_rate'].tolist()
median = data['Median'].tolist()

filter = []
#Functions
def payment(pay,pay2):   #This programs helps users find out how much pay they want at min and max
    for i in range(len(major)):
        if median[i]<=(pay) and median[i]>=(pay2):
            filter.append(major[i])
    print(filter)
    filter.clear()

def amount():
        purpose = input("How many people should already be in your field? (little,medium, large): ").lower() #This program helps users find how filled their major is.
        if purpose == "little":
            for i in range(len(major)):
                if employed[i]<= 10000:
                    filter.append(major[i])
            print(filter)
            filter.clear()
        if purpose == "medium":
            for i in range(len(major)):
                if employed[i]>= 10001 and employed[i] <= 100000:
                    filter.append(major[i])
            print(filter)
            filter.clear()
        if purpose == "large":
            for i in range(len(major)):
                if employed[i]>= 100001:
                    filter.append(major[i])
            print(filter)
            filter.clear()
def percent():
        num = input("Pls tell us how much employment rate matters:(little, medium, large):") #this Program helps users sort their options through Employment percentages
        if num == "little":
            for i in range(len(major)):
                if rate[i]<= 0.05:
                    filter.append(major[i])
            print(filter)
            filter.clear()
        if num == "medium":
            for i in range(len(major)):
                if rate[i]>= 0.051 and rate[i] <= 0.079:
                    filter.append(major[i])
            print(filter)
            filter.clear()
        if num == "large":
            for i in range(len(major)):
                if rate[i]>= 0.08:
                    filter.append(major[i])
            print(filter)
            filter.clear()
def all(pay, pay2,user_rate, user_employed):
    #Step one: This is La oop
    for i in range(len(major)):
        #Step 2: This then filters out by pay
        if median[i] <= pay and median[i] >= pay2:
            #Step 3: This if helps filter out by unemployment rate
            if rate[i] >= user_rate - 0.08 and rate[i] <= user_rate + 0.08:
                #Step 4: This if statement help filters out by how filled the Major is
                if employed[i] >= user_employed - 30000 and employed[i] <= user_employed + 30000:
                    filter.append(major[i])
    print(filter)
    filter.clear()



def main():
    print("Hello, Welcome to your college major finder.")
    while True:
        #Here is the main menu. You will be able to choose where you wasnt to go if it through pay,emlpoyment rate, or even how cometative. You also can choose all the above.
        attention = input("What do you want to find a College major based on? (Pay, unemployment rate, employed, all or Exit): ").lower()
        if attention == "pay":
            pay = int(input("What is your maximum pay? "))
            pay2 = int(input("What is your minimum pay? "))
            payment(pay, pay2)
        if attention == "unemployment rate":
            percent()
        if attention == "employed":
            amount()
        if attention == "all":
            print("Example: For Pereoleum Engineering try (110000,110000,0.0183,1976")
            print("Example: For Nurse try (48000,48000,0.0448,180903)")
            pay = int(input("What is your maximum pay? "))
            pay2 = int(input("What is your minimum pay? "))
            print("The higher the percent the less they are employed, Try a number 0.000-0.200. Your number will be have a +-of 0.08:")
            user_rate = float(input(" give a number 0.000-0.200:"))
            print("The higher the number the more filled this field will be. Try a number 1000-200000. Your number will have a +- 30000:")
            user_employed = int(input("How many people should already be in this field?"))
            all(pay,pay2,user_rate,user_employed)

        if attention == "exit":
            print("Goodbye!")
            break

#Main
main()

#// This algorithm for finding the values of all the data in a list taken from https://github.com/rfordatascience/tidytuesday/tree/main/data/2018/2018-10-16
#Data Set was provided by code.org
