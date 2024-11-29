import sqlite3

def init_db():
    conn =sqlite3.connect("traffic.db")
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS packets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    src_ip TEXT,
                    dst_ip TEXT,
                    protocol TEXT,
                    payload TEXT
        )
    ''')
    conn.commit()
    return conn

def log_packet(src_ip,dst_ip,protocol,payload):
    conn = init_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO packets (src_ip, dst_ip, protocol, payload)VALUES (?,?,?,?)',
                   (src_ip, dst_ip, protocol, payload))
    conn.commit()

