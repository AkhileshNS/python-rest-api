# PYTHON REST API

- **Step 1**: To install python run

  - windows - `choco install python -y`
  - macos - `brew install python`
  - linux - `sudo apt update && sudo apt install python3.6 && sudo apt install python-pip`

  [OR] Download and install it from [here](https://www.python.org/downloads/)

  Verify everything is installed using `python --version` and `pip --version`

- **Step 2**: run `pip install flask` to install flask (In Linux, additionally run `sudo apt install python3-flask`)

- **Step 3**: Create a new folder, create an index.py file and put the following contents inside:-

  ```python
  from flask import Flask
  app = Flask(__name__)
  @app.route('/hello')
  def hello_handler():
      return 'world of python'
  ```

- **Step 4**: In the same folder, open a cmd/powershell/bash window and run

  - `$env:FLASK_APP="index.py";flask run` on windows
  - `export FLASK_APP=index.py && flask run` on macos/linux
    to launch your REST API

- **Step 6**: Don't forget use git to manage your project

# To Deploy REST API via Heroku

- **Step 1**: Before deploying to Heroku, we must first use a production server, so run `pip install gunicorn`

- **Step 2**: Also run `pip freeze` and paste the contents of the output in a _requirements.txt_ file at your project folder:-

  ```txt
  autopep8==1.4.4
  Click==7.0
  Flask==1.1.1
  gunicorn==19.10.0
  itsdangerous==1.1.0
  Jinja2==2.10.3
  MarkupSafe==1.1.1
  pycodestyle==2.5.0
  Werkzeug==0.16.0
  ```

- **Step 2**: Now add a _Procfile_ in your project with the contents:-

  ```Procfile
  web: gunicorn index:app
  ```

- **Step 3**: Now create a folder _.github/workflows_ and in there create a file _main.yml_ with contents:

  ```yaml
  name: Deploy
  on:
    push:
      branches:
        - master
  jobs:
    build:
      runs-on: ubuntu-latest

      steps:
        - uses: actions/checkout@v1.0.0
        - uses: akhileshns/heroku-deploy@master
          with:
            heroku_api_key: ${{secrets.HEROKU_API_KEY}}
            heroku_email: ${{secrets.HEROKU_EMAIL}}
            heroku_app_name: ${{secrets.HEROKU_APP_NAME}}
  ```

- **Step 4**: Now we can push this to GitHub but before that, make sure you have created a Heroku account and in account settings, copy the api key. Then in the github repo for this project, go to settings and add secrets HEROKU_API_KEY (Your copied apikey), HEROKU EMAIL (The email associated with your heroku account) and HEROKU_APP_NAME (The name of your app and keep in mind it needs to be unique in heroku)

  Now whenever you push to the master branch of your github repo, your app is automatically deployed to heroku
