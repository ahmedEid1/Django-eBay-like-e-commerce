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
    - Listing (owner, title, description, starting_bid, image, category, active)
    - Bid (owner, listing, price)
    - Comment (author, listing, content, date_created)
----
- Create Listing: 
  - Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
![create form](readme_media/listing_create_form.PNG)

---
- Active Listings Page: 
  - The default route of your web application should let users view all the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).
![listings](readme_media/listings.PNG)
    
---
