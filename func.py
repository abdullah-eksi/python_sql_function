connection = lt.connect("data.db")

def listele(table_name, where=None):
    cursor = connection.cursor()
    
    
    sorgu = f"SELECT * FROM {table_name}"
    if where:
        sorgu += f" {where}"
    
    
    cursor.execute(sorgu)
    
 
    results = cursor.fetchall()
    
    return results


def ekle(table_name, columns_values):
    cursor = connection.cursor()

  
    columns = [item[0] for item in columns_values]
    values = [item[1] for item in columns_values]


    columns_str = ', '.join(columns)
    placeholders = ', '.join(['?' for _ in values])
    
    sorgu = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
    

    cursor.execute(sorgu, values)
    

    connection.commit()
    
    
def guncelle(table_name, columns_values, where):
    cursor = connection.cursor()
    
    columns = [item[0] for item in columns_values]
    values = [item[1] for item in columns_values]


    set_clause = ', '.join([f"{col} = ?" for col in columns])
    
    sorgu = f"UPDATE {table_name} SET {set_clause} {where}"
  
    cursor.execute(sorgu, values)
    

    connection.commit()    
    
def delete(table_name, where):
    cursor = connection.cursor()
    sorgu = f"DELETE FROM {table_name} WHERE {where}"
  
    cursor.execute(sorgu)
    
    connection.commit()    
