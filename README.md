# wp-test-demo-python
Project to demonstrate my coding ability in Python, specifically using REST APIs to test a local Wordpress site. This is a port of my wp-test-demo-java project from Java into Python.

This suite of test cases runs against an example Wordpress site. It uses Wordpress REST API endpoints to retrieve data about the test site, and analyzes JSON payloads returned by these endpoints.

In Phase 1 of this demo, I am working with the endpoints that provide publicly available data, such as the posts, categories, tags, and pages visible on the site.

## Prerequisites
To run this suite, I set up a test Wordpress site using Docker Compose. You can see the wp-docker-compose.yml file I use to set up the containers on my [misc-configs repo](https://github.com/annathepiper/misc-configs/blob/master/docker-compose.yml).

I also add aliases for wordpress.local and phpmyadmin.local to my hosts file, so that those URLs will work as the automation runs.

The test data I'm using is a copy of one of my [live Wordpress sites](http://angelahighland.info), which has provided me the items to fill in for the helper library WPTestLib. WPTestLib is a port of the properties file I use over in the Java version of this project.

The main tool I'm using to run the suite is PyCharm, and the version of Python I'm working with is 3.7. I'm using Nosetests as the test runner, as that's what I used in my prior experience on my last day job, and PyCharm supports it.

Overall, I'm setting up this suite in Python similarly to how I wrote similar test suites on my previous day job.

## Skills and tech I'm demonstrating here
* Use of the Python Requests library to do REST API calls and get JSON back
* Use of a helper class to set test-specific strings like ID numbers, titles, and names
* Using Nose functionality to run the test suite, and to annotate test methods
* Testing against a site running as a Docker container
* Negative test cases

## Running the code yourself

If you'd like to try running this suite yourself, you will need to do the following:

1. Install PyCharm if you don't have it already. (Or your Python IDE of choice; maybe you like Eclipse?)
2. Install Docker if you don't have it already.
3. Install git if you don't have it already.
4. Edit your local hosts file to add aliases for wordpress.local to 127.0.0.1 (and phpmyadmin.local if you're using my PHPMyAdmin container).
5. Create a local Wordpress instance with Docker (see my misc-configs repo for a wp-docker-compose.yml you can use as a reference, and modify as appropriate for your testing).
6. Configure your local Wordpress with whatever test data you want to use. This may involve importing data of your own in from another site, or otherwise generating test posts, pages, etc. via whatever means you have available.
7. Check out this repo on your own system.
8. Import the project into your PyCharm (or other IDE of choice).
9. Open the WPTestLib.py file and edit its strings as appropriate to reflect what test data you're using.
10. If you use my Postman collection and environment, you should also tweak the environment settings to reflect your test data. The environment file should match what you put into the WPTestLib.py file in PyCharm.
11. To run the tests, you have a few options. You can set up a configuration in PyCharm to use nose as your test runner, and run the tests directly in PyCharm. Or, if you have nose independently installed, you can go to the directory where you've checked out the code and run it from there. (This latter option is my current preference, as I've observed that running the tests within PyCharm gives me garbled output. This is apparently a known issue; I've seen other users reporting this when I went googling for information about it.)

## Why Nose?
I'm aware that the original version of Nose is in maintenance mode, and its docs do encourage people to use Nose2 instead. For the time being, though, I'm using Nose as that's what I'm most immediately familiar with. Time permitting, I'll be updating this suite to use Nose2.

## Running the code on a Linux environment
This code has been successfully most recently run against PyCharm Community Edition 2020.1.2, on an Ubuntu Linux install (Ubuntu 20.04 LTS) with Python version 3.8 installed.

## Reference links
* [Misc-configs repo](https://github.com/annathepiper/misc-configs) where I store my Docker Compose yml files
* [Java version of this project](https://github.com/annathepiper/wp-test-demo-java)
* [Nose](https://nose.readthedocs.io/en/latest/), the testing framework I'm using
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Requests library](http://docs.python-requests.org/en/master/)
