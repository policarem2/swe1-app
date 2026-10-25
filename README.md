
# SWE1 Django Polls Application

This project uses automated CI/CD with Travis CI.
[![Build Status](https://app.travis-ci.com/policarem2/swe1-app.svg?branch=main)](https://app.travis-ci.com/policarem2/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/policarem2/swe1-app/badge.svg)](https://coveralls.io/github/policarem2/swe1-app)

A Django web application developed for my Software Engineering course. The project allows users to vote in polls and view their results.

The application is deployed on AWS Elastic Beanstalk and uses Travis CI for automated testing and deployment.

## Live Application

[View the deployed application](http://swe1-app-env.eba-ibhwm3d7.us-east-2.elasticbeanstalk.com)

## Technologies Used

- Python 3.11
- Django
- AWS Elastic Beanstalk
- Travis CI
- Black and Flake8
- Coverage.py and Coveralls

## Continuous Integration and Deployment

Travis CI automatically performs the following checks:

- **Black:** Checks Python code formatting.
- **Flake8:** Checks code style and linting.
- **Django system checks:** Validates the Django project configuration.
- **Django tests:** Runs automated tests.
- **Coverage.py:** Measures test coverage.
- **Coveralls:** Reports test coverage results.

Successful builds on the `main` branch automatically deploy to AWS Elastic Beanstalk.

## Test Coverage

Test coverage is measured using Coverage.py and reported through Coveralls.

<!-- Coveralls badge will be added here. -->
