data = [
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
    ["Bob", 35, "Chicago"]
]

# JSON 형식의 문자열 생성
json_string = "[\n"
for i, sublist in enumerate(data):
    list_string = ", ".join(f'"{item}"' if isinstance(item, str) else str(item) for item in sublist)
    json_string += f'    [{list_string}]'
    if i < len(data) - 1:
        json_string += ",\n"
    else:
        json_string += "\n"
json_string += "]"

# 파일에 쓰기
with open('data.json', 'w') as f:
    f.write(json_string)