class Transaction:
    def __init__(self, id):
        self.id = id
        self.locks = set()
        self.phase = "Growing"

    def acquire_lock(self, resource):
        if self.phase == "Growing":
            if resource not in self.locks:
                self.locks.add(resource)
                print(f"Transaction {self.id} acquired lock on resource {resource}.")
            else:
                print(f"Transaction {self.id} already holds lock on resource {resource}.")
        else:
            print(f"Transaction {self.id} cannot acquire lock during Shrinking phase.")

    def release_lock(self, resource):
        if resource in self.locks:
            self.locks.remove(resource)
            print(f"Transaction {self.id} released lock on resource {resource}.")
        else:
            print(f"Transaction {self.id} does not hold lock on resource {resource}.")

    def end_transaction(self):
        self.phase = "Shrinking"
        print(f"Transaction {self.id} entered Shrinking phase.")

    def read_write(self):
        if self.phase == "Growing":
            print(f"Transaction {self.id} performing read/write operations.")
        else:
            print(f"Transaction {self.id} cannot perform read/write operations during Shrinking phase.")


class ResourceManager:
    def __init__(self):
        self.locked_resources = set()

    def acquire_lock(self, resource):
        if resource not in self.locked_resources:
            self.locked_resources.add(resource)
            print(f"Resource {resource} locked.")
            return True
        else:
            print(f"Resource {resource} already locked.")
            return False

    def release_lock(self, resource):
        if resource in self.locked_resources:
            self.locked_resources.remove(resource)
            print(f"Resource {resource} released.")
            return True
        else:
            print(f"Resource {resource} not locked.")
            return False


if __name__ == "__main__":
    rm = ResourceManager()

    t1 = Transaction(1)
    t2 = Transaction(2)

    t1.acquire_lock('A')
    t2.acquire_lock('B')

    rm.acquire_lock('A')
    rm.acquire_lock('B')
    rm.acquire_lock('C')
    rm.release_lock('A')

    t1.release_lock('A')
    t1.end_transaction()
    t1.read_write()

    t2.acquire_lock('A')
    t2.release_lock('B')
    t2.end_transaction()
