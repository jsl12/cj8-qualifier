from typing import Any, List, Optional

class Table:
    mid_vert = '│'
    mid_hor = '─'
    top_left = '┌'
    top_mid = '┬'
    top_right = '┐'
    mid_left = '├'
    middle = '┼'
    mid_right = '┤'
    bottom_left = '└'
    bottom_mid = '┴'
    bottom_right = '┘'


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    col_widths = column_widths(rows, labels)
    num_cols = len(rows[0])
    res = Table.top_left + Table.top_mid.join(
        (Table.mid_hor * (col_widths[i] + 2)) for i in range(num_cols)) + Table.top_right + '\n'

    if labels is not None:
        res += create_row(labels, col_widths, centered)
        res += Table.mid_left + Table.middle.join(
            (Table.mid_hor * (col_widths[i] + 2)) for i in range(num_cols)) + Table.mid_right + '\n'

    for row in rows:
        res += create_row(row, col_widths, centered)

    res += Table.bottom_left + Table.bottom_mid.join(
        (Table.mid_hor * (col_widths[i] + 2)) for i in range(num_cols)) + Table.bottom_right + '\n'

    return res

def column_widths(rows: List[List[Any]], labels: Optional[List[Any]] = None) -> List[int]:
    res = rows.copy()
    if labels is not None:
        res.append(labels)
    col_widths = [
        max(len(str(row[i])) for row in res)
        for i in range(len(res[0]))
    ]
    return col_widths

def create_row(row: List[Any], col_widths: List[int], centered: bool = False) -> str:
    convert = lambda d, w: f' {str(d).ljust(w + 1)}' if not centered else f'{str(d).center(w + 2)}'
    return Table.mid_vert + \
           Table.mid_vert.join(convert(data, width) for data, width in zip(row, col_widths)) + \
           Table.mid_vert + '\n'
