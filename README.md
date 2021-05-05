# Crypto Trade Data

## Setup

Set environment variables with secrets to `.bash_profile`, `.zshrc`, etc.

```
export COINBASE_API_KEY="xxxxxxxxxxxxxxxx"
export COINBASE_PASSPHRASE="xxxxxxxxxxxxxxxx"
export COINBASE_SECRET="xxxxxxxxxxxxxxxx"
```

Ensure you have python3 installed. The default version of python on mac is 2.7. Run the following command to ensure you have python3.

`which python3`

You should see something like this:

`/usr/bin/python3`

To install dependencies, execute the following command in the repo's main directory

`pip3 install -r requirements.txt`

To run

`python3 <path to repo>/main.py`
