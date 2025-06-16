## Setup

* Clone the repo with `git clone -b sdk https://github.com/browserstack/pytest-browserstack.git`
* It is recommended to use a virtual environment to install dependencies. To create a virtual environment:
  ```
  python3 -m venv env
  source env/bin/activate # on Mac
  env\Scripts\activate # on Windows
  ```
* Install dependencies `pip install -r requirements.txt`
* To run your automated tests using BrowserStack, you must provide a valid username and access key. This can be done either by providing your username and access key in the `browserstack.yml` configuration file, or by setting the `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` environment variables.

## Run sample test:
* To run the sample test across platforms defined in the 'browserstack.yml' file run:

`browserstack-sdk pytest -s -m sample_test`
