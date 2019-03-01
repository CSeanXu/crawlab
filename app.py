from flask import Flask, logging
from flask_cors import CORS
from flask_restful import Api

from config import FLASK_HOST, FLASK_PORT
from routes.deploys import DeployApi
from routes.files import FileApi
from routes.nodes import NodeApi
from routes.spiders import SpiderApi
from routes.stats import StatsApi
from routes.tasks import TaskApi

# flask app instance
app = Flask(__name__)
app.config.from_object('config')

# init flask api instance
api = Api(app)

# cors support
CORS(app, supports_credentials=True)

# reference api routes
api.add_resource(NodeApi,
                 '/api/nodes',
                 '/api/nodes/<string:id>',
                 '/api/nodes/<string:id>/<string:action>')
api.add_resource(SpiderApi,
                 '/api/spiders',
                 '/api/spiders/<string:id>',
                 '/api/spiders/<string:id>/<string:action>')
api.add_resource(DeployApi,
                 '/api/deploys',
                 '/api/deploys/<string:id>',
                 '/api/deploys/<string:id>/<string:action>')
api.add_resource(TaskApi,
                 '/api/tasks',
                 '/api/tasks/<string:id>',
                 '/api/tasks/<string:id>/<string:action>'
                 )
api.add_resource(FileApi,
                 '/api/files',
                 '/api/files/<string:action>')
api.add_resource(StatsApi,
                 '/api/stats',
                 '/api/stats/<string:action>')

if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT)
