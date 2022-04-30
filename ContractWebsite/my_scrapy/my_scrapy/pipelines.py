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
						date,
						notice_number ,
						tender_name ,
						procedure_state ,
						contract_type ,
						type_of_procurement ,
						estimated_value	
						)""")

    # store items to databases.
    def process_item(self, item, spider):
        self.putitemsintable(item)
        return item

    def putitemsintable(self, item):
        # extracting item and adding to table using SQL commands.
        self.curr.execute("""insert into noticetable values (?,?,?,?,?,?,?,?)""", (
            item['Notice'][0],
            item['date'][0],
            item['notice_number'][0],
            item['tender_name'][0],
            item['procedure_state'][0],
            item['contract_type'][0],
            item['type_of_procurement'][0],
            item['estimated_value'][0],

        ))
        # new_notice=N(
        #     date=item['date'][0],
        #     notice_number= item['notice_number'][0],
        #     tender_name=item['tender_name'][0],
        #     procedure_state=item['procedure_state'][0],
        #     contract_type=item['contract_type'][0],
        #     type_of_procurement=item['type_of_procurement'][0],
        #     estimated_value=item['estimated_value'][0],
        # )
        # new_notice.save()

        self.conn.commit()  # closing the connection.

        # new_phrase = Phrase(phrase=say_form.cleaned_data['phrase'])
        # new_phrase.save()





