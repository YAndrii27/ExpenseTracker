# Expense tracker  
  
It's a realization of the [project](https://www.coursera.org/learn/showcase-build-expense-tracker-app-django/home/welcome) from the Coursera.  
It has **only** basic front-end.

## Project goals  
  
- Develop a CRUD* view to manage book categories (such as Business Analytics, Python, Data Science, and Math). ✅
- Develop a CRUD* view to add book information such as the title, the author, the publishing date, the book category, and the distribution expenses. ✅
- Import existing data from [spreadsheets](https://docs.google.com/spreadsheets/d/1VRzbBwvhisfFbN6YTAuRO5Qsg13and8eGXA0zX4oa_A/edit#gid=0) to the web app.  
- Develop a report view that enables the team to view the distribution expenses of books according to their categories.  ✅
  
*By CRUD here means create, read, update, and delete.  
  
## Running
#### If you have a poetry in your system:

    git clone github.com/YAndrii27/expense-tracker

    cd expense-tracker/expensetracker

    poetry install

    poetry run python manage.py runserver

#### If you do not have a poetry:
    git clone github.com/YAndrii27/expense-tracker

    cd expense-tracker/expensetracker

    pip install -r ../requirements.txt

    python manage.py runserver
