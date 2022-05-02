# Contract-notices-website
This is simple web application for crawling all tender notices for the current day from http://www.e-licitatie.ro.
There are two types of users- admins and normal. The normal users first have to make registration and then can crawl from the website, and see the result in JSON format.
All tender notices could be filtered by ID of the notice, by name or by date, if the period is more than one day. Steps for crawling are:
1. Choose time period, which you want to check.
2. Press 'crawl'.
3. See the result.

Admins can also edit all registered users and can delete them, if it needed.All information and permission for each user in the application.

The application is based on DJango framework, DJango REST framework and for crawling is used Scrapy.All crawled data are stored in the datebase of  the application, in 
this case it is sqlite.

(It is not finished, still have to work on crawling condition, for collect right data, for now it is using test website=> https://quotes.toscrape.com .)