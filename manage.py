from app import create_app
from flask_script import Manager

manager = Manager(create_app)
manager.add_option('-e', '--environment', dest='environment', required=True)

if __name__ == '__main__':
    manager.run()
