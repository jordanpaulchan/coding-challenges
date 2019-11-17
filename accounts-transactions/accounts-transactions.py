from bisect import bisect_right


class Account():
    def __init__(self, account_id, ts, value):
        self.account_id = account_id
        self.timestamps = [ts]
        self.balances = [value]
        self.values = [value]


class Accounts:
    def __init__(self):
        self.accounts = {}

    def credit(self, account_id, ts, value):
        if account_id not in self.accounts:
            self.accounts.setdefault(
                account_id, Account(account_id, ts, value))
        else:
            account = self.accounts[account_id]
            account.timestamps.append(ts)
            account.balances.append(account.balances[-1] + value)
            account.values.append(value)

    def debit(self, account_id, ts, value):
        if account_id not in self.accounts:
            self.accounts.setdefault(
                account_id, Account(account_id, ts, -value))
        else:
            account = self.accounts[account_id]
            account.timestamps.append(ts)
            account.balances.append(account.balances[-1] - value)
            account.values.append(-value)

    def current(self, account_id):
        if account_id not in self.accounts:
            return None
        account = self.accounts[account_id]
        return account.balances[-1]

    def balance_change(self, account_id, start_ts, end_ts):
        if account_id not in self.accounts:
            return None
        account = self.accounts[account_id]
        start_idx = bisect_right(account.timestamps, start_ts)
        end_idx = bisect_right(account.timestamps, end_ts)

        return account.balances[end_idx - 1] - account.balances[start_idx - 1]


accounts = Accounts()
accounts.credit(1, 1, 100)
accounts.debit(1, 3, 50)
accounts.credit(1, 5, 20)
accounts.debit(1, 7, 10)
print(accounts.current(1))
print(accounts.balance_change(1, 2, 6))
print(accounts.balance_change(1, 3, 5))
