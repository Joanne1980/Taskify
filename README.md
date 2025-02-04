# Taskify

[View live site here!](https://taskify-todo-eaffb38b30eb.herokuapp.com/login/)

**Project Overview**

**Todo Task application**

This web application was designed with the intention of helping people stay up to date with tasks they need to get through each day 

![amiresponsive](/Documentation/Amiresponsive.png)

---

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

**ERD**

![ERD](/Documentation/TaskifyERD.png)

### User Stories

Shown below is my Project Board which shows the features i was not able to implement in the given timeline.

![Project Board](/Documentation/Projects-board.png)

| **User Story ID** | **User Story Description**          | **MoSCoW Prioritization** |
|-------------------|-------------------------------------|---------------------------|
| #1                | User Registration                   | Must Have                 |
| #2                | User Login                          | Must Have                 |
| #3                | User Logout                         | Must Have                 |
| #4                | Create task                         | Must Have                 |
| #5                | Edit task                           | Must Have                 |
| #6                | Delete task                         | Must Have                 |
| #7                | Bright colours & images             | Must Have                 |
| #8                | Reward stickers                     | Should Have               |
| #9                | Pre loaded tasks                    | Should Have               |
| #10               | Points system                       | Should Have               |
| #11               | Share tasks                         | Should Have               |
| #12               | Headings                            | Should Have               |
| #13               | Reminders                           | Could Have                |

**Agile**

The developement of the task application was broken down in to smaller easier to maintain tasks. In future sprints I would like to continue to develope the application to be better with more features and colours 

## Design

### Colour Scheme

The colours I originally chose for the Taskify app changed during developement for a more cleaner look. 

![Colour Palette](/Documentation/Colours.png)


### Typography

The font I used was Lato as I liked the crispness and ease of reading at a glance


### Wireframes

![wireframe](/Documentation/Wireframe.png)

## Features

My application is made up of the registration/login page, the task page where you can see which tasks you have outstanding or completed, edit taks page, delete task page. Search bar where you can also filter tasks and a log out. You have to be a registered user to use Taskify. 


### Future Implementations

In the future I would like to add a task/chore share feature where you can share jobs with your family, friend, colleagues. Also a points system where you can be rewarded points and stickers for example for completing tasks

### Accessibility

I have run a lighthouse test and a wave test to ensure I have met the requirements needed to be accessible friendly. images shown in the test section 

## Technologies Used

### Languages Used

- HTML
- CSS
- JavaScript
- Python
- [Git](https://git-scm.com/) used for version control.
- [Github](https://www.github.com) used for online storage of codebase and Projects tool.
- [GitPod](https://codeinstitute-ide.net/workspaces) as the IDE Code Institute recommeneds we use.
- [Coolors](https://coolors.co/) for colour theme creation and accessibility checkers.
- [Django](https://www.djangoproject.com/) was used as the Python framework for the site.
- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) create and host the database.
- [Heroku](https://www.heroku.com) was used to host the Muddy Paws application.
- [WAVE](https://wave.webaim.org/) to evaluate the accessibility of the site.
- [Figma](https://www.figma.com/) was used for Wireframes
- [LucidChart](https://www.lucidchart.com/) was used for ERDs.



## Deployment


### Deployment

The site was deployed to Heroku. The steps to deploy are as follows:
 - Install the gunicorn python package and create a file called 'Procfile' in the repo's root directory
 - In the Procfile write 'web: gunicorn lunar_lists.wsgi'
 - In settings.py add ".herokuapp.com" to the ALLOWED_HOSTS list
 - In settings.py add 'https://*.herokuapp.com' to CSRF_TRUSTED_ORIGINS list, git add, commit and push to github

Navigate to the Heroku dashboard
 - Create a new Heroku app
 - Give it a name and select the region 'Europe'
Navigate to settings tab and scroll down to Config Vars
 - Click 'Reveal Config Vars'
 - Add the following keys:
         key = DATABASE_URL | value = (my secret database url)
         key = SECRET_KEY | value = (my secret key)
Navigate to Deploy tab
 - Connect to GitHub and select the repo 'lunar-lists'
 - Scroll down to 'Manual deploy' and select the 'main' branch
 - Click 'Deploy Branch'

## Testing

## Manual Testing

| **Feature**   | **Expected**                                                         | **Result** | **Fix**            |
|---------------|----------------------------------------------------------------------|------------|--------------------|
| Login         | Once correct username and password used should take you to task page | Correct    | Works as it should |
| Register      | Once registered should be taken to task page                         | Correct    | Works as it should |
| Logout        | Log out page should take you to login page                           | Correct    | Works as it should |
| Add Task      | Click add task or the cross next to search bar, add title and description click save, Task saved to task page        | Correct    | Works as it should |
| Update Task   | Click on task will open it up for you to edit                        | Correct    | Works as it should |
| Complete Task | Click on complete box inside of the task, strikes out task and change dot to green | Correct | Works as it should|
| Delete Task   | Click on cross next to task on main screen will open new page asking to confirm | Correct | Works as it should|
| Search Task   | Click in search bar start to type out name of task and click search will bring up any tasks starting with the same letters as you have typed in. | Correct | Works as it should |
| Three dots    | Click on three dots you can move tasks around to put them in the order you wish | Correct | Works as it should |

## Responsive 

| **Screen Size**   | **Responsive** |
|-------------------|----------------|
| Iphone SE         |  Yes           |
| Samsung Galaxy S8 |  Yes           |
| Ipad Pro          |  Yes           |
| Desktop           |  Yes           |


## Lighthouse 
![Lighthouse](/Documentation/Lighthouse.png)

My lighthouse testing was very successful I was very happy with this outcome. 

## Wave Testing

![wave](/Documentation/Wave.png)

A few errors but I was unable to fix due to not being able to see exactly where the issue was coming from. 

## CSS Testing

![W3C CSS Validation](/Documentation/CSS.png)
No errors found

## HTML Testing

![HTML validation](/Documentation/Register.png) 

![HTML Validation](/Documentation/Login-page.png) 

![HTML Validation](/Documentation/Task-page.png)

![HTML Validation](/Documentation/Todo-form.png)
Only errors I came across where ones that are in djangos prebuilt forms so I cannot fix those

## Python Testing 

![Python linter](/Documentation/Python.png)
No errors


## Credits

### Code Used

- [perplexity](https://www.perplexity.ai/)
- [Daisy Walkthrough](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1)
- [Dennis Ivy](https://www.youtube.com/watch?v=llbtoQTt4qw)
  
###  Acknowledgments

- First of all I would like to thank my amazing Learning Facilitator [Amy Richardson](https://github.com/amylour) for her  guidance and support over the last 16 weeks. Without her I would not be where I am with this project, she is a credit to Code Institute. 

- I would also like to thak my coding coaches John Rearden and [Mark Briscoe](https://github.com/mbriscoe) for all their guidance throughout the course. They have some wonderful knowledge. 

- I would like to thank my Cohort for always having each others backs and always lending a hand or an ear when needed.

- Dennis Ivy I watch many youtube videos over the three weeks and before this project and once I found Dennis things started to make a little more sense 

### Over view
I have to say the last three weeks in completing this project has been a huge learning curve. First trying to build a web application which was far to big for my first proper solo Django project. I just wish I had realised sooner to save myself some stress and tears. My final project wasnt exactly how I had envisioned it but I suppose it is all about learning and growing. I do plan in building it further in the future and have to say it was quite fun minus the stress. 
Thank you for looking at my project 