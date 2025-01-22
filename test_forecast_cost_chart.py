import re
from playwright.sync_api import Page, expect
import pytest
from pytest_check import check
import csv

from chartpage import ChartPage
from test_data import data_from_csv


@pytest.fixture(scope="function", autouse=True)
def chart_page(page: Page):
    chart_page = ChartPage(page)
    chart_page.navigate(chart_page.dashboards["CM"]["Forecast"]["Cost"])
    yield chart_page


def test_has_title(chart_page):
    expect(chart_page.page).to_have_title(re.compile("CM Forecast Cost"))


def test_has_one_chart(chart_page):
    expect(chart_page.chart_frame.get_by_label(re.compile("Forecast Capacity Payments"))).to_have_count(1)

@pytest.mark.parametrize("datum", data_from_csv("cm_forecast_cost.csv"))
def test_chart_values(chart_page, datum):
    check.almost_equal(chart_page.value_of(datum), float(datum["Monthly_CM_Forecast_Cost_GBP"]), abs=0.0001)
