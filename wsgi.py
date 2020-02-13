import os
from app.server import create_app

# Get environment from variable
env = os.getenv('ENV', 'LOCAL')
debug = os.getenv('BRANDI_DEBUG')

application = create_app(env=env)

if __name__ == "__main__":
    application.run(debug=debug)
