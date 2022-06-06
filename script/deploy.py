def run(nre):
    print("Compiling contract…")
    nre.compile(["contracts/contract.cairo"]) # we compile our contract first
    print("Deploying contract…")
    name = str(str_to_felt("ByteScanCairoToken"))
    symbol = str(str_to_felt("BSCT"))
    decimals = "18"
    recipient = "0x01690dc28fb69fc73f0cbd93eedba3861633b67b2f67e3f074b4590713d350fc"
    params = [name, symbol, decimals, "100", "0", recipient]
    address, abi = nre.deploy("ByteScanCairoToken", params, alias="bytescan_token")
    print(f"ABI: {abi},\nContract address: {address}")
# Auxiliary functions
def str_to_felt(text):
    b_text = bytes(text, "ascii")
    return int.from_bytes(b_text, "big")
def uint(a):
    return(a, 0)