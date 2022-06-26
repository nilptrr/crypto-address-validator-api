# Cryptro address validator API
[API for Cryptro address validator](https://github.com/null-po1nter/crypto-address-validator)

## Supported currencies
| Currency      | Symbol | Mainnet | Testnet    | Note                                                                                                      |
|:-------------:| ------ | ------- | ---------- | ---------------------------------------------------------------------------------------------         |
| Bitcoin       | BTC    | +       | +          | P2PKH (Legacy Adresses), P2SH (Pay to Script Hash), P2WPKH (Native SegWit), P2TR (Taproot) address formats    |
| Cosmos        | ATOM   | +       | -          |                                                                                                       |
| Binance Coin  | BNB    | +       | +          |                                                                                                       |
| Aion          | AION   | +       | +          |                                                                                                       |
| EOS           | EOS    | +       | +          |                                                                                                       |
| IOST          | IOST   | +       | +          |                                                                                                       |
| IOTA          | MIOTA  | +       | Devnet     | Chrysalis, Legacy address formats                                                                                                                                                 |

## Installation and run
```
python3 -m venv venv
(venv) pip install -r requirements.txt
cd src
uvicorn --reload main:app
```

## Usage
symbol: Currency symbol, e.g. 'btc' or 'atom'.

address: Currency address to validate.

Example:
```
/validate?symbol=btc&address=1Kd7V9gcKrDWADMo4Dr7SU9bKCY4mvcz9o
```

## License
The Unlicense. See the LICENSE file for details.