# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class MyScrapyPipeline:
#     def process_item(self, item, spider):
#         return item



import sqlite3


class MyScrapyPipeline(object):

    # init method to initialize the database and
    # create connection and tables
    def __init__(self):
        # Creating connection to database
        self.create_conn()

        # calling method to create table
        self.create_table()

    # create connection method to create database
    # or use database to store scraped data
    def create_conn(self):
        # connecting to database.
        #self.conn = sqlite3.connect("mydata.db")
        self.conn = sqlite3.connect("test_notices")

        # collecting reference to cursor of connection
        self.curr = self.conn.cursor()

    # Create table method using SQL commands to create table
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS noticetable""")
        self.curr.execute("""create table noticetable(
						Notice text,
						Name text
						
						)""")

    # store items to databases.
    def process_item(self, item, spider):
        self.putitemsintable(item)
        return item

    def putitemsintable(self, item):
        # extracting item and adding to table using SQL commands.
        self.curr.execute("""insert into noticetable values (?,?)""", (
            item['Notice'][0],
            item['Name'][0],

        ))

        self.conn.commit()  # closing the connection.





