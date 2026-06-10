import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--symbol")
parser.add_argument("--side")
parser.add_argument("--type")
parser.add_argument("--quantity",type=float)
parser.add_argument("--price",type=float)
args = parser.parse_args()
print(args)