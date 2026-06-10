from orders import market_order

try:
    response = market_order(
        symbol="BTCUSDT",
        side="BUY",
        quantity=0.001
    )

    print(response)

except Exception as e:
    print("Error:", e)