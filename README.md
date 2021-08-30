## BLOG-POST APP 

### Description
> This is my personal blogging web application.
> I can create and share opinions.Authenticated users can read and comment on the blogs I have created.
> The application also displays random quotes every time a user refreshes the page. 

## Author

👤 **Author**
- Amukozo berit Mwashe

- GitHub: [@amukozo-berit](https://github.com/amukozoberit)

## Technologies Used

- HTML
- CSS
- PYTHON `3.9`
- PYTHON SHELL 
- FLASK
- FLASK_BOOTSTRAP
- HEROKU

### User Stories
As a user I would like to;

- view the blogs on the site.
- comment on the blogs.
- view the most recent blogs.
- have an email alert when a new post is made by joining a subscription.
- see random quotes on the site 

As a writer I would like to;
- sign in to the blog
- create a blog from the application
- delete comments that I find insulting or degrading.
- update or delete blogs I have created.

## Specifications:
These are the actions the user will do, inputs required and their outputs on the page. 

  | Action    | Input                                      | Output                        |
  | ----------|:-------------                              | :------                       |
  | Load page | On page load                               | Displays the homepage         |
  | Sign up   | email, username, password, confirm password| Redirected to login page      |
  | Login     | username, password                         | Redirect to homepage          |
  | Select Comment| a comment                              | Your comment displayed        |
  |           |                                            |                               |
## Live Demo

[Live Demo Link]( --)


### Installation Process

- Clone the repository using the link below

```
$ git clone https://github.com/Koech-code/My-blogPost.git

```

- Create a directory and install the requirements

  ```
  cd blog-post
  pip install -r requirements.txt
  ```
- Export configurations
  ```
  Secrete Key
  Mail_username
  Mail_password
  ```
- Run the application using;
  ```
  python3.6 manage.py server
  ```
- Test it if its working using;
  ```
  python3.9 manage.py test
  ```
- Open the application on your browser , preferably `chrome` using port `127.0.0.1:5000`


## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- I would like to acknowledge Moringa school for giving me this opportunity to learn software development.
- Appreciations to  my TM `Nancy Umutoniwase` for the support she gives me.

## 📝 License

This project is [MIT](LICENCE.md) licensed.