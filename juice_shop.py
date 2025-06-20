import pytest


class JuiceShop:
    base_url = "https://stc-owasp-juice-dnebatcgf2ddf4cr.uksouth-01.azurewebsites.net"
    # privacy_policy = "privacy-security/privacy-policy"
    # score_board = "score-board"
    pages = {
        "Privacy Policy": "privacy-security/privacy-policy",
        "Score Board": "score-board"
    }

    def __init__(self, page):
        self.page = page

    def open_shop(self):
        self.page.goto(f"{self.base_url}/#/")

    def open_page(self, page_name):
        self.page.goto(f"{self.base_url}/#/{self.pages[page_name]}")

    def check_challenge_solved(self, challenge, api_request_context):
        challenge_statuses = api_request_context.get(f"/api/Challenges/?name={challenge}").json()
        return challenge_statuses["data"][0]["solved"]


