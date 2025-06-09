import random
import time
import platform
import psutil
import threading
import multiprocessing


class DummySensor:
    def __init__(self):
        self.env_values = {}

    def set_env(self):
        self.env_values = {
            'mars_base_internal_temperature': round(random.uniform(18, 30), 1),
            'mars_base_external_temperature': round(random.uniform(0, 21), 1),
            'mars_base_internal_humidity': round(random.uniform(50, 60), 1),
            'mars_base_external_illuminance': random.randint(500, 715),
            'mars_base_internal_co2': round(random.uniform(0.02, 0.1), 3),
            'mars_base_internal_oxygen': round(random.uniform(4, 7), 1)
        }

    def get_env(self):
        return self.env_values


class MissionComputer:
    def __init__(self, name='Computer'):
        self.ds = DummySensor()
        self.name = name

    def dict_to_json(self, data):
        items = [f'  "{k}": "{v}"' if isinstance(v, str) else f'  "{k}": {v}' for k, v in data.items()]
        return '{\n' + ',\n'.join(items) + '\n}'

    def get_mission_computer_info(self):
        while True:
            try:
                info = platform.uname()
                data = {
                    'os': info.system,
                    'version': info.release,
                    'cpu': info.processor,
                    'cores': psutil.cpu_count(),
                    'memory_gb': round(psutil.virtual_memory().total / (1024**3), 2)
                }
                print(f'[{self.name}] System:\n{self.dict_to_json(data)}')
            except Exception as e:
                print(f'[{self.name}] Error: {e}')
            time.sleep(20)

    def get_mission_computer_load(self):
        while True:
            try:
                data = {
                    'cpu_percent': f'{round(psutil.cpu_percent(interval=1), 1)}%',
                    'memory_percent': f'{round(psutil.virtual_memory().percent, 1)}%'
                }
                print(f'[{self.name}] Load:\n{self.dict_to_json(data)}')
            except Exception as e:
                print(f'[{self.name}] Error: {e}')
            time.sleep(20)

    def get_sensor_data(self):
        while True:
            try:
                self.ds.set_env()
                data = self.ds.get_env()
                print(f'[{self.name}] Sensor:\n{self.dict_to_json(data)}')
            except Exception as e:
                print(f'[{self.name}] Error: {e}')
            time.sleep(5)


def run_thread():
    computer = MissionComputer('Thread')
    threads = [
        threading.Thread(target=computer.get_mission_computer_info, daemon=True),
        threading.Thread(target=computer.get_mission_computer_load, daemon=True),
        threading.Thread(target=computer.get_sensor_data, daemon=True)
    ]
    for t in threads:
        t.start()
    time.sleep(30)


def run_process(func, name):
    computer = MissionComputer(name)
    getattr(computer, func)()


def run_multiprocess():
    processes = [
        multiprocessing.Process(target=run_process, args=('get_mission_computer_info', 'Process1')),
        multiprocessing.Process(target=run_process, args=('get_mission_computer_load', 'Process2')),
        multiprocessing.Process(target=run_process, args=('get_sensor_data', 'Process3'))
    ]
    for p in processes:
        p.start()
    time.sleep(30)
    for p in processes:
        p.terminate()
        p.join()


if __name__ == '__main__':
    print('=== Multi-Thread ===')
    run_thread()
    print('\n=== Multi-Process ===')
    run_multiprocess()
