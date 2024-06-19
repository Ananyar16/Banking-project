import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("_____________________________________________________________")
print()
print()
print("WELCOME TO IAVS BANK")
print()
print('_____________________________________________________________')
print()
print("")
print("")
print("")
print("")
print("")


def Main_menu():
    while True:
        print("MAIN MENU")
        print('_________________________________________')
        print()
        print('1. CUSTOMER')
        print('2. EMPLOYEE')
        print('3. BRANCHES')
        print('4. TRANSACTIONS')
        print('5. HOLIDAYS')
        print('6. FEEDBACK') 
        print('7. LOGOUT/EXIT')
        print()
        print('_________________________________________')
        print()
        a=int(input("Enter your choice =  "))
        if a==1:
            cust()
        elif a==2:
            emp()
        elif a==3:
            branch()
        elif a==4:
            trans()
        elif a==5:
            holiday()
        elif a==6:
            feedback()
        elif a==7:
            logout()
            break
        else:
            print()
            print("Wrong choice. Enter again.")
def login():
    df1=pd.read_csv("passw.csv",names=['user','pass'])
    print(df1)
    n=input("ENTER NAME:       ")
    p=input("ENTER PASSWORD:   ")
    for (col, colSeries) in df1.iteritems():
        print('=-=-=-=-=-=-=-=-=-==-=-=-=-=-=')
        ctr=0
        for val in colSeries:
            if val==n:
                ctr=ctr+1
            if val==p:
                ctr=ctr+1
    if ctr==2:
        
        print("Access given")
    

def register():
    df1=pd.read_csv("passw.csv",index_col=0)
    name=input("enter your name:     ")
    p=input("enter your passw:       ")
    df1.loc['name',:]=p
    df1.to_csv("passw.csv")

def cust():
    df3=pd.read_csv("customer.csv",index_col=0)
    while True:
        print()
        print()
        print("---------------------------------------------------------------")
        print("1. Customer Database") 
        print("2. Loans Applied")
        print("3. Account details")
        print("4. Credit Amount")
        print("5. Debit Amount")
        print("6. Account balance")
        print("7. Locker availed")
        print("8. Investment profile")
        print("9. Loan status")
        print("10. Mutual funds")
        print("11.Exit")
        print("---------------------------------------------------------------")
        print()
        print() 
        r=int(input("Enter your choice   =    "))
        print()
        print()         
        if r==1:
            print(df3.T)
        elif r==2:
            print(df3[['Name','no. of loans']])
        elif r==3:
            print(df3[['Name','Account balance']])
        elif r==4: 
            print(df3['Amount credited'])
        elif r==5:
            print(df3['Amount debited'])
        elif r==6:
            print(df3['Account balance'])
        elif r==7:
            print(df3['Locker availed'])
        elif r==8:
            print(df3['Investment in mutual funds'])
        elif r==9:
            print(df3['Loan status'])
        elif r==10:
            print(df3[['Mutual funds','Investment in mutual funds']])
        elif r==11:
            break
    else:
        print('Wrong choice. Try again')
 
def emp():
    df1=pd.read_csv("Emp_data.csv")
    while True:
        print()
        print()
        print("---------------------------------------------------------------")
        print("1. Employee Database")
        print("2. Employee name")
        print("3. Total 5alary paid")
        print("4. Details of a particular employee")
        print("5. Aadhar card and pan card no of all employees")
        print("6. Employee Salary bar graph")
        print("7. Check retirement status")
        print("8. Pension status")
        print("9. Joining Date")
        print("10. Provident fund")
        print("11. Provident fund bar graph")
        print('12. Exit')
        print("---------------------------------------------------------------")
        print()
        print()
        x=int(input("Enter your choice   =   "))
        print()
        print()    
        if x==1:
            print(df1)
        elif x==2:
            print(df1.iloc[:,0:2])
        elif x==3:
            print(df1[['Emp_ID','Name','Salary']])
        elif x==4:
            df1=pd.read_csv("Emp_data.csv",index_col=0)
            n=input("Enter Empolyee id   =   ")
            print(df1.loc[n])
        elif x==5:
            print(df1[['Aadhar no.','PAN card no.']])
        elif x==6:
            plt.bar(df1['Name'],df1['Salary'],color='r',width=0.20)
            plt.title("Salary of employees")
            plt.show()
            print("The bar graph shows the employee name on the x axis and their salary on the y axis")    
        elif x==7:
            print(df1[['Name','Retirement status']])
        elif x==8:
            print(df1[['Name','Pension Status']])
        elif x==9:
            #showing keyerror
            print(df1[['Name','Joining date']])
        elif x==10:
            print(df1[['Name','Provident fund']])
        elif x==11:
            plt.bar(df1['Name'],df1['Provident fund'],color='cyan',width=0.25)
            plt.title("Provident Fund")
            plt.show()
            print("The bar graph shows provident fund of all employees")
        elif x==12:
            break
                    
        else:
            print("Wrong option. Try again") 

def branch():
    df=pd.read_csv("branches.csv")
    print("Branches over India with their facilities")
    print(df)   

