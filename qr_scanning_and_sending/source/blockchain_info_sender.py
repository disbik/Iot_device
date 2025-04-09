ABI = [
    {"inputs": [{"internalType": "address", "name": "initialOwner", "type": "address"}], "stateMutability": "nonpayable", "type": "constructor"},
    {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}], "name": "OwnableInvalidOwner", "type": "error"},
    {"inputs": [{"internalType": "address", "name": "account", "type": "address"}], "name": "OwnableUnauthorizedAccount", "type": "error"},
    {"anonymous": False, "inputs": [{"indexed": False, "internalType": "uint256", "name": "labelId", "type": "uint256"}, {"indexed": False, "internalType": "address", "name": "sender", "type": "address"}, {"indexed": False, "internalType": "address", "name": "receiver", "type": "address"}], "name": "LabelCreated", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "internalType": "uint256", "name": "labelId", "type": "uint256"}, {"indexed": False, "internalType": "address", "name": "receiver", "type": "address"}], "name": "LabelReceived", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "internalType": "uint256", "name": "labelId", "type": "uint256"}, {"indexed": False, "internalType": "address", "name": "sender", "type": "address"}], "name": "LabelSent", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": False, "internalType": "uint256", "name": "labelId", "type": "uint256"}, {"indexed": False, "internalType": "address", "name": "by", "type": "address"}], "name": "LabelVoided", "type": "event"},
    {"anonymous": False, "inputs": [{"indexed": True, "internalType": "address", "name": "previousOwner", "type": "address"}, {"indexed": True, "internalType": "address", "name": "newOwner", "type": "address"}], "name": "OwnershipTransferred", "type": "event"},
    {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "authorizedIoTReceivers", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "authorizedIoTSenders", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "authorizedLabelCreators", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "_labelId", "type": "uint256"}, {"internalType": "address", "name": "_sender", "type": "address"}, {"internalType": "address", "name": "_receiver", "type": "address"}], "name": "createLabel", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "deviceInfo", "outputs": [{"internalType": "address", "name": "device", "type": "address"}, {"internalType": "string", "name": "location", "type": "string"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "labelCounter", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "labels", "outputs": [{"internalType": "uint256", "name": "id", "type": "uint256"}, {"internalType": "address", "name": "sender", "type": "address"}, {"internalType": "address", "name": "receiver", "type": "address"}, {"internalType": "bool", "name": "sent", "type": "bool"}, {"internalType": "bool", "name": "received", "type": "bool"}, {"internalType": "bool", "name": "voided", "type": "bool"}], "stateMutability": "view", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "_labelId", "type": "uint256"}], "name": "markAsReceived", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "_labelId", "type": "uint256"}], "name": "markAsSent", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [], "name": "owner", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "renounceOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "_device", "type": "address"}, {"internalType": "string", "name": "_location", "type": "string"}], "name": "setDeviceInfo", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "_account", "type": "address"}, {"internalType": "bool", "name": "_asSender", "type": "bool"}, {"internalType": "bool", "name": "_asReceiver", "type": "bool"}, {"internalType": "bool", "name": "_status", "type": "bool"}], "name": "setIoTAuthorization", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "_account", "type": "address"}, {"internalType": "bool", "name": "_status", "type": "bool"}], "name": "setLabelCreatorAuthorization", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}], "name": "transferOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function"},
    {"inputs": [{"internalType": "uint256", "name": "_labelId", "type": "uint256"}], "name": "voidLabel", "outputs": [], "stateMutability": "nonpayable", "type": "function"}
]

def create_trans_contract(info, contract_address, sender_address, w3):
    contract = w3.eth.contract(address=contract_address, abi=ABI)
    nonce = w3.eth.get_transaction_count(sender_address)
    tx = contract.functions.markAsSent(info).build_transaction({
        'chainId': w3.eth.chain_id,
        'gasPrice': w3.eth.gas_price,
        'from': sender_address,
        'nonce': nonce,
    })
    tx['gas'] = w3.eth.estimate_gas(tx)
    return tx

def send_transaction(transaction, private_key, w3) -> None:
    try:
        signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Транзакция подтверждена: {tx_hash.hex()}, {tx_receipt}")
    except Exception as e:
        print(f"Ошибка: {str(e)}")