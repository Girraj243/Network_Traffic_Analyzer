import sqlite3
import matplotlib.pyplot as plot

def visualize_protocol():
    conn = sqlite3.connect('traffic.db')
    cursor = conn.cursor()
    cursor.execute("SELECT protocol,COUNT(*) FROM packets GROUP BY protocol")
    data = cursor.fetchall()

    protocols = [row[0] for row in data]
    counts =[row[1] for row in data]

    plot.pie(counts,labels=protocols, autopct="%1.1f%%")
    plot.title("Protocol Distribution")
    plot.show()

    conn.close()