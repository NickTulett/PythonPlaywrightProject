import re
from playwright.sync_api import Page, expect
import pytest
from pytest_check import check

from chartpage import ChartPage
from test_data import CfD_actuals_historic_values


@pytest.fixture(scope="function", autouse=True)
def chart_page(page: Page):
    chart_page = ChartPage(page)
    chart_page.navigate(chart_page.dashboards["CfD"]["Actuals"]["Historical Data"])
    yield chart_page


def test_has_title(chart_page):
    expect(chart_page.page).to_have_title(re.compile("CfD Historical Data"))


def test_has_two_charts(chart_page):
    expect(chart_page.chart_frame.get_by_label(re.compile("Actual CfD"))).to_have_count(2)
    expect(chart_page.chart_frame.get_by_text("2025 Qtr 1")).to_have_count(2)
    expect(chart_page.first_chart_plots).to_have_count(2)


def test_chart_has_all_metrics(chart_page):
    # chart has a bar stack per metric
    (expect(chart_page.first_chart_plots.first.get_by_role("listbox"))
     .to_have_count(len(CfD_actuals_historic_values.items())))
    # chart has 3 overlaid lines
    (expect(chart_page.first_chart_plots.last.locator("path"))
     .to_have_count(3))

@pytest.mark.parametrize("metric, values", CfD_actuals_historic_values.items())
def test_chart_values(chart_page, metric, values):
    for index, expected_value in enumerate(values):
        # need to subtract from index as I've only captured the 2 most recent values
        check.equal(chart_page.nth_value_of(metric, index - 2), expected_value)
