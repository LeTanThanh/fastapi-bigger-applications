from fastapi import FastAPI

from .routers import users

app = FastAPI()

app.include_router(users.router)

# An example file structure

"""
Let's say you have a file structure like this:

|__ app
|   |__ __init__.py
|   |__ main.py
|   |__ dependencies.py
|   |__ routes.py
|   |   |__ __init__.py
|   |   |__ items.py
|   |   |__ users.py
|   |__ internal
|       |__ __init__.py
|       |__ admin.py

There are several __init__.py files: one in each directory or subdirectory.

This is what allows importing code from one file into another.

For example, in app/main.py you could have a line like this:

from app.routes import items

- The app directory contains everything.
And it has an empty file app/__init__.py, so it is a "Python package" (a collection of "Python modules") app.

- It contains an app/main.py file.
As it is inside a Python package (a directory with a file __init__.py), it os a module of that package: app.main.

- There's also an app/dependencies.py file, just like app/main.py, it is a module: app.dependencies.

- There's a subdirectory app/routes/ with another file __init__.py, so it's a Python subpackage: app.routes.

- The file app/routes/items.py is inside a package, app/routes/, so it's a submodule: app.routes.items.

- The same with app/routes/users.py, it's another submodule: app.routes.users.

- There's also a subdirectory app/internal with another file __init__.py, so it's another Python subpackage: app.internal

- And the file app/internal/admin.py is another submodule: app.internal.admin.
"""

# APIRouter

# Dependencies
