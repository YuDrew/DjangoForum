# DjangoForum 💬
Basic online forum made with Django for the 2020 PennApps Development Team Application.
## Instructions for Running Code 📝
1. Don't! Check out the website here: https://yudrew-django-forum.herokuapp.com/
### Run the Code Locally 🖥 
Instructions are for MacOS, but you would follow similar steps for a Windows machine.
1. Download the repo
2. Open the repo directory in terminal or command prompt
3. (Optional) Open a fresh new virtual environment however you'd like. Just make sure you have pip installed.
4. Install the required packages in terminal or command prompt with a pip install

```bash
    pip install -r requirements.txt
```

5. Open your .bash_profile and stick in the following code block with your own values substituted as necessary:

```bash
    export SECRET_KEY="GENERATE_A_SECRET_KEY_AND_PUT_IT_HERE_ANY_KEY_WILL_DO"
    export DEBUG_VALUE="True"
```

6. Apply these changes to your environment with

```bash
    source ~/.bash_profile
```

7. Go to DjangoForum/mysite/settings.py and comment out the following code, since you'll be hosting images on your own machine

```python
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

8. Start your server in terminal or command prompt

```bash
    python manage.py runserver
```
If this fails, make your migrations to set up the database and then try again
```bash
    python manage.py makemigrations
```
and
```bash
    python manage.py migrate
```
9. Check your terminal output. You should see something like this:

```bash
    System check identified no issues (0 silenced).
    June 02, 2020 - 14:53:23
    Django version 3.0.6, using settings 'mysite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
```
From the line "starting development server at...", copy the url into the browser of your choice.

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
