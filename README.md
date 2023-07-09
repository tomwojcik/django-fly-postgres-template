### Before we begin

Start with creating a PostgresDB. DB providers I suggest:
1. Fly.io - [howto](https://fly.io/docs/postgres/getting-started/create-pg-cluster/)
* has a free tier, but requires a "free app slot" (which you can have up to 3)
* [this is NOT a managed Postgres](https://web.archive.org/web/20230219115111/https://fly.io/docs/postgres/getting-started/what-you-should-know/). Probably good enough for your side projects, but not production ready
2. Supabase.com
* has a free tier
* very scalable and production ready if you're willing to pay

### How to use

Last I checked, Jinja2 didn't work well with Python3.11. Use any lower Python version.

```shell
$ pip install -U cookiecutter jinja2
$ cookiecutter gh:tomwojcik/django-fly-postgres-template
```

Give it a proper name

```shell
project_name [Fly App]: My Blog
project_slug [my_blog]:  # just hit enter if it looks fine, the slug is generated automatically
```

Post generation hook already creates a git repository and adds everything that's been created. Just add remote and push

```shell
$ git remote add origin git@github.com:<username>/<reponame>.git
$ git push -u -f origin main
```

For the next steps follow the `README.md` from the generated app.
