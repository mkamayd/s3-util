# get Name, Last_Modified and Size from any S3 bucket subpath

## prequisites
- python (python --version)
- pip (pip --version)
- virtualenv (virtualenv --version) (pip install virtualenv)

## installation
- on the root of the project run
    * `virtualenv venv`
    * `touch .env`

## configure .env
``` txt
REGION_NAME=us-east-1
AWS_ACCESS_KEY_ID=*********************
AWS_SECRET_ACCESS_KEY=*******************
BUCKET_NAME=the-bucket-name
FILE_NAME_PREFIX=2020/01/
```

## before running activate the virtual environment
`source venv/bin/activate`

## install packages (first time only)
`pip install -r requirements.txt`

## to run it
`python main.py`

## when done with it, deactivate:
`deactivate`