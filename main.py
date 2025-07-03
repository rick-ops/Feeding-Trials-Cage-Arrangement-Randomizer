import matplotlib.pyplot as plt

# Cumulative Net Profit from Months 1 to 24
cumulative_net_profit = [
    -50000, -100000, -150000, -150000, -150000, -150000, -120000, -90000,
    -60000, 70000, 200000, 330000, 346500, 375500, 417000, 471000, 537500,
    616500, 708000, 812000, 928500, 1057500, 1199000, 1353000
]

# Adjusted for initial investment
initial_investment = -1500000
adjusted_cumulative = [initial_investment + val for val in cumulative_net_profit]

months = list(range(1, 25))

plt.figure(figsize=(10, 6))
plt.plot(months, adjusted_cumulative, marker='o', label='Net Profit w/ Initial Investment')
plt.axhline(0, color='red', linestyle='--', label='Breakeven Line')
plt.axhline(initial_investment, color='gray', linestyle=':', label='Initial Investment (-1.5M)')
plt.title('Breakeven Curve for Animal Feeds Venture')
plt.xlabel('Month')
plt.ylabel('Cumulative Profit (KES)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
