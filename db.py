import psycopg2

# Esta conexión se utiliza para consultas más especializadas
def get_connection():
    conn = psycopg2.connect(
        host="localhost",  # Cambia esto a la dirección de tu servidor PostgreSQL
        database="db_ejemplo",  # Cambia esto al nombre de tu base de datos
        user="postgres",  # Cambia esto al usuario de PostgreSQL
        password="root"  # Cambia esto a tu contraseña de PostgreSQL
    )
    return conn

def insert_record(name, pet):
    conn = get_connection()
    cursor = conn.cursor()
    insert_query = "INSERT INTO mytable (name, pet) VALUES (%s, %s)"
    cursor.execute(insert_query, (name, pet))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_records():
    conn = get_connection()
    cursor = conn.cursor()
    select_query = "SELECT * FROM mytable"
    cursor.execute(select_query)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

def delete_record_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    delete_query = "DELETE FROM mytable WHERE name = %s"
    cursor.execute(delete_query, (name,))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected

def update_record(name, new_name, new_pet):
    conn = get_connection()
    cursor = conn.cursor()
    update_query = "UPDATE mytable SET name = %s, pet = %s WHERE name = %s"
    cursor.execute(update_query, (new_name, new_pet, name))
    conn.commit()
    rows_affected = cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected
