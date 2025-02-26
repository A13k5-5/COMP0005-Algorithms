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
        if row >= self.height:
            self.height = row + 1
        if col >= self.width:
            self.width = col + 1

    def __str__(self):
        rows = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if y in self.rows and x in self.rows[y]:
                    row.append(str(self.rows[y][x]))
                else:
                    row.append("0")
            rows.append(" ".join(row))
        return "\n".join(rows)

    def get(self, row, col):
        if row >= self.height or col >= self.width:
            raise Exception("Out of range")
        if row not in self.rows.keys() or col not in self.rows[row].keys():
            return 0
        return self.rows[row][col]

    def __add__(self, mtrx2):
        if self.height != mtrx2.height or self.width != mtrx2.width:
            raise Exception("Matrices not of same dimension")

        result = Matrix()
        for row in self.rows:
            for col in self.rows[row]:
                result.add_val(self.rows[row][col], row, col)

        for row in mtrx2.rows:
            for col in mtrx2.rows[row]:
                current = result.get(row, col)
                result.add_val(current + mtrx2.rows[row][col], row, col)
        return result

    def __mul__(self, mtrx2):
        if self.height != mtrx2.width:
            raise Exception("Cant multiply these two")

        result = Matrix()
        for y in range(self.height):
            for x in range(mtrx2.width):
                newEntry = 0
                for i in range(mtrx2.height):
                    newEntry += self.get(y, i) * mtrx2.get(i, x)
                result.add_val(newEntry, y, x)
        return result


if __name__ == "__main__":
    mtrx = Matrix()
    mtrx.add_val(1, 0, 0)
    mtrx.add_val(2, 0, 1)
    mtrx.add_val(3, 0, 2)
    mtrx.add_val(4, 1, 0)
    mtrx.add_val(5, 1, 1)
    mtrx.add_val(6, 1, 2)
    print(mtrx)

    mtrx2 = Matrix()
    mtrx2.add_val(1, 0, 0)
    mtrx2.add_val(3, 0, 1)
    mtrx2.add_val(2, 1, 0)
    mtrx2.add_val(4, 1, 1)
    mtrx2.add_val(8, 2, 0)
    mtrx2.add_val(2, 2, 1)
    print()
    print(mtrx2)
    # print()
    # print(mtrx + mtrx2)

    print()
    print(mtrx * mtrx2)
