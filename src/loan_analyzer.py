import matplotlib.pyplot as plt
import numpy as np

def calculate_future_payments(loan, months):
    payments = []
    remaining_balance = loan.principle
    
    for _ in range(months):
        interest = remaining_balance * (loan.interest_rate / 12)
        principal = loan.monthly_payment - interest
        remaining_balance -= principal
        payments.append(loan.monthly_payment)
    
    return payments

def graph_future_payments(loan, months):
    payments = calculate_future_payments(loan, months)
    
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, months + 1), payments)
    plt.title(f'Future Payments for Loan {loan.id}')
    plt.xlabel('Month')
    plt.ylabel('Payment Amount')
    plt.grid(True)
    plt.savefig(f'loan_{loan.id}_payments.png')
    plt.close()

# Usage
# loan = Loan(...)
# graph_future_payments(loan, 120)  # Graph payments for 10 years
