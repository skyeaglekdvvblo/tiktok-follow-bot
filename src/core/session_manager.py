class SessionManager:
    def __init__(self, driver):
        self.driver = driver

    def close(self):
        self.driver.quit()
