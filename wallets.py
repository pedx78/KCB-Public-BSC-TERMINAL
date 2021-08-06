# Wallets info dependencies


wallets = {
    "test_wallet": [wallet_address, wallet_private_key]
}

names =  {
    "wallet_address": test_wallet
}


def wallet_info(name, option):
    if name in wallets and option == "addr":
        return wallets[name][0]
    if name in wallets and option == "key":
        return wallets[name][1]
    else:
        return "No info on wallet, check spelling"

def wallet_info_all(name):
    if name in wallets:
        return [wallets[name][0], wallets[name][1]]
    else:
        return "No info on wallet, check spelling"


def wallet_addr_name(name):
    if name in names:
        return names[name]
    else:
        return "No info on wallet"

#print(wallet_addr_name('0x4B44c71C34Ecd2f64C1A4223149A2b39Ca113F98'))
