import pytest


class JuiceShop:
    base_url = "https://stc-owasp-juice-dnebatcgf2ddf4cr.uksouth-01.azurewebsites.net"
    pages = {
        "Privacy Policy": "privacy-security/privacy-policy",
        "Score Board": "score-board"
    }
    xss = {
        "Bonus Payload": '<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>',
        "DOM XSS": '<iframe src="javascript:alert(`xss`)">'
    }
    search_button = "#searchQuery"
    search_input = "app-mat-search-bar input"

    def __init__(self, page):
        self.page = page

    def open_shop(self):
        self.page.goto(f"{self.base_url}/#/")
        self.page.get_by_text("Dismiss").click()
        self.page.get_by_text("But me wait!").click()

    def open_page(self, page_name):
        self.page.goto(f"{self.base_url}/#/{self.pages[page_name]}")

    def search_for(self, search_term):
        self.page.locator(self.search_button).click()
        self.page.locator(self.search_input).fill(search_term)
        self.page.locator(self.search_input).press("Enter")

    def check_challenge_solved(self, challenge, api_request_context):
        challenge_statuses = api_request_context.get(f"/api/Challenges/?name={challenge}").json()
        return challenge_statuses["data"][0]["solved"]


