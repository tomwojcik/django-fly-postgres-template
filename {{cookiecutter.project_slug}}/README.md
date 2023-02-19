## Initial setup

In the development environment I use docker.

**Warning**, the Dockerfile is glued together without giving it much thought. It needs some improvements but it works.

To run the app, in one terminal run
```shell
make up
```

Then in another
```shell
make migrate
```
to apply the migraitons.

Confirm you see some Lorem ipsum in your browser at [`http://127.0.0.1:8000`](http://127.0.0.1:8000).

Django Debug Toolbar and Silk profiler ([http://127.0.0.1:8000/silk/](http://127.0.0.1:8000/silk/)) are already working.

## Fly setup

#### Create new app

```shell
$ flyctl launch --copy-config --no-deploy --name {{cookiecutter.project_slug}}
```

You should see
> Your app is ready! Deploy with `flyctl deploy`

If you see

> Error Validation failed: Name has already been taken

You will need to come up with a different name. Any will do. Replace it in the `launch` command above and
your `fly.toml` file.

#### Set secrets

```shell
$ flyctl secrets set DJANGO_SECRET_KEY={{ random_ascii_string(64) }} DJANGO_ALLOWED_HOSTS={{cookiecutter.project_slug}}.fly.dev
```

Remember to also push secrets for the DB.

You should see
> Secrets are staged for the first deployment


```shell
$ flyctl secrets set POSTGRES_HOST=? POSTGRES_USER=? POSTGRES_PASSWORD=? POSTGRES_DB=?
```

#### Deploy

If you have Docker installed, I'd suggest to deploy with

```shell
$ flyctl deploy --local-only --build-target production
```

The remote
builder [is/was somewhat fragile](https://tomwojcik.com/posts/2022-09-02/django-app-on-fly#3-remote-builder-is-very-fragile)
.
Otherwise, just drop the `--local-only` flag and it should be ok.

After a moment you should see

> deployed successfully

Congrats, your app is live! From now on you can just `make deploy` or see `.github/workflows` to deploy automatically on push.

## If you want to point a domain towards you fly app

Assuming that your domain is `example.com` and your Fly app subdomain is `{{cookiecutter.project_slug}}.fly.dev`:


1. Allocate IP addresses

    If you run

    ```shell
    $ flyctl ips list
    ```

    you will see that your IPv4 is shared. You can allocate it using

    ```shell
    $ fly ips allocate-v4 -a {{cookiecutter.project_slug}}
    ```

2. Issue the certificates

    ```shell
    fly certs create "*.example.com" -a {{cookiecutter.project_slug}}
    ```
    Configure the challenge using CNAME DNS record. For details see https://fly.io/apps/{{cookiecutter.project_slug}}/certificates

3. Configure the rest of the DNS

    ```shell
    $ flyctl ips list
    ```

    to check again what IP addresses are allocated for your app, set IPv4 for `A` record and IPv6 for `AAAA`.

    ```shell
    example.com   A: <IPv4>
    example.com   AAAA: <IPv6>
    *.example.com CNAME: {{cookiecutter.project_slug}}.fly.dev.
    ```
