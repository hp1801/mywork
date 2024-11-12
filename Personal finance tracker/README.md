 # Personal Finance Tracker
    #### Video Demo:  https://youtu.be/5DoKIvdEMNY
    #### Description:
     Project which helps in managing your income and expenses.




Perosnal Fiannce Tracker is is a command-line based project  which helps in management of income and expenses.It also allows to track your transactions,check your balance and generate analytics to understand your finanicial income and expense.

**Features:**
 Adding income and expenses
 Displaying Table of all your transactions
 Displaying the available balance along with average income and average expense
 Show Data analysis of your income and expense
 Update any detail in your transaction


**Functions:**

   The program checks if there exits a file for reading the data, if there is a pre-existing file it loads the file for reading else it creates a csv file as data.csv.
   There are 6 column in the file: Transaction_id,Date,Category,Description,Type,Amount,
   The first transaction is taken as 1 and it increments by 1 on next addition of a transaction in the dataframe.

  Add_income
     It allows us to add income which takes the date,category,description and amount as input.The type ie. income is already assumed.There is error handling if the date is in correct format or not.

  Add_expense
     It allows us to add expense which takes the date,category,description and amount as input.The type ie. expense is already assumed.There is error handling if the date is in correct format or not.

  Show_All
     This displays all the expenditures that have happended in a tabular form


  Balance
  This displays the balance that is available and also shows what is the average income and what is teh average expense.

  Analytics
   The data visuals are saved in the form png file which can be accessed in the directory.There are three plots: One is the ratio of income and expense,the second is category wise income plot and last is category wise expense plot.

  Update
   Here you can update any detail you want .First provide a transaction_Id  and then you have to choose the option of what do you want to update;
   date,category,type,amount or description.

  Main
   A main funtion was used to display the menu with all options.

  One of the things I learned was using '.loc' which is a accessor in Pandas dataframe which is used to access row and colums in the table.

**Libraries**
  Pandas,numpy,Matplotlib,os and sys were used for various operations









