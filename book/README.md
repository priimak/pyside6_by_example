PySide6 By Example
==================

## Introduction
The goal here is to show how to develop simple but practical GUI 
applications using Python and Qt 
using [PySide6](https://wiki.qt.io/Qt_for_Python) library. Emphasis 
is on _practical_. Many of the examples on the web are either way 
too simple or too complex and thus are not practical. But what is 
practical? That will vary depending on the problem at hand, however, 
there are a few motifs that seem to repeat from one place to another. 
These are:

1. Searching and displaying tabular data.
2. Transforming data.
3. Visualization of numerical data.
4. Configuring and executing complex processes.

All of the above does not technically require use of graphical 
applications, however, target audience could be accountants, 
electrical or mechanical engineers, managers and so on. For them
having an intuitive GUI for these tasks is essential.

In this project we will build several GUI applications. You can use
them as templates for your own projects. All code here is under MIT 
license, which means that you are free to copy and incorporate any 
part the code into your projects.

My goal here is not to build a clever code, but code that is easy 
to modify and extend. 


## Init project

```shell
uv init --app pyside6_by_example -p 3.13
cd pyside6_by_example
uv venv --seed -p 3.13
```

Activate virtual environment

```shell
.venv\Scripts\activate
```

And then edit `pyproject.toml` file add make sure that `dependencies` appear like so
```python
dependencies = ["pyside6"]
```

Then download dependencies by running
```shell
uv pip install -r .\pyproject.toml
```

When done running `uv pip freeze` should show something like this:
```shell
pip==24.3.1
pyside6==6.8.0.2
pyside6-addons==6.8.0.2
pyside6-essentials==6.8.0.2
shiboken6==6.8.0.2
```

## First basic template GUI application