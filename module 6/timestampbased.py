class Transaction:
    def __init__(self, id, timestamp):
        self.id = id
        self.timestamp = timestamp

    def get_id(self):
        return self.id

    def get_timestamp(self):
        return self.timestamp


class TimestampConcurrencyControl:
    def __init__(self):
        self.active_transactions = []

    def start_transaction(self, transaction):
        self.active_transactions.append(transaction)
        print(f"Transaction {transaction.get_id()} started at timestamp {transaction.get_timestamp()}.")

    def end_transaction(self, transaction):
        self.active_transactions.remove(transaction)
        print(f"Transaction {transaction.get_id()} ended at timestamp {transaction.get_timestamp()}.")

    def check_conflict(self, transaction):
        for active_transaction in self.active_transactions:
            if active_transaction.get_timestamp() > transaction.get_timestamp():
                print(f"Conflict detected between Transaction {transaction.get_id()} and Transaction {active_transaction.get_id()}.")
                return True
        return False


if __name__ == "__main__":
    concurrency_control = TimestampConcurrencyControl()

    t1 = Transaction(1, 1)
    t2 = Transaction(2, 2)
    t3 = Transaction(3, 3)
    t4 = Transaction(4, 4)
    t5 = Transaction(5, 5)

    concurrency_control.start_transaction(t1)
    concurrency_control.start_transaction(t2)
    concurrency_control.start_transaction(t3)

    if not concurrency_control.check_conflict(t4):
        concurrency_control.start_transaction(t4)

    if not concurrency_control.check_conflict(t5):
        concurrency_control.start_transaction(t5)

    concurrency_control.end_transaction(t1)
    concurrency_control.end_transaction(t2)

    if not concurrency_control.check_conflict(t5):
        concurrency_control.start_transaction(t5)

    concurrency_control.end_transaction(t3)
    concurrency_control.end_transaction(t4)
    concurrency_control.end_transaction(t5)
