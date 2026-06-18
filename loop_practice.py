user_input = input("Enter your trades separated by spaces")
string_list = user_input.split()

trades = []

for iteme in string_list:
    trades.append(float(iteme))

total_profit = 0
total_loss = 0
win_trade = 0

for trade in trades:
    if trade > 0:
        total_profit += trade
        win_trade += 1
        print(f"[+] Win: ${trade}")
    else:
        total_loss += (-trade)
        print(f"[-] Loss: ${trade}")

total_trade = len(trades)
win_Rate = (win_trade / total_trade) * 100

print(f"\n[+] Total Profit: ${total_profit}")
print(f"[-] Total Loss: ${total_loss}")
print(f"[*] Net Profit: ${total_profit -total_loss}")
print(f"[*] Win Rate: {win_Rate}%")
