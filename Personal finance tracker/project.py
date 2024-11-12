



#importing libraries like pandas,numpy,matplolib,os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

#checking wheter data.csv file exits or not
if os.path.exists("data.csv"):
    file_name = pd.read_csv("data.csv", index_col="Transaction_id")
    if "Transaction_id" not in file_name.columns:
     file_name["Transaction_id"] = range(1, len(file_name) + 1)
    transaction_id = file_name["Transaction_id"].max() + 1 if not file_name.empty else 1

else:
    transaction_id = 1
    file_name = pd.DataFrame(columns=["Transaction_id", "Date", "Category", "Description", "Type", "Amount"])
    file_name.to_csv("data.csv", index=False)


#main menu
def main():
  while True:
   print("==========================")
   print(" PERSONAL FINANCE TRACKER ")
   print("==========================")
   print(" 1. Add Income")
   print(" 2. Add Expense")
   print(" 3. Show all Transactions")
   print(" 4. Show Balance")
   print(" 5. Show Transaction Analysis")
   print(" 6. Update Transaction")
   print(" 7. Quit")
   x=int(input("Enter Choice:" ))
   choice(x)


#what choice is selected
def choice(option):
   if option==1:
     print(add_income())
   elif option==2:
     print(add_expense())
   elif option==3:
     show_all()
   elif option==4:
     balance()
   elif option==5:
     analytics()
     print("Check your Directory for saved Images\n")
   elif option==6:
     update(file_name)
   elif option==7:
      sys.exit()
   else:
    print("Invalid Option\n")


#adding income to dataframe
def add_income():

    #check if date is of correct format
    global transaction_id
    while True:
        try:
            date = input("Enter Date (yyyy-mm-dd):")
            pd.to_datetime(date)
            break
        except ValueError:
            print("Invalid date format. Please try again.")
    cat=input("Enter Category:").capitalize()
    desc=input("Enter Description:").capitalize()
    amt=int(input("Enter Amount:"))
    income=pd.DataFrame({"Transaction_id": [transaction_id],"Date":[date],"Category":[cat],"Description":[desc],"Type":["Income"],"Amount":[amt]})
    transaction_id += 1
    global file_name
    file_name=pd.concat([file_name,income] ,ignore_index=True)
    file_name = file_name[["Transaction_id", "Date", "Category", "Description", "Type", "Amount"]]
    file_name.to_csv("data.csv", index=False)
    print("Data successfully added\n")


#adding expense to dataframe
def add_expense():
    global transaction_id
    while True:
        try:
            date = input("Enter Date (yyyy-mm-dd):")
            pd.to_datetime(date)
            break
        except ValueError:
            print("Invalid date format. Please try again.")
    cat=input("Enter Category:").capitalize()
    desc=input("Enter Description:").capitalize()
    amt=int(input("Enter Amount:"))
    expense=pd.DataFrame({"Transaction_id": [transaction_id],"Date":[date],"Category":[cat],"Description":[desc],"Type":["Expense"],"Amount":[amt]})
    transaction_id += 1
    global file_name
    file_name=pd.concat([file_name,expense] ,ignore_index=True)
    file_name = file_name[["Transaction_id", "Date", "Category", "Description", "Type", "Amount"]]
    file_name.to_csv("data.csv", index=False)
    print("Data successfully added\n")


#show the transactions table
def show_all():
    table=pd.read_csv('data.csv', parse_dates=["Date"])
    print(table)
    print()

# show balance and also show average income,expense
def balance():
    inc=file_name.loc[file_name["Type"] == "Income", "Amount"].sum()
    exp=file_name.loc[file_name["Type"] == "Expense", "Amount"].sum()
    bal=inc-exp
    avg_inc=np.mean(file_name.loc[file_name["Type"] == "Income"]["Amount"])
    avg_exp=np.mean(file_name.loc[file_name["Type"] == "Expense"]["Amount"])
    print(f"Balance:{bal:.2f}")
    print(f"Average income:{avg_inc:.2f}")
    print(f"Average expense:{avg_exp:.2f}")
    print()

#show visualisatons
def analytics():

  #income vs expense
  inc=file_name.loc[file_name["Type"] == "Income", "Amount"].sum()
  exp=file_name.loc[file_name["Type"] == "Expense", "Amount"].sum()
  comp=pd.DataFrame({"Type":["Income","Expense"], "Amount":[inc,exp]})
  comp.plot(kind='bar',x='Type',y='Amount')
  plt.xlabel('Type')
  plt.ylabel('Amount')
  plt.title('Income and Expense Comparison')
  plt.savefig('income_vs_expense.png')

  #income category wise
  income_grp=file_name.loc[file_name["Type"] =="Income"].groupby("Category")["Amount"].sum()
  income_grp.plot(kind='pie', autopct='%1.1f%%')
  plt.title('Category Wise Income')
  plt.savefig('category_wise_income.png')

  #expense category wise
  category_grp=file_name.loc[file_name["Type"] =="Expense"].groupby("Category")["Amount"].sum()
  category_grp.plot(kind='pie', autopct='%1.1f%%')
  plt.title('Category Wise Expense')
  plt.savefig('category_wise_expense.png')



# Update any detail in my transaction
def update(filename):
      while True:
        trans_id = int(input("Enter the transaction ID to update: "))
        if trans_id not in file_name['Transaction_id'].dropna().values:
            print("Transaction not found!")
            continue
        print("What do you want to update?")
        print("1. Date")
        print("2. Category")
        print("3. Description")
        print("4. Amount")
        print("5. Type")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            new_date = input("Enter new date (yyyy-mm-dd): ")
            filename.loc[filename['Transaction_id'] == trans_id, "Date"] = new_date
        elif choice == 2:
            new_cat = input("Enter new category: ").capitalize()
            filename.loc[filename['Transaction_id'] == trans_id, "Category"] = new_cat
        elif choice == 3:
            new_desc = input("Enter new description: ").capitalize()
            filename.loc[filename['Transaction_id'] == trans_id, "Description"] = new_desc
        elif choice == 4:
            new_amt = int(input("Enter new amount: "))
            filename.loc[filename['Transaction_id'] == trans_id, "Amount"] = new_amt
        elif choice == 5:
            new_type = input("Enter new type (Income/Expense): ").capitalize()
            filename.loc[filename['Transaction_id'] == trans_id, "Type"] = new_type
        else:
            print("Invalid choice!")
            continue
        filename.to_csv("data.csv", index=False)

        print("Transaction updated successfully!")
        break



if __name__ == "__main__":
    main()



