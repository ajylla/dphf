from dphf import dphfsum


class CollisionException(Exception):
    pass


class Dpht:

    def __init__(self, max_size):
        self.max_size = max_size
        self.table = [None for i in range(max_size)]

    def __str__(self):
        str = "Index\tValue\n"
        for i, v in enumerate(self.table):
            if v is None:
                v = "-"
            str += f"{i}\t\t{v}\n"
        return str

    def append(self, string, overwrite=False):
        idx = dphfsum(string) % self.max_size
        stored = self.table[idx]
        if stored is None or overwrite:
            self.table[idx] = string
        else:
            raise CollisionException(f"Table[{idx}] already stores {stored}. Pass overwrite=True to overwrite.")

    def delete(self, idx):
        if self.table[idx] is None:
            print("Nothing to delete.")
        else:
            self.table[idx] = None

    def lookup(self, string):
        idx = dphfsum(string) % self.max_size
        value = self.table[idx]
        if value is None:
            print(f"{string} not in table.")
            return None
        else:
            return idx


if __name__ == "__main__":
    size = 10
    table = Dpht(size)
    names = ["Aleksi", "Aleks", "Alex", "Aleksandr", "Alexander"]
    for name in names:
        table.append(name)

    print(table)

    lookup_name = "Aleksi"
    index = table.lookup(lookup_name)
    print(f"{lookup_name} found at index {index}.")
