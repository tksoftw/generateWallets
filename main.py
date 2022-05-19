
import eth_account
import secrets

ethPrivateKey = "0x" + secrets.token_hex(32)
ethAccountObject = eth_account.Account.from_key(ethPrivateKey)
ethPublicKey = ethAccountObject.address

print(f"Ethereum Public Key: {ethPublicKey}")
print(f"Ethereum Private Key: {ethPrivateKey}")

###

import solana.account
from solana.keypair import Keypair

solKeypair = Keypair()
solSeed = solKeypair.from_seed
solAccount = solana.account.Account(solSeed)
solPrivateKey = solAccount.keypair()
solPublicKey = solAccount.public_key()

print(f"Solana Public Key: {solPublicKey}")
print(f"Solana Private Key: {solPrivateKey.decode('utf-8')}")
