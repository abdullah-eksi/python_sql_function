
## SqLite Python Functions

## Setup

1. Install the required dependencies:

```bash
pip install sqlite3
```

2. Create a connection to your SQLite database:

```python
import sqlite3 as lt

connection = lt.connect("data.db")
```

## Usage

### Listing Data

```python
# Example usage of listele function
data = listele("table_name")
print(data)
```

### Inserting Data

```python
columns_values = [("column1", value1), ("column2", value2)]
ekle("table_name", columns_values)
```

### Updating Data

```python
columns_values = [("column1", new_value1), ("column2", new_value2)]
guncelle("table_name", columns_values, "WHERE condition")
```

### Deleting Data

```python
delete("table_name", "WHERE condition")
```



