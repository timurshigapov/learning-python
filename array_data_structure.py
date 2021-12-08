# I. Let us say your expense for every month are listed below,
    # Create a list to store these monthly expenses and using that find out,
    # 1. In Feb, how many dollars you spent extra compare to January?
    # 2. Find out your total expense in first quarter (first three months) of the year.
    # 3. Find out if you spent exactly 2000 dollars in any month
    # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    # 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

expense = [2200, 2350, 2600, 2130, 2190]
months = ["Jan", "Feb", "March", "Apr", "May"]


def compare_expense():
    print("Enter month's to compare", months)
    month1 = input("Enter 1st month to compare: ")
    month2 = input("Enter 2d month to compare: ")
    
    compare = zip(months, expense)
    mth_1 = 0
    mth_2 = 0
        
    for i in compare:
        if i[0] == month1:
            mth_1 = i[1]
        elif i[0] == month2:
            mth_2 = i[1]

    result = mth_1 - mth_2
    print("Difference between", month1, "and", month2, "is:", result)
    
    pass


def quarter_expense():
    q = 0
    for i in range(len(expense)):
        if i < 3:
            q += expense[i]

    print(q)
    
 
def seacrh_exp(amount_exp):
    monthly_exp = {}
    compare = zip(months, expense)
    for i in compare:
        if amount_exp == i[1]:
            monthly_exp[i[0]] = i[1]

    if list(monthly_exp):
        print("The amount was spent in", list(monthly_exp))
    elif not list(monthly_exp):
        print("Amount not found.")
        

def new_amount_exp():
    while True:
        month = input("Enter month (to stop do not enter anything and hit Enter key):")
        if month == '':
            break
        else:
            months.append(month)
            break
            
    while True:
        new_amount = input("Enter new amount (to stop do not enter anything and hit Enter key):")
        if new_amount == '':
            break
        else:
            expense.append(new_amount)
            break
            
    print(months)
    print(expense)
    


# compare_expense()
# quarter_expense()
# seacrh_exp(1980)
new_amount_exp()
