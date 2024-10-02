Blogsite README


PFE_BlogProject 


PFE_blog


Requirements
Before running the project, make sure you have the following installed on your machine:

Python 3.12.6
Pip (Python package installer)


Installation

Clone the repository:

git clone https://github.com/yourusername/PFE_BlogProject.git
cd PFE_BlogProject

Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install django


Set up the Django project:
Navigate to the project directory and set up the initial database with migrations:
cd PFE_blog
python manage.py migrate


Create a superuser for admin access:
python manage.py createsuperuser


Run the development server:
python manage.py runserver


The project will be available at http://127.0.0.1:8000/.

Running the Project
Open your web browser and navigate to http://127.0.0.1:8000/.
For admin access, go to http://127.0.0.1:8000/admin/ and log in with the superuser account you created.
Start creating blog posts, managing users, and exploring the features of the site.



