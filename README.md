# Fitness Manager
Take care of hearth and fitness with this application, using a database to store data about your progress, of course.

Our license is found here: [LICENSE](LICENSE).

## Summary

1. [Description](#description)
2. [Dependencies](#dependencies)
3. [How To Run?](#how-to-run)
   1. [Testing](#testing)
4. [Enums](#enums)
5. [Models](#models)
6. [Structure](#structure)
7. [Frequent Asks](#frequent-asks)

## Description
This project is a **CLI** (command line) application using a user account to auth and use their services.

The objective is to help those whom want to keep their health safe and take care or their bodies.

## Dependencies
The project main dependencies list.

* [Python](https://python.org)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* [Python DotEnv](https://github.com/theskumar/python-dotenv)
* [Pytest](https://docs.pytest.org/en/stable/)
* [Pytest Asyncio](https://pytest-asyncio.readthedocs.io/en/latest/)
* [Pydantic](https://docs.pydantic.dev/latest/)

You can install each one following their docs, but I suggest you install all them by the [requirements.txt](requirements.txt) file:

```commandline
pip install -r requirements.txt
```

## How To Run?
### Testing
## Enums
The python enumerates for this project:

```python
EnumGender = {
    "MALE": "male",
    "FEMALE": "female",
    "NOT_SAY": "not-say"
}
```

```python
EnumIntensity = {
    "SEDENTARY": "1.2",
    "LIGHTLY_ACTIVE": "1.375",
    "MODERATELY_ACTIVE": "1.55",
    "HIGHLY_ACTIVE": "1.725",
    "VERY_ACTIVE": "1.9"
}
```

Where:

| Sedentary                 | BRM | Lightly                     | BRM   | Moderately                    | BRM  | Highly                   | BRM   | Very | BRM |
|---------------------------|-----|-----------------------------|-------|-------------------------------|------|--------------------------|-------|-----|-----|
| little or no exercise | 1.2 | light activity 1-3 days/week | 1.375 | moderate activity 3-5 days/week | 1.55 | intense  activity 6-7 days/week | 1.725 | very intense activities, such as training for athletes | 1.9 |


## Models
Models of this project.

```python
User = {
  "full_name": "full name",
  "date_born": "YYYY-MM-DD",
  "gender": "EnumGender",
  "height": "NNN as cm",
  "weight": "decimal(n.nnn)",
}
```
```python
BMetabolicRate = {
    "weight": "decimal(n.nnn)",
    "height": "NNN as cm",
    "age": "integer",
    "gender": "EnumGender"
}
```
```python
BRMIntensity = {
    "tmb_brm": "decimal(n.n...)",
    "intensity": "EnumIntensity"
}
```

## Structure
Here you can found our project packages structure.

```text
.github/
src/
|---controllers/
|---core/
|---database/
|---enums
|---models/
|---prototypes/
|---repositories/
|---services/
|---utilities/
|---views/
tests/
|---controllers/
|---core/
|---services/
.env.example
.gitignore
app.py
LICENSE
README.md
requirements.txt
```

## Frequent Asks

---
That's all folks!
[Go ahead!](#fitness-manager)
