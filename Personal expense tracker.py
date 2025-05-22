""" 
Personal Expense Tracker
------------------
This python program allows user to take record of its daily expenses
Author by: Nikhilesh Rawat 

"""
import datetime
import os
#Function to enter today's expenses
def enter_expense():
        file1=open("Expense_file.txt","a")# open file in append mode
        day_expense={}#Dictonary to hold product and prices
        #Ask how many product they bought
        try:
            k=int(input("How many products you brought today"))
        except ValueError:
             print("\ninvalid value please enter number\n")
             return
       #take product name as input
        product=[]
        for i in range(k):
            product.append(input("Enter the product bought by you "))
        #Enter price for product
        for i in product:
            try:
                print("Enter price for this product ",i,": ")
                day_expense[i]=int(input()) # add in dictonary
            except ValueError:
                 print("\ninvalid input\n")
                 return
        # add total maximum expenditure and date
        total=sum(day_expense.values())
        day_expense['Maximum_expenditure']=max(day_expense.values())
        day_expense['total']=total
        day_expense['Date']=datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        conver_string=str(day_expense)
        conver_string=conver_string+"\n"
        file1.write(conver_string)# append in file
        file1.close()
def view_expense():
            # check whether file exists or not
            if os.path.exists("Expense_file.txt"): 
                print("\nExpense History\n")
                file1=open("Expense_file.txt","r") # open file in read mode
            
                for line in file1: #print each line of file
                    print(line.strip() +"\n")
                file1.close()
            else:
                 print("\nfile not found first try to enter the expenses\n")

# main program loop                 
while True:
    user_input= int(input('Enter one for enter today expense \n Enter two for check the expenses \n' 
                          ' Enter anything else  to quit  '))
    
    if user_input==1:
        enter_expense()
    elif user_input==2:
         view_expense()
    else:
        print("Have a nice day")
        break