def trans():
    df1=pd.read_csv("Emp_data.csv")
    df3=pd.read_csv("customer.csv",index_col=0)
    s=pd.Series(data=df3['Account balance'])
    dx=pd.DataFrame(data=df3['Account balance'])    
    df3['NaN']=0
    while True:
        print("---------------------------------------------------------------")
        print('1. Total amount in bank')
        print('2. Transfer amount in an account')
        print('3. Add money to my account')
        print('4. Withdraw money')
        print("5. Double line graph of credit amount and debit amount")
        print('6. Exit')
        print("---------------------------------------------------------------")
        w=int(input('Enter your choice-      '))
        
        if w==1:
            df3=pd.read_csv("customer.csv")
            print(df3['Account balance'])       
        elif w==2:
            a=int(input("Enter account number=        "))
            x=s[a]
            b=int(input("Enter amount  =   "))
            s[a]=x+b
            print("The amount is changed to ",s[a])
        elif w==3:
            a=int(input("Enter account number=        "))
            x=s[a]
            b=int(input("Enter amount  =   "))
            s[a]=x+b
            print("The amount is changed to ",s[a])
        elif w==4:
            a=int(input("Enter account number=        "))
            x=s[a]
            b=int(input("Enter amount  =   "))
            s[a]=x-b
            print("Account balance after withdrawl is    ",s[a])
        elif w==5:
            plt.plot(df3['Account balance'],df3['Amount credited'],color='r',label='Credit amount')
            plt.plot(df3['Account balance'],df3['Amount debited'],color='cyan',label='Debit amount')
            plt.xlabel('Account balance')
            plt.ylabel('Amount')
            plt.legend(loc='upper left')
            plt.show()
        elif w==6:
            break
        else:
            print("Wrong option. Try again")
            
def holiday():
    h=["Republic Day","Mahashivratri",'Holi',\
       'Annual Closing of banks',"Good friday",\
       "Ram Navami",'Mahavir Jayanti',\
       "Id ul Fitr",'Id ul Fitr',\
       'Buddha Purnima','Bakrid',\
       'Bakrid','Independence Day',\
       'Muharram',"Janamashtmi",\
       "Gandhi Jayanti",'Vijiya dakshmi',\
       'Id e Milad','Diwali','Guru Nanak Jayanti']
    d=["26-01-2021",'11-03-2021','29-03-2021',\
       '01-04-2021','02-04-2021',\
       '21-04-2021','25-04-2021',\
       '13-05-2021','14-05-2021',\
       '26-05-2021','20-07-2021',\
       '21-07-2021','15-08-2021',\
       '19-08-2021','30-08-2021',\
       '02-10-2021','15-10-2021',\
       '19-10-2021','04-11-2021','19-11-2021']
    m=["January","March","March",\
       'April','April',\
       'April','April',\
       "May","May",\
       "May",'July',\
       'July','August',\
        'August','August',\
       "October","October",\
       "October",'November','November']
    s=pd.Series(data=h,index=d)
    s1=pd.Series(data=h,index=m)
    while True:
        print('MENU:')
        print()
        print("---------------------------------------------------------------")
        print('1. Print all holidays' )
        print('2. Show all holidays in a particular month')
        print('3. Exit')
        print("---------------------------------------------------------------")
        print()
        x=int(input("Enter your choice =   "))
        if x==1:
            print('All second saturdays and fourth saturdays of the month are bank holidays')
            print()
            print(s)
        if x==2:
            print("---------------------------------------------------------------")
            print()
            print("1.January")
            print("2.Feburary")
            print("3.March")
            print("4.April")
            print("5.May")
            print("6.June")
            print("7.July")
            print("8.August")
            print("9.September")
            print("10.Octuber")
            print("11.November")
            print("12.December")
            print()
            print("---------------------------------------------------------------")
            print()
            a=int(input("Enter your choice  =     "))
            print("________________________________________________________________")
            if a==1:
                print("Holdiays in January")
                print()
                print(s1['January'])
            elif a==2:
                print("Holdiays in Feburary")
                print()
                print('No holidays')
            elif a==3:
                print("Holidays in March")
                print()
                print(s1['March'])
            elif a==4:
                print("Holdiays in April")
                print()
                print(s1['April'])
            elif a==5:
                print("Holdiays in May")
                print()
                print(s1['May'])
            elif a==6:
                print("Holdiays in June")
                print()
                print('No holidays')
            elif a==7:
                print("Holdiays in July")
                print()
                print(s1['July'])
            elif a==8:
                print("Holdiays in August")
                print()
                print(s1['August'])
            elif a==9:
                print("Holdiays in September")
                print()
                print(s1['September'])
            elif a==10:
                print("Holdiays in October")
                print()
                print(s1['October'])
            elif a==11:
                print("Holdiays in November")
                print()
                print(s1['November'])
            elif a==12:
                print("Holdiays in December")
                print()
                print('No Holdiays')
        if x==3:
            break
        else:
            print("Wrong option. Try again")
            
    

def feedback():
    f=input("Enter your feedback -   ")
    s=pd.Series(f)
    df=pd.DataFrame(s)
    df.to_csv("Feedback.csv")
    print("Thank you for your feedback")

def logout():
    exit

print("Kindly login/register to continue using the website")
print()
print('1. LOGIN')
print('2. REGISTER')
print('3. EXIT')
print()
q=int(input('Enter your choice =   '))
if q==1:
    login()
elif q==2:
    register()
elif q==3:
    exit

else:
    print("Wrong option. Try again")
Main_menu()
    

