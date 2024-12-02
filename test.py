from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
import time
import random

def visit_website(url, driver_path):
    """访问指定 URL 的函数"""
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 无头模式
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")  # 避免共享内存问题

        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        time.sleep(random.uniform(1, 5))  # 随机等待
        print(f"访问页面: {url}, 页面标题: {driver.title}")
    except Exception as e:
        print(f"线程访问 {url} 时发生错误: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass

# 设置 WebDriver 路径
driver_path = r'C:\Program Files\Google\Chrome\Application\chromedriver.exe'

# 定义多个 URL
urls = [
    'https://food-ek2.pages.dev/',
    'https://food-ek2.pages.dev/%E5%8F%8C%E7%9A%AE%E5%A5%B6/shunde-doublenail',
    'https://food-ek2.pages.dev/%E9%99%88%E6%9D%91%E7%B2%89/shunde-chencunfen',
    'https://food-ek2.pages.dev/%E9%B1%BC%E7%94%9F/shunde-fishslices',
    'https://food-ek2.pages.dev/%E5%A7%9C%E6%92%9E%E5%A5%B6/shunde-gingermilk',
]

# 使用 ThreadPoolExecutor 限制最大线程数
max_threads = 5

# 使用 ThreadPoolExecutor 进行线程池管理
with ThreadPoolExecutor(max_threads) as executor:
    futures = [executor.submit(visit_website, url, driver_path) for url in urls]

# 无需手动 join，线程池会自动管理线程的启动和结束
