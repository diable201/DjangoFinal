# DjangoFinal

Your task is to create a part of the Online Book Store.

1. Authorization
  * a. Implement extending from Base Class
  * b. JWT
  * c. UserProfile
  * d. roles: [SuperAdmin, Guest]

2. You have the following classes:
   a. **BookJournalBase** - abstract class
   1. name
   2. price 
   3. description
   4. created_at
   
   b. **Book** extends from **BookJournalBase** 
   1. num_pages
   2. genre
   
   c. **Journal** extends from **BookJournalBase** 
   1. type [Bullet, Food, Travel, Sport]
   2. publisher
   
3. Implement endpoints using ViewSets:
   1. Auth Register
   /auth/login
   
   2. Core
      3. books/ - CRUD, only Admins can modify objects
      4. journals/ - CRUD, only Admins can modify objects
