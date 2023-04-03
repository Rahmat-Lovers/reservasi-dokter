from web3 import Web3
import json, os

w3 = Web3(Web3.HTTPProvider(os.environ['JSON_RPC_URL']))

contract = w3.eth.contract(
    address = json.loads(open('../address.json').read())['address'],
    abi = json.loads(open('../abi.json').read())
)