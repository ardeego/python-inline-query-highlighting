# Python Inline Kusto/SQL Syntax Highlighting

Adds support for inline query language syntax highlighting for Python multiline SQL and Kusto strings in Visual Studio Code.

## Installation

Install `python-inline-query-highlighting` from extensions (`ctrl + shift + x` or `cmd + shift + x` on mac).

Also available on [marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=ardeego.python-inline-query-highlighting)

## Usage

### Kusto

Insert `//beginkusto`, or `//begin-kusto` at the beginning of the part of the string you would like highlighted and `//endkusto`, or `//end-kusto` at the end of the highlighted section.

### SQL

Insert `--sql`, `--beginsql`, or `--begin-sql` at the beginning of the part of the string you would like highlighted and a semicolon, `--endsql`, or `--end-sql` at the end of the highlighted section.

## Requirements

- Visual Studio Code v1.32.0 recommended
- Comments at beginning and end of highlighted section in the string (see Usage section).

## Community
- 2020-05-18 forked from [python-string-sql](https://github.com/ptweir/python-string-sql)