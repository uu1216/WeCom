

from selenium import webdriver

class TestComiru():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_comiru(self):
        self.driver.get("https://comiru.net/teachers/login")
        self.driver.find_element_by_id("email").send_keys("angie.weber@weber.net")
        self.driver.find_element_by_id("password").send_keys("adHCj&}@L")
        self.driver.find_element_by_class_name('btn').click()








#        c_minute = "42"  　 #设置 分钟
#        c_hour = "8,17"　　　#设置 小时
#        c_week = "mon-fri"  #设置 日
#
# def work():
#     try:
#         driver = webdriver.Chrome()
#         driver.get("https://comiru.net/teachers/login")
#         #填充用户名 密码 验证码
 #browser.find_element_by_id("email").send_keys("angie.weber@weber.net")   #再chrome中安F12查找到你输入用户名文本框的 id 或者class 　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　  ：　用find_element_by_class_name 查找class
 #browser.find_element_by_id("password").send_keys("adHCj&}@L")
 #browser.find_element_by_class_name('btn').click() #找到你所需要点击按钮的class或者id 然后点击
#         # sleep(3)
#         # driver.quit()
#         print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ": Clock Success!")  #time.strftime格式化日期函数，获得当前系统时间
#     except:
#         print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ": Clock Filed!")
#
# if __name__ == '__main__':
#     # 添加任务
#     scheduler = BlockingScheduler()
#     # 设置定时任务时间
#     scheduler.add_job(work, 'cron', minute=c_minute, hour=c_hour, day_of_week=c_week)
#     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ": Add Task Work!")
#  #   try:
#  ##  except (KeyboardInterrupt, SystemExit):
#         scheduler.shutdown()