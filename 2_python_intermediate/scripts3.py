import argparse

parser = argparse.ArgumentParser(descriptio='searching by key..')
parser.add_argument('snippet', help='part or whole word')

args = parser.parse_args()
snippet = args.snippet.lower()

words = open('pl_PL.dic').readlines()
print([word.strip() for word in words if snippet in word.lower()])