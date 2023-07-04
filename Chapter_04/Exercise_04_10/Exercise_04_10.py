"""
10. Tuition Increase
At one college, the tuition for a full-time student is $8,000 per semester. It has been announced
that the tuition will increase by 3 percent each year for the next 5 years. Write a program
with a loop that displays the projected semester tuition amount for the next 5 years.

@author Sharaf Qeshta
"""

current_tuition_cost = 8_000
print("Year\t\tTuition Cost")
for i in range(5):
    print(f"{i+1}\t\t\t${format(current_tuition_cost, '.2f')}")
    current_tuition_cost += current_tuition_cost * 0.03
