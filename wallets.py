#Wallets info dependencies


wallets = {
    "Juan": ["0x4B44c71C34Ecd2f64C1A4223149A2b39Ca113F98", '9e7ba19a2d848ea8c4d3fab25e0edfe57835d01e53ca565d7b207d23d717499c'],
    "Dog": ["0x6d90E0C2d9DA305F8A60262C11975453e09AC962", 'b538903ec978d8bb96ca993ab623a17d3a588178cb8476c1aecdce988f569da0'],
    "Rug": ["0x4aaC16502aC78f91D0cA32ac5667dA4f9bBFD7aD", 'e0c71f8691892c1660fd20f5b3451badd4b988dce54ed58f4e1f7c6b01dd4ae8']

}

names =  {
    "0x4B44c71C34Ecd2f64C1A4223149A2b39Ca113F98": "Juan" ,
    "0x6d90E0C2d9DA305F8A60262C11975453e09AC962": "Dog",
    "0x4aaC16502aC78f91D0cA32ac5667dA4f9bBFD7aD": "Rug",

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

#print(wallet_info("Dog", "addr"))

def wallet_addr_name(name):
    if name in names:
        return names[name]
    else:
        return "No info on wallet"

#print(wallet_addr_name('0x4B44c71C34Ecd2f64C1A4223149A2b39Ca113F98'))
