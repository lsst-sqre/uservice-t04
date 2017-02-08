#!/usr/bin/env python
"""t04 microservice framework.
"""
# Python 2/3 compatibility
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError
from apikit import APIFlask
from apikit import BackendError
from flask import jsonify


def server(run_standalone=False):
    """Create the app and then run it.
    """
    # Add "/t04" for mapping behind api.lsst.codes
    app = APIFlask(name="uservice-t04",
                   version="0.0.1",
                   repository="https://github.com/sqre-lsst/uservice-t04",
                   description="Microservice Test 04",
                   route=["/", "/t04"],
                   auth={"type": "bitly-proxy",
                         "data": {"username": "",
                                   "password": "",
                                   "endpoint": "https://FIXME-BACKEND-URL/oauth2/start" }})
    app.config["SESSION"] = None

    @app.errorhandler(BackendError)
    # pylint can't understand decorators.
    # pylint: disable=unused-variable
    def handle_invalid_usage(error):
        """Custom error handler.
        """
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @app.route("/")
    def healthcheck():
        """Default route to keep Ingress controller happy.
        """
        return "OK"

    @app.route("/t04")
    @app.route("/t04/")
    # @app.route("/t04/<parameter>")
    # or, if you have a parameter, def route_function(parameter=None):
    def route_function():
        """Microservice Test 04
        """
        # FIXME: service logic goes here
        # See https://sqr-015.lsst.io for details.
        # - store HTTP session in app.config["SESSION"]
        # - raise errors as BackendError
        # - return your results with jsonify
        # - set status_code on the response as needed
        return

    if run_standalone:
        app.run(host='0.0.0.0', threaded=True)
    # Otherwise, we're running under uwsgi, and it wants the app.
    return app


def standalone():
    """Entry point for running as its own executable.
    """
    server(run_standalone=True)


if __name__ == "__main__":
    standalone()
