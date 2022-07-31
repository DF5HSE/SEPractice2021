# Kekos+

<!-- Add buttons here -->

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/DF5HSE/SE2021Practice?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/DF5HSE/SE2021Practice)
![GitHub issues](https://img.shields.io/github/issues-raw/DF5HSE/SE2021Practice)
![GitHub pull requests](https://img.shields.io/github/issues-pr/DF5HSE/SE2021Practice)
![GitHub](https://img.shields.io/github/license/DF5HSE/SE2021Practice)

<!-- Describe your project in brief -->

You are at the repository of the revolutionary project called "Kekos+". Our goal is to create super cool AR technology which allows people to play different sport games (e.g. tennis, ping-pong) anywhere while only needing a mobile phone and our devices with no additional inventory required. Once this project is finished everyone will say **"It's a revolution, Jhony"**. The name is inspired by a variable from some production code. More about the project in [this presentation](https://docs.google.com/presentation/d/1MCz6UrpTSqI-dBRKP3hgpjwFdbOWcO_p6LlD_ICNgVc/edit?usp=sharing).


# Table of contents

- [Table of contents](#table-of-contents)
- [Roadmap](#roadmap)
- [Installation](#installation)
- [Usage](#usage)
- [Contribute](#contribute)
    - [Sponsor](#sponsor)
    - [Adding new features or fixing bugs](#adding-new-features-or-fixing-bugs)
- [Project status](#project-status)
- [Authors and contacts](#authors-and-contacts)
- [License](#license)
- [Footer](#footer)

# Roadmap
Our roadmap for this project can be found [here](https://github.com/DF5HSE/SE2021Practice/projects/1). Fill free to share your ideas! 

Project changelog is available [here](https://github.com/DF5HSE/SE2021Practice/blob/readme/CHANGELOG.md).

# Installation
[(Back to top)](#table-of-contents)

To run our project, first clone the repo on your device using the command below:

```git init```

```git clone https://github.com/DF5HSE/SE2021Practice.git```

Make sure you have Python3 and pip installed on your device. Perform installation by running 

```python3 build-system-script.py install-depends```

You may run tests to check whether everyting is OK by running

```python3 build-system-script.py test```

# Usage
[(Back to top)](#table-of-contents)

Now our team is developing user administration system. By now we have implemented:
- the database prototype and functions for using it. You can try it by
importing `src.databse.user` module.
- the utilities' module. By now it contains function for password validation,
which will be used in new user registration process. You can try it by
importing `src.utils` module.
- the REST API with endpoints for registration new users and authorization
of existing ones. You can launch local server by `python3 -m uvicorn main:app --reload`
command and try out endpoins in your browser on http://127.0.0.1:8000/docs

Also, we write `build-system-script.py`. You can launch it by:
`python3 build-system-script.py <command>`. Available commands are:
- `install-depends` -- install dependencies, listed in `requirements.txt`.
- `type-check` -- run [mypy](https://mypy.readthedocs.io/en/stable/), which check matching
of types in source python files.
- `flake8` -- run [flake8](https://flake8.pycqa.org/en/latest/index.html) linter above source files
- `pylint` -- run [pylint](https://www.pylint.org/) linter above source files
- `test` -- run tests.
- `check-coverage` -- check coverage of source files by tests.
- `all-checks` -- run all checks commands.

# Contribute
[(Back to top)](#table-of-contents)

We welcome anyone to contribute into our project.

### Sponsor
[(Back to top)](#table-of-contents)

Just send money to our credit card with the following number xxxx-xxxx-xxxx-xxxx. Thanks a lot. Names of top donatros won't be forgiven.

### Adding new features or fixing bugs
[(Back to top)](#table-of-contents)

Create an issue on a problem that you found or a feature that you'd like to prupose or going to add to our project. 

If you wish to create features by your own just create a new branch with informative name, push updates and create a new pull request with the link to the corresponding issue.

# Project status
[(Back to top)](#table-of-contents)

Project is in development but already is ready for a revolution.

# Authors and contacts
[(Back to top)](#table-of-contents)

Denis Tarasov (GitHub: DT6A), Alina Ushakova (GitHub: AlinaUsh), Denis Filippov (GitHub: DF5HSE).

# License
[(Back to top)](#table-of-contents)

[MIT licenses](https://opensource.org/licenses/MIT)

# Footer
[(Back to top)](#table-of-contents)

Leave a star in GitHub and wait for upcomming updates and news!

