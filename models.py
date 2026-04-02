import datetime as dt
import random as rd
import os
from dotenv import load_dotenv

load_dotenv()


class Account:
    def __init__(self, name: str, balance: float, id: int):
        self.id = id
        self.name = name
        self.pin = self.generate_pin()
        self.balance = balance
        self.blocked = False
        self.actions = []


    # def generate_id():
    #     pass

    def generate_pin(self):
        return rd.randint(1000, 9999)

    def check_pin(self, user_input: int):
        return user_input == self.pin

    def withdraw(self, amount: float, input_pin: int, action_id: int):
        if self.check_pin(input_pin) and amount > 0.0 and amount < self.balance:
            self.balance -= amount
            self.record_action(action_id, dt.datetime.now(),amount,"withdraw")
            return "succses"
        else:
            return "failed"

    def transaction_out(self, amount: float, input_pin: int, action_id: int):
        return self.withdraw(amount, input_pin, action_id)

    def deposit(self, amount: float, input_pin: int, action_id: int):
        if self.check_pin(input_pin) and amount > 0.0:
            self.balance += amount
            self.record_action(action_id, dt.datetime.now(),amount,"deposit")
            return "succses"
        else:
            return "failed"

    def transaction_in(self, amount: float, input_pin: int, action_id: int):
        return self.deposit(amount, input_pin, action_id)

    def change_pin(self, old_pin: int, new_pin: int):
        if self.check_pin(old_pin):
            self.pin = new_pin
            return "succses"
        else:
            return "failed"

    # def block_account(self):
    #     self.blocked = True

    # def unblock_account(self):
    #     self.blocked = False

    def record_action(self, action_id: int, date_time: dt.datetime, amount: float, type: str):
        if type == "withdraw" or type == "deposit" or type == "transaction_in" or type == "transaction_out":
            self.actions.append({
                "action_id": action_id,
                "time": date_time,
                "amount": amount,
                "type": type
            })

    def actions_to_dictionary(self):
        actions_dictionary = {}
        for action in self.actions:
            key = action["action_id"]
            actions_dictionary[key] = {
                "time": str(action["time"]),
                "amount": action["amount"],
                "type": action["type"]
                }
        return actions_dictionary


class Bank(Account):
    accounts = {}

    def __init__(self, username, balance=0):
        super().__init__(self.create_account_id(), username, balance)
        Bank.accounts[self.account_id] = self

    @classmethod
    def create_account_id(cls):
        account_id = rd.randint(10000, 99999)
        while account_id in cls.accounts:
            account_id = rd.randint(10000, 99999)
        return account_id

    @classmethod
    def is_account_created(cls, account_id):
        return account_id in cls.accounts

    @classmethod
    def list_all_accounts(cls):
        for account_id, account in cls.accounts.items():
            print(f"ID: {account_id} | Username: {account.username} | Balance: {account.balance} | Active: {account.is_active} | PIN: {account.pin}")

    @staticmethod
    def is_admin_pin(entered_password):
        return entered_password == os.getenv("ADMIN_SECRET_PASS")

    @classmethod
    def transaction_to_from_accounts(cls, sender_id, receiver_id, amount):
        if not cls.is_account_created(sender_id):
            return False, "sender account not found"
        if not cls.is_account_created(receiver_id):
            return False, "receiver account not found"
        sender = cls.accounts[sender_id]
        if sender.balance < amount:
            return False, "insufficient balance"
        cls.accounts[sender_id].balance -= amount
        cls.accounts[receiver_id].balance += amount
        return True

    @classmethod
    def log_in_account(cls, account_id, pin):
        if not cls.is_account_created(account_id):
            return False, "account not created"
        account = cls.accounts[account_id]
        if not account.is_active:
            return False, "account suspend"
        if pin == account.pin:
            return True
        return False, "incorrect PIN"