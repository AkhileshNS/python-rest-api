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
