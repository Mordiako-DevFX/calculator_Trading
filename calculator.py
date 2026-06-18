# Function to calculate position size based on custom risk percentage
def calculate_position_size(balance, stop_loss, risk_percent):
    # 1. Calculate allowed risk in dollars
    allowed_risk_dollars = balance * (risk_percent / 100)

    # 2. Calculate position size (volume)
    volume = allowed_risk_dollars / stop_loss

    return volume



b = float(input("Enter account balance ($): "))
sl = int(input("Enter stop loss (pips): "))
r = float(input("Enter risk percentage (e.g., 1 or 2): "))


position_size = calculate_position_size(b, sl, r)

print(f"Maximum position size for this trade: {position_size}")