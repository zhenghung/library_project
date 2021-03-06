# Library Project
By Rebecca Carter and Zheng Hung Chuah

## Project Structure
```
├───migrations
├───models
│   ├───acc_types.py
│   ├───author.py
│   ├───book.py
│   └───user.py
├───paths
│   ├───api_paths.py
│   ├───general_paths.py
│   ├───librarian_paths.py
│   └───user_paths.py
├───services
│   ├───cookies.py
│   ├───db_helper.py
│   ├───librarian.py
│   ├───loan.py
│   └───tools.py
├───static
│   ├───images
│   │   ├───covers
│   │   └───prof_pics
│   └───style
├───views
│   ├───librarian_pages
│   ├───user_pages
│   └───visitor_pages
├───config.py
├───lib_project.py
└───requirements.txt
```

`models` contain class functions related to specific object types

`paths` contain the functions that are called when a request is received such as a GET or POST

`services` container helper functions used to read from and write to the database

`static` contains static files like images, css styling and javascript files

`views` contain tpl files that are used by bottle to convert into html

`config.py` contains the settings for the variables used in the web app

`lib_project.py` The project's main, run this to star the application

`requirements.txt` A list of dependencies needed to run the application



## Dependencies
1. python-bottle
2. bottle-sqlite

## Installing Dependencies
```
$ pip install requirements.txt
```

## Configuring the Web App
Edit the "config.py" file to change the variables
```
vim config.py
```


## Running the Web App
```
python lib_project.py
```





