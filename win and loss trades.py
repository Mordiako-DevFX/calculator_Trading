trades = input("pleas Enter trade list: ")

string_list= trades.split()
trades_list = []

for item in string_list:
    trades_list.append(float(item))

def get_winning_trades(trades):
    win_trades= []
    for t in trades:
        if t > 0:
            win_trades.append(t)
    return win_trades

def get_losing_trades(trades):
    loss_trades = []
    for t in trades:
        if t < 0:
            loss_trades.append(t)
    return loss_trades


win_trade= get_winning_trades(trades_list)
loss_trade = get_losing_trades(trades_list)

print(f"win trades: {win_trade}")
print(f"loss trades: {loss_trade}")