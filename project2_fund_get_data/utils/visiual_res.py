from typing import List

from rich import box
from rich.console import Console
from rich.table import Table


def visiual_single_fund_data(data: List[str]):
    console = Console()
    console.print(*data)


def visiual_all_fund_data(header, data: List[List[str]]):
    console = Console()
    table = Table(show_footer=False)

    # data
    for i in header:
        table.add_column(i)
    # table.add_column("UtilRate", justify="right")

    for i in data:
        table.add_row(*i)

    # table.title = ":rainbow:     :rainbow:"

    # table style
    # table.title_style = "none"
    # table.caption_justify = "right"
    # table.columns[0].style = "cyan"
    # table.columns[0].header_style = "bold cyan"
    # table.columns[1].style = "green"
    # table.columns[1].header_style = "bold green"
    # table.columns[2].style = "blue"
    # table.columns[2].header_style = "bold blue"
    # table.columns[3].style = "magenta"
    # table.columns[3].header_style = "bold magenta"

    # box line
    table.box = box.SIMPLE
    console.print(table)
