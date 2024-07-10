# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Features

Some features

## Configuration

In `config.yaml` specify logging options, icon, etc.

```yaml
gui:
  icon: myicon.png
logger:
  handlers:
    stream:
      level: INFO
      bubble: false
    timed_rotating_file:
      level: INFO
      bubble: true
      date_format: '%Y-%m-%d'
```

## Dependencies

See `requirements.txt` for managed dependencies.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.
