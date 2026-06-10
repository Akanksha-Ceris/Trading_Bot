# Trading Bot - Binance Futures Testnet

## Overview

This project is a Python-based trading bot designed for Binance Futures Testnet. The application follows a modular structure with separate components for client communication, order handling, validation, logging, and CLI interaction.

## Features Implemented

* Command Line Interface (CLI)
* Input validation
* Order management layer
* Logging configuration
* Binance client integration structure
* Error handling framework
* Support for MARKET and LIMIT order workflows

## Project Structure

trading_bot/

* cli.py
* client.py
* orders.py
* validators.py
* logging_config.py
* requirements.txt
* README.md

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

Example MARKET order:

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

Example LIMIT order:

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 65000
```

## Current Limitation

The Binance Futures Testnet API integration encountered authentication/permission issues during development (APIError -2015). The application structure and trading workflow have been implemented, and the API integration is prepared for completion once valid Testnet credentials and permissions are available.

## Future Improvements

* Complete Binance Futures Testnet order execution
* Add additional order types
* Improve CLI user experience
* Add automated tests
* Enhance logging and monitoring

## Author

Akanksha Kumari
