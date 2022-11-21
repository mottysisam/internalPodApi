import pod_info
import logging

from flask import Flask
from flask_restful import Resource, Api

logger = logging.getLogger('pod_info')

app = Flask(__name__)
api = Api(app)


class Root(Resource):
    def get(self):
        return {
            'info': {'message': ['please use the desired api endpoint, example: /info']}
        }


class PodInfo(Resource):
    def get(self):
        # get pod info from pod_info.py
        try:
            return pod_info.main()
        except Exception as exc:
            logger.exception(f"Get Pod Info failed, assuming it is unresponsive, {exc}")
            return False


api.add_resource(Root, '/')
api.add_resource(PodInfo, '/info')


if __name__ == "__main__":
    app.run()
