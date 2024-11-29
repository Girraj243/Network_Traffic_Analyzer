import sqlite3
def analyzer_traffic():
    conn = sqlite3.connect("traffic.db")
    cursor = conn.cursor()

    cursor.execute("SELECT protocol, COUNT(*) FROM packets GROUP BY protocol")
    for protocol,count in cursor.fetchall():
        print(f"protocol: {protocol},count: {count}")

    cursor.execute("SELECT src_ip, COUNT(*) FROM packets GROUP BY src_ip ORDER BY COUNT(*) DESC LIMIT 5")
    for src_ip,count in cursor.fetchall():
        print(f"src_ip: {src_ip},count: {count}")

    conn.close()