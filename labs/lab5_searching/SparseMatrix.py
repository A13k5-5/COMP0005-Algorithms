class Matrix:
    def __init__(self):
        self.rows = {}
        self.width = 0
        self.height = 0

    def add_val(self, val, row, col):
        if row not in self.rows.keys():
            self.rows[row] = {col: val}
        else:
            self.rows[row][col] = val
        if row > self.height:
            self.height = row
        if col > self.width:
            self.width = col

    def get(self, row, col):
        if row not in self.rows.keys() or col not in self.rows[row].keys():
            return 0
        return self.rows[row][col]

    def __add__(self, mtrx2):
        if self.height != mtrx2.height and self.width != mtrx2.height:
            raise Exception("Matrices not of same dimension")
        newMtrx = Matrix()


if __name__ == "__main__":
    mtrx = Matrix()
    mtrx.add_val(5, 0, 0)
    mtrx.add_val(5, 0, 1)
    mtrx.add_val(5, 5, 1)
    print(mtrx.rows)
    print(mtrx.get(0, 2))
    print(mtrx.width, mtrx.height)
