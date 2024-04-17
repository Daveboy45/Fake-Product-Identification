from web3 import Web3
from sympy import false
# Initialize Web3 with your desired provider
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))
from web3 import Web3

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

# Load the contract ABI and address
contract_address = '0xAA8cCA214D7D0B21BE1e9A483671eca823B0eE2F'
contract_abi = [
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "brand",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "manufacturerId",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "serialNumber",
				"type": "uint256"
			}
		],
		"name": "ProductRegistered",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "brand",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "manufacturerId",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "serialNumber",
				"type": "uint256"
			}
		],
		"name": "registerProduct",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "productIdCounter",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "products",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "brand",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "price",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "manufacturerId",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "serialNumber",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "hash",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "exists",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)
 # Replace with your contract address

