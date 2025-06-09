import random
import time


class DummySensor:
    # 화성 기지 환경 센서 더미 클래스

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
        # 환경 값을 무작위로 생성하여 env_values에 저장
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 1)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 1)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 1)
        self.env_values['mars_base_external_illuminance'] = random.randint(500, 715)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 3)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 1)

    def get_env(self):
        # 현재 환경 값을 반환
        return self.env_values


class MissionComputer:
    # 화성 기지 미션 컴퓨터 클래스

    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0.0,
            'mars_base_external_temperature': 0.0,
            'mars_base_internal_humidity': 0.0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0.0,
            'mars_base_internal_oxygen': 0.0
        }
        self.ds = DummySensor()

    def dict_to_json(self, data, indent=2):
        # 딕셔너리를 JSON 형태의 문자열로 변환
        def format_value(value):
            if isinstance(value, str):
                return f'"{value}"'
            elif isinstance(value, bool):
                return 'true' if value else 'false'
            elif value is None:
                return 'null'
            else:
                return str(value)

        def format_dict(d, current_indent=0):
            if not d:
                return '{}'
            
            items = []
            for key, value in d.items():
                spaces = ' ' * (current_indent + indent)
                formatted_key = f'"{key}"'
                formatted_value = format_value(value)
                items.append(f'{spaces}{formatted_key}: {formatted_value}')
            
            inner_content = ',\n'.join(items)
            outer_spaces = ' ' * current_indent
            return f'{{\n{inner_content}\n{outer_spaces}}}'

        return format_dict(data)

    def get_sensor_data(self):
        # 센서 데이터를 가져와서 5초마다 JSON 형태로 출력
        while True:
            # 센서의 값을 가져와서 env_values에 담기
            self.ds.set_env()
            self.env_values = self.ds.get_env()
            
            # env_values의 값을 JSON 형태로 출력
            json_output = self.dict_to_json(self.env_values)
            print(json_output)
            
            # 5초 대기
            time.sleep(5)


if __name__ == '__main__':
    # MissionComputer 클래스를 RunComputer라는 이름으로 인스턴스화
    RunComputer = MissionComputer()
    
    # get_sensor_data() 메소드를 호출하여 지속적으로 환경 값 출력
    RunComputer.get_sensor_data()
