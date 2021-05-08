Project consists of two parts: 
- django project
- svelte project

# To get started

- `git clone https://github.com/Sanshain/django-sapper-boilerplate.git`

To develop with this boilerplate you'll need two terminal instances

The first instance for working with svelte infrastructure:

- `cd project/main_app/templates`
- `npm i`
- `npm run build`
- `npm run export`
- `npm run dev`

Quick paste line: 

```bash
cd project/main_app/templates && npm i && npm run build && npm run export && npm run dev
```

Second instance:

- [`pip install pipenv`]
- `pipenv install`
- `pipenv shell`
- `cd project`
- `py manage.py runserver`

For everyday development employ this one:

```
pipenv shell && cd project && py manage.py runserver
```
