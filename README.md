# DjangoForum 💬
Basic online forum made with Django for the 2020 PennApps Development Team Application.
## Instructions for Running Code 📝
1. Don't! Check out the website here: https://yudrew-django-forum.herokuapp.com/
### Actually Running the Code 🖥 (Instructions are probably lacking... you may need to install Postgres. Also only works with MacOS at the moment)
1. Download the repo
2. Open the repo directory in terminal or command prompt
3. (Optional) Open a fresh new virtual environment however you'd like. Just make sure you have pip installed.
4. Run "pip install -r requirements.txt" in terminal or command prompt
5. Open your .bash_profile and stick in the following code block with your own values substituted as necessary:

    export SECRET_KEY="GENERATE_A_SECRET_KEY_AND_PUT_IT_HERE_ANY_KEY_WILL_DO"
    export DEBUG_VALUE="True"

6. Run "source ~/.bash_profile"
7. Go to DjangoForum/mysite/settings.py and comment out the following code, since you'll be hosting images on your own machine: 
	DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
8. Run "python manage.py runserver" in terminal or command prompt. If this fails, make your migrations with "python manage.py makemigrations" and then "python manage.py migrate", then try again.
9. Open up localhost:8000 in the browser of your choice
10. Explore the wild Django forum. It'll be blank, but register a user and mess around a bit.
11. If anything doesn't work, post an issue and I'll try to fix either the instructions or the code.
## Core Functionalities Completed 💪
- User registration/login/logout
- Post viewing restricted to authenticated users
- Users can create new posts and delete their own posts
- Users can see all posts
- Cloud hosting on Heroku
## Additional Challenges Finished 🙌
- A bit of html/css styling, largely pulling from Corey Schafer tutorials
- Users can view all posts made by any specific user
- Users can upload images with their posts
## Additional Challenges to be Completed Some Day in the Future 🛠
- Post liking system
- Mandatory email verification
- Post commenting (it's really not much of a forum without the comments section 🤔)
## Known bugs 🕷
- Images properly resize to a set maximum, but they don't adjust with window size. Overall the HTML and CSS is wonky.
## General Thoughts / Feedback on the Assignment 💭
- Was a nice escape from Netflix during quarantine
- Corey Schafer's Django tutorial series is amazing and I followed a lot of it very closely
