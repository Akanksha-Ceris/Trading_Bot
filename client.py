from binance.client import Client
from dotenv import load_dotenv
import os
load_dotenv()
print("API_KEY =",os.getenv("API_KEY"))
print("SECRET_KEY =",os.getenv("SECRET_KEY"))
def get_client():
    return Client(
        os.getenv("API_KEY"),
        os.getenv("SECRET_KEY"),
        testnet = True
        
    )
print("connected successfully")