import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="dataeng_practice",
    user="abhishek",
    password="password123"
)

print ("Connected to postgre")
