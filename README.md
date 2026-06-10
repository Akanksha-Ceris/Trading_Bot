# Trading_Bot
A python-based trading bot that interacts with the Binance Futures Testnet API.The applciation supports placing MARKET and LIMIT  orderss through a commmand-line interface (CLI) 
# Trading Bot

## Setup

1. Create virtual environment
2. Install requirements
3. Create .env file

## Run Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## Run Limit Order

python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 100000

## Assumptions

Uses Binance Futures Testnet.
