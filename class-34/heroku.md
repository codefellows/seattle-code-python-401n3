# Deploy Project - Heroku Time

- install [heroku cli](https://devcenter.heroku.com/articles/heroku-cli)
- `heroku apps:create snacks-api`
- Check remote with `git remote -v`
- If heroku remote doesn't show then `heroku git:remote -a snacks-api`
- Create `heroku.yml` in root folder.
- Add below text to `heroku.yml`

```yaml
build:
  docker:
    web: Dockerfile
release:
  image: web
  command:
    - python manage.py collectstatic --noinput
run:
  web: gunicorn project.wsgi
```

- **EXTRA IMPORTANT STEP**
- `heroku stack:set container`
- Add/Commit
- `git push heroku main`
- Go to [heroku](https://www.heroku.com/)
- Login takes you to dashboard
- Select your app
- Go to settings
- Click `reveal config vars` button
- Add config vars to match `.env` file
- `ALLOWED_HOSTS` should match the heroku URL for your app.
  - Click `Open app` button to see it
  - Leave out the `https://` and trailing slash.
  - E.g. snacks-api.herokuapp.com
- It can take a minute for the environment variable changes to take effect
- Once site is ready then see if you can log in, create snacks, etc.
  - It will be ugly because the styling was lost.
  - This is due to the Heroku file system's "ephemeral" nature
  - One way to handle issue is to run `collectstatic` locally then commit the `staticfiles` to heroku.