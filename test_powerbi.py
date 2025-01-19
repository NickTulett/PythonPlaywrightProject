import re
from playwright.sync_api import Page, expect
import pytest


def test_has_title(page: Page):
    page.goto("https://www.lowcarboncontracts.uk/resources/scheme-dashboards/cfd-historical-data-dashboard/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("CfD Historical Data"))


def test_has_charts(page: Page):
    page.goto("https://www.lowcarboncontracts.uk/resources/scheme-dashboards/cfd-historical-data-dashboard/")

    expect(page.get_by_role())