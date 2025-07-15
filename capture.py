from playwright.sync_api import sync_playwright
from datetime import datetime

def capture_profile_summary(username="feronline"):
    url = f"https://profile-summary-for-github.com/user/{username}"
    output_file = "profile_summary.png"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(5000)  # sayfa yüklenmesini bekle
        page.screenshot(path=output_file, full_page=True)
        browser.close()

        print(f"[{datetime.now()}] ✔ Görsel oluşturuldu: {output_file}")

if __name__ == "__main__":
    capture_profile_summary()
