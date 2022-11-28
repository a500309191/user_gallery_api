# user_gallery_api
## Test assignment for a python developer vacancy. 
The app is a user gallery api with authorization and CRUD manipulations.


#### The app is written using DJANGO, DJANGO REST FRAMEWORK.


#### WEB API ROUTING TABLE:

| route:  | HTTP methods: | permissions: | action: |
| ------------- |-------------|:-------------:|-------------|
| images/ | GET | un/authenticated | getting a list of all images |
| myimages/ | GET | authenticated | getting a list of authenticated user images |
| image/create/ | POST | authenticated | create image for authenticated user |
| image/<<id:int>>/ | GET, PUT, DELETE | authenticated | read, update, delete manipulations for image of authenticated user |
| imagesdelete/ | DELETE | superuser | delete all images from db |
| user/create/ | POST | un/authenticated | create new user |
| user/ | GET | authenticated | get details for authenticated user |