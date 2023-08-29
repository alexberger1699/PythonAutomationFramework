import os
import time


def get_base_url():
    env = os.environ.get('ENV', 'test')
    if env.lower()== 'test':
        return 'https://google.com'
    time.sleep(100000)