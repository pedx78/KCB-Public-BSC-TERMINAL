# Wallets info dependencies


wallets = {
    "Juan": ["0x4B44c71C34Ecd2f64C1A4223149A2b39Ca113F98", '9e7ba19a2d848ea8c4d3fab25e0edfe57835d01e53ca565d7b207d23d717499c']
}

names =  {
    "0x4B44c71C34Ecd2f64C1A4223149A2b39Ca113F98": "Juan" 
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
