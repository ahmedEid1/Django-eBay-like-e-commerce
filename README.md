- create the watchList :
    - it is a cart so look for the cart built in the book
## My Tasks
- Django Admin Interface: 
  - Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.
![admin interface](readme_media/admin.PNG)
-----
- Models: 
  - Your application should have at least three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.
  - 
  - ##### my models :
    - Category (name)
    - Listing (owner, title, description, starting_bid, image, category)
    - Bid (owner, listing, price)
    - Comment (author, listing, content, date_created)
----