# Python-API-Testing
Testing Python APIs

## Sections.
- Introduction - Brief intro of the article and setup of the application.
- Test Driven Development(TDD) - A bit of explanation on TDD.
- Utilizing Mocks - Explain the concept of mocking and different ways of mocking as follows.
  - Using Decorators
  - Using a Context Manager
  - Using a Patcher
- Mocking the whole function behavior - Demonstrate and explain how its done.
- Mocking third party functions - Demonstrate and explain how to mock out own functions/modules in other functions.
- Continuous integration with Circle CI - Brief walk through of how to combine testing and CI to make our development smooth, use case Github and Circle CI.
- Conclusion - Brief summary touching on mocking and CI.

## Setup.
 ```sh
$ git clone git@github.com:kimobrian/Python-API-Testing.git
$ cd Python-API-Testing
$ virtualenv -p python3 venv   # Create virtual environment
$ source venv/bin/activate # Activate virtual environment
$ pip install -r requirements.txt
 ```
