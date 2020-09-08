# Set Up Notes
## Guide rails for setting up the dev environment and getting started on a project

### Dev Environment
0. Clone the repo `$ git clone <git-link> <target-directory>`
1. Check that Flask is installed by running `Flask --version`
2. If it isn't installed run `cd ~ && pip3 install Flask`
3. Install virtualenv by running `pip install virtualenv`
4. To initialize a Python virtual environment:
```
$ cd <project_path>/
$ virtualenv env # Note here that the Udacity instructions include a deprecated flag that is now the default behavior of virtualenv
$ source env/bin/activate
```
5. Locate the dependencies file `requirements.txt` and run `pip install -r <path>/requirements.txt`
6. Run the development server:
```
$ export FLASK_APP=myapp
$ export FLASK_ENV=development # enables debug mode
$ python3 app.py
```
7. The site should now be running in localhost:[port-number]

### App development
[ ]
