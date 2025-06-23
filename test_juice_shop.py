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

@pytest.mark.parametrize("payload", ["Bonus Payload", "DOM XSS"])
def test_injecting_xss(juice_shop, payload, api_request_context):
    juice_shop.open_shop()
    juice_shop.search_for(juice_shop.xss[payload])
    check.equal(True, juice_shop.check_challenge_solved(payload, api_request_context))
