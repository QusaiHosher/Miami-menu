print("""
**************************************
**    Welcome to the Miami Cafe!    **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

while True :
    a=input(" ")
    if a == "quit" :
        break
    else :
        txt="** 1 order of {} have been added to your meal **"
        print(txt.format(a))