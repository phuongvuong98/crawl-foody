from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_mongoengine import MongoEngine
# db = SQLAlchemy()
db = MongoEngine()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)
    app.config['MONGODB_DB'] = 'crud'
    app.config['MONGODB_HOST'] = 'mongodb+srv://cluster0-aecmg.mongodb.net/crud?ssl=true&ssl_cert_reqs=CERT_NONE'
    app.config['MONGODB_USERNAME'] = 'nodejs'
    app.config['MONGODB_PASSWORD'] = 'Vuong0935986100'

    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'flask+mongoengine=<3'
    app.debug = True
    app.config['DEBUG_TB_PANELS'] = (
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel',
        'flask_mongoengine.panels.MongoDebugPanel'
    )

    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    db.init_app(app)

    from app.CRUD.city.views import city_blueprint
    # from app.CRUD.district.views import district_blueprint
    # from app.CRUD.color.views import color_blueprint
    # from app.CRUD.category.views import category_blueprint
    # from app.CRUD.store.views import store_blueprint
    # from app.CRUD.address.views import address_blueprint
    # from app.CRUD.product.views import product_blueprint
    # from app.CRUD.brand.views import brand_blueprint
    # from app.CRUD.product_variant.views import variant_blueprint
    #
    app.register_blueprint(city_blueprint, url_prefix='/city')
    # app.register_blueprint(district_blueprint, url_prefix='/district')
    # app.register_blueprint(color_blueprint, url_prefix='/color')
    # app.register_blueprint(category_blueprint, url_prefix='/category')
    # app.register_blueprint(store_blueprint, url_prefix='/store')
    # app.register_blueprint(address_blueprint, url_prefix='/address')
    # app.register_blueprint(product_blueprint, url_prefix='/product')
    # app.register_blueprint(brand_blueprint, url_prefix='/brand')
    # app.register_blueprint(variant_blueprint, url_prefix='/variants')

    return app
