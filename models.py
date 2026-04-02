import datetime as dt
import random as rd

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