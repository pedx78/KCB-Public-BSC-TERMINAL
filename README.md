# KCB-Public A Python base terminal to interact with bep-20 tokens on the binance smart chain

Tools needed:
+ BSC scan API keys
+ Metamask wallet address
+ wallet address private key


This project is a high level terminal to interact with tokens that use pancakeswap


        Functions:                Describtions:
        c:                   returns current connected contract
        ntoken:              (address) function to change the current contract aka add a new token and replace old one
        cinfo:               information on token
        methods:             returns all methods of token
        winfo:               (wallet_address) information of the wallet
        t:                   (from, to, amount(int or "max"), type("manual" or "auto")) transfer tokens between wallets
        buy:                 (buyer, amount, type) buys amount of tokens at the price of the block it enters
        sell:                (sell, amount or "max", type) sells amount of tokens -currently undere development-
        snipe:                   (buyer, amount, contract_address) snipe fair launches by connecting to to contract and sending a buy at market price 
