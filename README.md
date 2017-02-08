[![Build Status](https://travis-ci.org/lsst-sqre/uservice-t04.svg?branch=master)](https://travis-ci.org/lsst-sqre/uservice-t04)

# sqre-uservice-t04

LSST DM SQuaRE api.lsst.codes-compliant microservice wrapper.  TODO

## Usage

`sqre-uservice-t04` will run standalone on port
5000 or under `uwsgi`.  It responds to the following routes:

### Routes

* `/`: returns `OK` (used by Google Container Engine Ingress healthcheck)

* `/t04`: TODO

### Returned Structure

The returned structure is JSON.  TODO.
