def capture(driver, name):
    driver.save_screenshot(f"logs/{name}.png")
