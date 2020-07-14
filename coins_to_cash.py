def coins_to_cash(**coins):
  return coins["pennies"] * 0.01 + coins["nickels"] * 0.05 + coins["dimes"] * 0.1 + coins["quarters"] * 0.25


print(coins_to_cash(pennies= 342, nickels=9, dimes=32, quarters=4))