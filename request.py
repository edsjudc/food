import requests

# 访问 URL
url = 'https://food-ek2.pages.dev/'
response = requests.get(url)

# 打印响应信息
print(f"响应状态码: {response.status_code}")
print(f"响应内容: {response.text[:200]}")  # 打印前200个字符

# 记录其他信息，比如响应时间
print(f"响应时间: {response.elapsed.total_seconds()} 秒")
