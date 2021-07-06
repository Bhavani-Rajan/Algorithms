#!/usr/bin/python

import argparse

def find_max_profit(prices):
    difference = []
    for i in range(len(prices[:-1])):
        #print(i)
        
        
        for j in range(len(prices)):
            if j > i:
                #print(prices[j],prices[i], prices[j] - prices[i])
                difference.append(prices[j] - prices[i] )
    return  max(difference)
    
    

 


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))