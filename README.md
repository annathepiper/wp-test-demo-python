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

## Why Nose?
I'm aware that the original version of Nose is in maintenance mode, and its docs do encourage people to use Nose2 instead. For the time being, though, I'm using Nose as that's what I'm most immediately familiar with. Time permitting, I'll be updating this suite to use Nose2.

## Reference links
* [Misc-configs repo](https://github.com/annathepiper/misc-configs) where I store my Docker Compose yml files
* [Java version of this project](https://github.com/annathepiper/wp-test-demo-java)
* [Nose](https://nose.readthedocs.io/en/latest/), the testing framework I'm using
* [PyCharm](https://www.jetbrains.com/pycharm/)
* [Requests library](http://docs.python-requests.org/en/master/)
