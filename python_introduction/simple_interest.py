# simple_interest.py 
#Define Variables
principal = 1000 # $1000
rate = 0.05 # 5% annual interest rate
time = 3 # 3 years
# Print variables to verify
print(f"Principal: ${principal}")
print(f"Rate: {rate * 100}%")
print(f"Time: {time} years")
# Calculate the simple interest using the formula I = P * R * T
interest = principal * rate * time
# Print the results
print(f"The simple interest is: {interest}")
