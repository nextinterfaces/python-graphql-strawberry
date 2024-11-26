---

## Installation

Follow these steps to set up and run the project locally:


Install virtualenv via pipx

If you specifically want to use virtualenv, you can use pipx, which is Homebrew’s recommended way to manage Python applications.

Install pipx if this is brew managed python:

    brew install pipx

Ensure pipx is configured:

    pipx ensurepath

Install virtualenv using pipx:

    pipx install virtualenv

Create a virtual environment using virtualenv:

    virtualenv .venv

Activate the virtual environment:

    source .venv/bin/activate

    # or deactivate when done
    deactivate

Proceed to install packages (e.g., Flask):

    pip install -r requirements.txt
    pip list

Or install manually:

    pip install 'strawberry-graphql[debug-server]'
    pip install fastapi uvicorn
    pip freeze > requirements.txt
    pip list

Run the service:

    uvicorn main:app --reload


- OpenAPI docs:
http://127.0.0.1:8000/redoc#
http://127.0.0.1:8000/docs#/


