## Creating a virtual environment

python -m venv <folder_name>

e.g.

```
python -m venv .venv
```
- to activate it:
```
source .venv/bin/activate
```
- to deactivate it:
```
deactivate
```

- to install packages:
pip install <package_name>
e.g.
```
pip install Faker
pip install Django
```

## To create a requirements file
```
pip freeze > requirements.txt
```
# To install the packages in an empty project
1. Create the virtual environment on your machine
2. Run the following : ```pip install -r requirements.txt```
3. Please do not forget to add a .gitignore file with the .venv/ folder as an entry in it

## For Windows Users
1. Run your command prompt as an Administrator
2. .\.venv\Scripts\activate