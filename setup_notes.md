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
1. Create the folder for the project using `$ mkdir`
2. Start by creating the `app.py` file in that folder
3. Then import Flask by writing `from flask import Flask` to the top of `app.py`
4. Create an application object with `app = Flask(__name__)`
5. We can also go ahead and create the index route with:
```
@app.route('/')
def index():
  return render_template('index.html') # note we will also need to import render_template by adding it to the line from step 3 above
```
6. Create a folder called `templates` # by default Flask will look in there for all templates
7. Add the basic HTML structure in `index.html`
8. Note that we can also pass data into the template by editing the route:
```
@app.route('/')
def index():
  return render_template('index.html', data=[{
    'description': 'example 1' # note this is dummy data
  }, {
    'description': 'example 2'
  }])
```
9. To create the database for the project:
  * SQLAlchemy doesn't create the database so we need to do that manually from the CLI with `createdb <app_name>`
  * Add `from flask_sqlalchemy import SQLAlchemy` to the `imports` section of `app.py`
  * Define the db object with `db = SQLAlchemy(app)` in the `config` section of `app.py`# links SQLAlchemy to the app
  * Define the model(s) in `app.py`:
  ```
  class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
  ```
  * Optionally add a `repr` method to the model(s) for debugging:
  ```
  def __repr__(self):
    return f'<Todo {self.id} {self.description}>' # where Todo, id and description are examples based on the todoapp model
  ```
  * install Flask-Migrate by running `$ pip3 install Flask-Migrate`
  * Add `from flask_migrate import Migrate` to the `imports` section of `app.py` and then add `migrate = Migrate(app, db)` in the `config` section of `app.py`
  * Add the config variable to tell the app where to connect to the database as `app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://local-admin:localhost:5432/app_name'`
  * Note that we can also do this by defining the variable in a `config.py` file with `SQLALCHEMY_DATABASE_URI = 'postgresql://local-admin@localhost:5432/app_name'` and then running `app.config.from_object('config')` in `app.py` # see (documentation)[https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-files]
  * Run `$ flask db init` to create the initial migrations directory structure
  * If already created per above, clear the database by running `$ dropdb <app_name>` # confirm this step is necessary if steps above were followed from scratch with db edits
  * Create the database again by running `$ createdb <app_name>`
  * If there are any issues, try restarting the postgresql server with:
  ```
  $ brew services stop postgresql
  $ brew services start postgresql
  ```
  * Run `$ flask db migrate` to detect the model changes to be made and create a migration file with `upgrade` and `downgrade` logic
  * If there are any dependency errors, install the required modules (in my case, it mentioned my environment hadn't yet installed `psycopg2`)
  * Review the migration file generated in `migrations/versions`. If everything checks out, run `$ flask db upgrade` to apply the migration
  * Confirm that the migration set up the tables defined as models by running `$ psql <app_name>` and then `=# \dt`
10. Design/review the models to normalize object properties and relationships. This should include implementation of association tables or models
11. Implement any changes via the migration process above
12. Implement form submissions for creating new objects in the models
  * Note to insert arrays into the database with SQL, use the ARRAY object. For example, INSERT INTO table_name (column_name) VALUES (ARRAY['a', 'b', 'c'])
  * Create the route and associated function
  * Instantiate an object using a variable name and the object class. Use `request.form.get(property_a)` or `request.form.getlist(property_b)` to define the object's properties
  * Persist the object to the database with `db.session.add(venue)` and `db.session.commit()`
  * Implement error handling and `flashes` as user messages for errors
  * I ran into some issues with the Show model where the id was not set to increment automatically. Going into the database directly via `psql` and running `ALTER TABLE "Show" ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY;` solved my problem
  * Confirmed that trying to create a show for a venue or artist that doesn't exists throws an error
  * [ ] Consider coming back here to change the venue_id and artist_id in the form to drop downs
  * [ ] Consider coming back here to review how we might prevent duplicate shows




x. Review the config file to check for the database connection and insert the appropriate URI. Also, you might consider turning off track modifications
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user@localhost:5432/app_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```
