
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg)](https://opensource.org/licenses/MIT) [![PSM](https://img.shields.io/badge/dependency-myp-blue)](https://github.com/yunisdev/myp)

# PYPI starter template

This repo is starter template for [PYPI](https://pypi.org/) packages.



## Installation 

There is two ways to use this template:
- Generate with "Use with template" button
- Clone project and use it

### Generate with "Use with template" button

You can create your own repo from template by clicking green "Use this template" button on template repo page:

![App Screenshot](https://raw.githubusercontent.com/yunisdev/pypi-starter/main/assets/use_template_button.png)

### Clone project and use it

Clone repo from github to folder with your project name and delete `.git`, `assets` folders.

```bash 
> git clone https://github.com/yunisdev/pypi-starter.git
> cd pypi-starter
```

After, you can customize all the things with your needs. Example, you need to change folder name.

Don't forget to delete useless folders:

``` bash
> rm -rf .git
> rm -rf assets
```

`PYPI starter template` uses `MYP` for better user experience.
`MYP` is used for adding your credentials to setup.py and adding some other functionalities to your project while you are developing your project.
You just need to install `myp` and dependencies:
``` bash
> pip install --upgrade myp
> myp get:deps --dev
```

You can get more information about `MYP` by clicking [this link](https://github.com/yunisdev/myp).

**Note**: Do not forget to install requirements. Otherwise, nothing will work as expected.
## Deploy package

Run following command to deploy your project to `PYPI`:

```bash
> myp deploy
```

This command will build your project and deploy it to [pypi.org](https://pypi.org/)

`setup.py` will use version number from `myp.json` file.

To update project version, run following command and enter version number:

```bash
> myp set version
```

## Environment Variables

You can also use environment variables with the help of `snakenv` and `myp`.

When you run `myp deploy` or any other `myp` script, you can use environment variables from `.env` files.

If you want to use other `.env` files like `dev`, `prod`, `test`, you need to run:

```bash
> myp set environment
```

Enter name of environment you want and create file with name of `[ENV_NAME].env`.

For example, if you set `env` to `dev`, you need to create `dev.env` file.

**Note**: You will not be able to use environment variables when running your script outside `myp`.

You can disable environment variable usage by running:

```bash
> myp set use_environment -v "False"
```

And activate by running:

```bash
> myp set use_environment -v "True"
```
## License

[MIT](https://github.com/yunisdev/pypi-starter/blob/main/LICENSE)