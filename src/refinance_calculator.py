import numpy as np

def calculate_refinance_options(loan, new_interest_rates, new_terms):
    options = []
    
    for rate in new_interest_rates:
        for term in new_terms:
            monthly_payment = (loan.principle * (rate / 12) * (1 + rate / 12) ** term) / ((1 + rate / 12) ** term - 1)
            total_interest = monthly_payment * term - loan.principle
            
            option = {
                'interest_rate': rate,
                'term': term,
                'monthly_payment': monthly_payment,
                'total_interest': total_interest
            }
            options.append(option)
    
    return options

# Usage
# loan = Loan(...)
# new_rates = [0.03, 0.035, 0.04]  # 3%, 3.5%, 4%
# new_terms = [180, 240, 360]  # 15 years, 20 years, 30 years
# refinance_options = calculate_refinance_options(loan, new_rates, new_terms)
