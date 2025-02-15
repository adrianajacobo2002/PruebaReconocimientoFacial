import mysql.connector as db
import json

with open('C:/Users/Adriana Jacobo/Desktop/prueba/src/keys.json') as json_file:
    keys = json.load(json_file)

def convertToBinaryData(filename):
    try:
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    except:
        return 0

def write_file(data, path):
    with open(path, 'wb') as file:
        file.write(data)

def registerUser(name, photo):
    id = 0
    inserted = 0

    try:
        con = db.connect(host=keys["host"], user=keys["user"], password=keys["password"], database=keys["database"])
        cursor = con.cursor()
        sql = "INSERT INTO `user`(name, photo) VALUES (%s,%s)"
        pic = convertToBinaryData(photo)

        if pic:
            cursor.execute(sql, (name, pic))
            con.commit()
            inserted = cursor.rowcount
            id = cursor.lastrowid

    except db.Error as e:
        print(f"Failed inserting image: {e}")

    finally:
        if con.is_connected():
            cursor.close()
            con.close()

    return {"id": id, "affected":inserted}

def getUser(name, path):
    id = 0
    rows = 0

    try:
        con = db.connect(host=keys["host"], user=keys["user"], password=keys["password"], database=keys["database"])
        cursor = con.cursor()
        sql = "SELECT * FROM `user` WHERE name = %s"

        cursor.execute(sql, (name,))
        recuperados = cursor.fetchall()

        for row in recuperados:
            id = row[0]
            write_file(row[2], path)
        rows = len(recuperados)

    except db.Error as e:
        print(f"Failed to read image: {e}")

    finally:
        if con.is_connected():
            cursor.close()
            con.close()
    return {"id": id, "affected": rows}