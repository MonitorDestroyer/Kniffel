from output import constants

class Row:
    def __init__(self, n_columns: int, data: list[str]) -> None:
        self.n_columns: int = n_columns
        self.data: list[str] = data
        data_length: int = len(data)
        if(data_length < n_columns):
            for __ in range(n_columns - data_length):
                self.data.append("?")
    
    def append_data(self):
        self.data.append("?")

class Column:
    def __init__(self, length: int, title: str, alignment: int) -> None:
        self.length = length
        self.title = title
        self.alignment = alignment

class Table:
    def __init__(self, title: str) -> None:
        self.columns: list[Column] = []
        self.rows: list[Row] = []
        self.title: str = title

    def get_full_length(self) -> int:
        length = 1
        for column in self.columns:
            length += column.length + 1
        return length
    
    def add_column(self, length: int, title: str, alignment: int):
        self.columns.append(Column(length, title, alignment))

    def add_row(self, data: list[str]):
        self.rows.append(Row(len(self.columns), data))

    def print_table(self) -> None:
        full_length: int = self.get_full_length()
        print(string_center(self.title, full_length))
        print(string_bar(full_length))
        header_string = "|"
        for column in self.columns:
            header_string += string_center(column.title, column.length)
            header_string += "|"
        print(header_string)
        print(string_bar(full_length))
        for row in self.rows:
            row_string = "|"
            for i in range(len(self.columns)):
                if(self.columns[i].alignment == constants.ALIGN_LEFT):
                    row_string += string_resize(row.data[i], self.columns[i].length)
                elif(self.columns[i].alignment == constants.ALIGN_CENTER):
                    row_string += string_center(row.data[i], self.columns[i].length)
                row_string += "|"
            print(row_string)
            print(string_bar(full_length))

def string_resize(string: str, size: int) -> str:
    string_length: int = len(string)
    if(string_length <= size):
        for __ in range(size - string_length):
            string += " "
    else:
        for __ in range(string_length - size):
            string = string[:-1]
    return string

def string_center(string: str, size: int) -> str:
    string_length: int = len(string)
    if(string_length < size):
        left_over: int = size - string_length
        left_side: int = 0
        right_side: int = 0
        if(left_over % 2 == 0):
            left_side = right_side = round(left_over / 2)
        else:
            left_side = round(left_over / 2 + 0.1) - 1
            right_side = round(left_over / 2 + 0.1)
        return_string = ""
        for __ in range(left_side):
            return_string += " "
        return_string += string
        for __ in range(right_side):
            return_string += " "
        string = return_string
    return string

def string_bar(size: int) -> str:
    return_string = ""
    for __ in range(size):
        return_string += "-"
    return return_string

