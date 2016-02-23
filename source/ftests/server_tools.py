# ftests/server_tools.py


from os import path
import subprocess
THIS_FOLDER = path.dirname(path.abspath(__file__))

def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email), #12
            '--host={}'.format(host),
            '--hide=everything,status', #3
        ],
        cwd=THIS_FOLDER
    ).decode().strip() #4


def reset_database(host):
    subprocess.check_call(
        ['fab', 'reset_database', '--host={}'.format(host)],
        cwd=THIS_FOLDER
    )
