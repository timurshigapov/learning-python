# expense_list = [2340, 2500, 2100, 3100, 2980]
# month_list = ['Jan', 'Feb', 'March', 'Apr', 'May']
# expense = int(input('Please enter your expense amount: '))
#
# for e in range(len(expense_list)):
#     if expense == expense_list[e]:
#         expense = e
#         break
# else:
#     expense = -1
#     print('not found')
#
#
# if expense >= 0:
#     for m in range(len(month_list)):
#         if expense == m:
#             print('The month of expense is: ',month_list[m])


shape = '*'
for i in range(len(shape)):
    print(shape)
    if len(shape) == 1:
        for i in range(4):
            shape = shape + '*'
            print(shape)
