# PdfBackend
Start by making a virtual environment in the project directly 

```bash
 python3 -m venv env
```
After making a virtual environment activate it

```bash
source env/bin/activate
```
Now install required packages using `requirement.txt`

```bash
pip install -r requirement.txt
```

If every thing works then, run the migrations 

```shell
python manage.py makemigrations
python manage.py migrate
```
Now run the server
```bash
python3 manage.py runserver
```