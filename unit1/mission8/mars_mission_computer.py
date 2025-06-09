import random
import time
import platform
import psutil


class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0
        }

    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 1)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 1)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 1)
        self.env_values['mars_base_external_illuminance'] = random.randint(500, 715)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 3)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 1)

    def get_env(self):
        return self.env_values


class MissionComputer:
    def __init__(self):
        self.env_values = {}
        self.ds = DummySensor()

    def dict_to_json(self, data, indent=2):
        def format_value(value):
            if isinstance(value, str):
                return f'"{value}"'
            else:
                return str(value)

        items = []
        for key, value in data.items():
            spaces = ' ' * indent
            items.append(f'{spaces}"{key}": {format_value(value)}')
        
        inner_content = ',\n'.join(items)
        return f'{{\n{inner_content}\n}}'

    def get_mission_computer_info(self):
        try:
            system_info = platform.uname()
            memory_gb = round(psutil.virtual_memory().total / (1024**3), 2)
            
            info = {
                'operating_system': system_info.system,
                'os_version': system_info.release,
                'cpu_type': system_info.processor,
                'cpu_cores': psutil.cpu_count(),
                'memory_size_gb': memory_gb
            }
            
            print(self.dict_to_json(info))
            
        except Exception as e:
            print(f'System info error: {str(e)}')

    def get_mission_computer_load(self):
        try:
            load_info = {
                'cpu_usage_percent': f'{round(psutil.cpu_percent(interval=1), 1)} %',
                'memory_usage_percent': f'{round(psutil.virtual_memory().percent, 1)} %'
            }
            
            print(self.dict_to_json(load_info))
            
        except Exception as e:
            print(f'Load info error: {str(e)}')

    def get_sensor_data(self):
        while True:
            self.ds.set_env()
            self.env_values = self.ds.get_env()
            print(self.dict_to_json(self.env_values))
            time.sleep(5)


if __name__ == '__main__':
    runComputer = MissionComputer()
    
    # 시스템 정보 출력
    runComputer.get_mission_computer_info()
    
    # 부하 정보 출력  
    runComputer.get_mission_computer_load()
