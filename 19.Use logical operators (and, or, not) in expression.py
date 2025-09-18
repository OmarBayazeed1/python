#19.Use logical operators (and, or, not) in expression
passed=True
paied=True
Accepted=passed and paied
print(f"Does the user Accepted? {Accepted}")
print(f"If the user passed or paied so Accepted: {Accepted}")
print("when the user does not have money",not paied,'not accepted')
