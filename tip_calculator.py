def calculate_tip(total_bill, tip_percentage):
    tip_amount = total_bill * (tip_percentage / 100)
    return tip_amount

def main():
    try:
        total_bill = float(input("Enter the total bill amount: $"))
        tip_percentage = float(input("Enter the tip percentage you want to give: "))
        
        tip_amount = calculate_tip(total_bill, tip_percentage)
        
        print(f"\nTip amount: ${tip_amount:.2f}")
        print(f"Total amount (including tip): ${total_bill + tip_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
