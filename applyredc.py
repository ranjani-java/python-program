import pandas as pd

data = {
    "Name": ["Ravi", "Anu", "Kiran", "Meena"],
    "Age": [30, 22, 45, 19],
    "Income": [40000, 28000, 50000, 30000],
    "CreditScore": [720, 680, 750, 600],
    "LoanAmount": [300000, 200000, 400000, 150000]
}

df = pd.DataFrame(data)


eligible = df[
    (df["Age"] >= 21) &
    (df["Income"] >= 25000) &
    (df["CreditScore"] >= 650) &
    (df["LoanAmount"] <= df["Income"] * 10)
].copy()  
eligible["ProcessingFee"] = eligible["LoanAmount"] * 0.02


eligible["LoanStatus"] = "Approved"


total_loan = eligible["LoanAmount"].sum()

print("Eligible Customers:\n")
print(eligible)
print("\nTotal Approved Loan Amount:", total_loan)
