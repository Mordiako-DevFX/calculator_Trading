
def analyze_journal(trade_list):
    total_profit = 0
    total_loss = 0
    win_count = 0
    total_trades = len(trade_list)

    if total_trades == 0:
        return 0, 0

    for trade in trade_list:
        if trade > 0:
            total_profit += trade
            win_count += 1
        else:
            total_loss += (-trade)

    # محاسبات نهایی
    net_profit = total_profit - total_loss
    win_rate = (win_count / total_trades) * 100

    # فرستادن دو تا خروجی اصلی به بیرون از تابع
    return win_rate, net_profit



user_input = input("Enter your trades separated by spaces: ")
string_list = user_input.split()

trades = []
for item in string_list:
    trades.append(float(item))


w_rate, net_prof = analyze_journal(trades)


print("\n" + "="*30)
print(f"[*] Total Trades Analyzed: {len(trades)}")
print(f"[*] Win Rate: {w_rate:.2f}%")
print(f"[*] Net Profit: ${net_prof}")
print("="*30)