from flask_script import Manager
from flask_skeleton_api.main import app
import subprocess

manager = Manager(app)


@manager.command
def unittest(report=False):
    if report:
        subprocess.call(["py.test", "--junitxml=test-output/unit-test-output.xml",
                         "--cov-report=html:test-output/unit-test-cov-report"])
    else:
        subprocess.call(["py.test"])


@manager.command
def integrationtest(report=False):
    if report:
        subprocess.call(["py.test", "--junitxml=test-output/integration-test-output.xml",
                         "integration_tests"])
    else:
        subprocess.call(["py.test", "integration_tests"])


@manager.command
def runserver():
    app.run(debug=True, port=8080)

if __name__ == "__main__":
    manager.run()
