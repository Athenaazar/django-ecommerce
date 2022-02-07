<h1 align="center">
  <a href="https://github.com/Athenaazar/django-ecommerce">
    Stop & Shop
  </a>
</h1>

<div align="center">
  Django Ecommerce Project :<a href="https://athena-ec.herokuapp.com/"> click-here!</a>
  <br />
  <br />
  <a href="https://github.com/Athenaazar/django-ecommerce/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Report a Bug</a>
  ·
  <a href="https://github.com/Athenaazar/django-ecommerce/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Request a Feature</a>
  .
  <a href="https://github.com/Athenaazar/django-ecommerce/discussions">Ask a Question</a>
</div>

<div align="center">
<br />

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![PRs welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/Athenaazar/Paradise-restaurant-html-css/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![made with hearth by Athena](https://img.shields.io/badge/made%20with%20%E2%9D%A4%EF%B8%8F%20by-Athena-red)](https://github.com/Athenaazar)

</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
- [Getting Started](#getting-started)
  - [Quick demo](#quick-demo)
  - [Usage](#usage)
    - [Running this project](#running-this-project)
- [Features & Pages](#features--pages)
  - [Frameworks, Libraries & Resources Used](#frameworks-libraries--resources-used)
    - [Frontend](#frontend)
    - [Backend](#backend)
  - [website consists pages](#website-consists-pages)
  - [Supported Browsers](#supported-browsers)
  - [**Validation**](#validation)
- [Deployment](#deployment)
  - [Stripe (Payments API) setup](#stripe-payments-api-setup)
  - [Remote (Heroku)](#remote-heroku)
- [Contributing](#contributing)
- [License](#license)

</details>

---
## About

<table>
<tr>
<td>

**About Project :**
This is a simple e-commerce website built with Django. It contains the essentials for adding products and capturing payments online.





</td>
</tr>
</table>

## Getting Started
### Quick demo
<a href="https://athena-ec.herokuapp.com/"> click-here!</a>

### Usage

#### Running this project


To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with:

```sh
pip install virtualenv
```
Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project
```sh
virtualenv env
```
That will create a new folder env in your project directory. Next activate it with this command on mac/linux:
```sh
source env/bin/active
```
Then install the project dependencies with
```sh
pip install -r requirements.txt
```
Now you can run the project with this command
```sh
python manage.py runserver
```
**Note** if you want payments to work you will need to enter your own Stripe API keys into the `settings.py` file in the core folder.







## Features & Pages

### Frameworks, Libraries & Resources Used
#### Frontend
I use these libraries for my work 
- [Bootstrap v4.0.0-beta.2](https://getbootstrap.com/) : The world’s most popular front-end open source toolkit<br>
- [Themify Icons](https://themify.me/themify-icons) : Themify Icons is a complete set of icons for use in web design and apps, consisting of 320+ pixel-perfect <br>
- <a href="hhttps://fontawesome.com/">Font Awesome 4.7.0</a> : used for icons in the home page detail navigation section and footer social media links. Needed for site aesthetic and UX purposes<br>
- <a href="https://jqueryniceselect.hernansartorio.com/">jQuery Nice Select</a> : Simple Open Source icons that i used in footer<br>
- [jQuery FlexSlider v2.0](http://flexslider.woothemes.com/) : A lightweight jQuery plugin that replaces native select elements with customizable dropdowns.<br>
- [Owl Carousel v2.2.1](https://owlcarousel2.github.io/) : Fully Customisable. Over 60 options. · Touch and Drag Support. Designed specially to boost mobile browsing experience.
- [SlickNav Responsive Mobile Menu v1.0.10](https://github.com/ComputerWolf/SlickNav) : slicknav is a simple and easy-to-use jQuery menu plugin for creating a responsive & cross-browser multi-level navigation menu on your website.
#### Backend
- [Django](https://www.djangoproject.com/) : the framework used to build the project and apps.<br>
- [Heroku](https://www.djangoproject.com/) : used to deploy my project and incorporate their postgreSQL resource.<br>

### website consists pages

- Homepage
- Shop
- About us
- Wishlist
- Cart
- Checkout
- Profile page

### Supported Browsers 
- Chrome
- Firefox
- Safary
 and other popular browsers ...
 
 
 
 
### **Validation**
  The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

- **W3C Markup Validator**
  All the pages are HTML error free expect for stripe iframe errors.
  For Certain pages manual testing was performed, due to a w3-Html-checker unable access pages for reasons like.. requeries login, administrator privileges, required post or other...
  -  Manual testing performed for the following pages.\
      ✓ Profile page\
      ✓ Update user profile\
      ✓ Checkout page\
      ✓ Cart page\
      ✓ Add new product\
      ✓ Admin manage

- **W3C CSS Validation**\
  ✓ All the CSS files are error free 
- **PEP8 compliance test**\
  ✓ All the custom .py files are error free. Scanning found some errors and all of them was was corrected
## Deployment

### Stripe (Payments API) setup

Prior to deploying the application to Heroku it is recommended that you create a Stripe account to use the payment processing functionality - note: the application is set for test payments only. Follow the steps below to create an account and to retrieve the necessary keys you will need later.

1. Create an account at [Stripe](https://dashboard.stripe.com/register)

2. Goto the [account dashboard](https://dashboard.stripe.com/test/dashboard).

3. Click the _Developers_ link then [API keys](https://dashboard.stripe.com/test/apikeys)

4. You will see two keys; `Publishable key` and `Secret key`. Keep these private, you will need them later when setting environment variables in Heroku.

| Stripe Key | Maps to Environment Key |
| ---------- | ----------------------- |
| Publishable key | STRIPE_PUBLISHABLE_KEY |
| Secret key | STRIPE_SECRET_KEY |

### Remote (Heroku)

1. Create an account at [Heroku](https://www.heroku.com/).

2. Download CLI [here](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).

3. Open up CMD (Windows) or Terminal (MacOS) and type the following and follow the instructions that appear.

```terminal
heroku login
```

4. Create a new Heroku app using the following code in your terminal:

```terminal
heroku create app-name-here
```

5. With the Heroku app name you just created, modified the `production.py` file in the settings folder and update the following:

```python
ALLOWED_HOSTS = ['your-app-name.herokuapp.com', '127.0.0.1', 'localhost']
```

6. Open the [Heroku apps](https://dashboard.heroku.com/apps) webpage and click the app you created in Step 4.

7. Navigate to the Settings tab on the top horizontal bar, we will be adding the required _environment variables_ here.

8. Click the _'Reveal Config Vars'_ button and add the below variables:

| KEY  | VALUE |
| ---- | ----- |
| `ENV_SETTINGS` | `settings.production` |
| `SECRET_KEY` | input your own value here |
| `STRIPE_TEST_PUBLISHABLE` | input your own value here |
| `STRIPE_TEST_SECRET` | input your own value here |

9. Given the application has been developed within a Docker container, it will be deployed to Heroku using Docker. To enable this, Heroku requires a *[heroku.yml]* file is created. The [Heroku documentation](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml) provides more detail on this.

10. The Heroku stack will need to be set to use container - this is specific to deployment with Docker. You can find out more [here](https://devcenter.heroku.com/articles/stack). To do this type the following command into your terminal:

```terminal
heroku stack:set container -a app-name-here
```

11. You can verify the above was completed by going to your app's overview screen, on the Heroku website and clicking the latest activity, you should see something similiar to:

```text
email@address.com: Upgrade stack to container
```

12. A database is required to run the application, we will use Heroku's free option to do so. This step can be completed using the terminal, with the following code:

```terminal
heroku addons:create heroku-postgresql:hobby-dev -a app-name-here
```

13. To push the code to the Heroku app, a git remote link needs to be added and the code then needs to be pushed. To do this, within your terminal write the following code:

```terminal
heroku git:remote -a app-name-here
git push heroku master
```

14. Given this will be a fresh build, Django will need to create the required databases in our database. Run the following code in your terminal:

```terminal
heroku run python manage.py migrate 
```

_**NOTE:** `--settings=settings.production` is required because Django by default looks for the file, `settings.py`. This does not exist within this application, instead a settings folder has been setup with different settings dependent on the environment the application is being run on._

15. Next, a superuser account needs to be created to manage the application. Type the following into your terminal:

```terminal
heroku run python manage.py createsuperuser 
```

16. It is possible to link your Github repository to Heroku so that each time new code is committed to Github, it is also deployed to Heroku and thus your Heroku app is always sync to Github. To do this, nagivate to the following link and input your Github details. You will be prompted to search for the repo name. Once you have selected the repo make sure to click **Enable automatic deploys**.

```url
https://dashboard.heroku.com/apps/app-name-here/deploy/
```

17. To enable product images to be uploaded you will need to install django-storages and use Amazon S3 to store media files. Follow [this excellent guide](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) to set this up. Follow all the steps for creating an S3 bucket, assigning access, and retrieving the keys to access it. Once you have the access keys you can proceed to the step below.

18. You will need to create some additional environment variables in Heroku - these are outlined below and are self-explantory. (See Steps 6-8 above for a refresher on creating Heroku environment variables)

| KEY  | VALUE |
| ---- | ----- |
| `USE_S3` | `TRUE` |
| `AWS_ACCESS_KEY_ID` | access key you created in Step 17 |
| `AWS_SECRET_ACCESS_KEY` | access key you created in Step 17 |
| `AWS_STORAGE_BUCKET_NAME` | the name of the bucket you created in Step 17 |

19. Run the below command in the Heroku CLI:

```terminal
heroku run python manage.py collectstatic --noinput 
```

19. Your Heroku deployment is now operational. You can access it via the Heroku dashboard.



## Contributing

First off, thanks for taking the time to contribute! Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make will benefit everybody else and are **greatly appreciated**.

## License
This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.



See [LICENSE](https://choosealicense.com/licenses/mit/) for more information.

 

