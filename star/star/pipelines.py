# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import  mysql.connector

class StarPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database='scrappy',
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS  star_tb """)
        self.curr.execute("""create table star_tb (
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        links text,
        title text
        )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item


    def store_db(self, item):
        titlex=str(item['title'][0])
        link=str(item['links'][0])
        if str(link) != "":
            y = link.split("&")
            x = str(y[1]).split("=")
            print("Value to be inserted is ===> ", str(x[1]))
            w = str(x[1])
        sql = "INSERT INTO star_tb (links, title) VALUES (%s, %s)"
        val = (w, titlex)
        self.curr.execute(sql,val)
        self.conn.commit()


    def __del__(self):
        print("closed")
        self.conn.close()
