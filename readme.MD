# Simple Banking System

This is a basic banking system implemented in Python, allowing users to perform deposit, withdrawal, check balance, and view transaction history functionalities.

## Instructions

1. Run the Python script in an environment that supports Python.
2. Follow the on-screen instructions to navigate through the banking functionalities.

## Features

- **Deposit**: Allows users to deposit funds into their account.
- **Withdrawal**: Permits users to withdraw funds, considering balance and withdrawal limits.
- **Check Balance**: Provides users with their current account balance and transaction history.
- **Exit**: Allows users to exit the system.

## Usage

1. Upon running the script, a menu is displayed presenting options for actions.
2. Select an option by entering the corresponding number:
    - `[1]` Deposit
    - `[2]` Withdraw
    - `[3]` View Transaction History
    - `[4]` Exit

## Code Overview

- `menu`: Displays the available options.
- `saldo`: Variable to store the account balance.
- `limite`: Maximum withdrawal limit.
- `extrato`: Variable to store transaction history.
- `numero_saques`: Counter for the number of withdrawals made.
- `LIMITE_SAQUES`: Constant defining the maximum number of withdrawals allowed.
- `depositos`: List to store deposit transactions.
- `saques`: List to store withdrawal transactions.
- The code continuously runs in a loop, allowing users to perform banking operations until they choose to exit.

## Disclaimer

This code is for educational purposes and represents a simplistic banking system. It does not incorporate robust security measures or real banking functionalities and should not be used for actual financial transactions.


