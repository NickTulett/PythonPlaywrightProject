import re
from playwright.sync_api import Page, expect
import pytest


# def test_has_title(page: Page):
#     page.goto("https://www.lowcarboncontracts.uk/resources/scheme-dashboards/cfd-historical-data-dashboard/")
#
#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("CfD Historical Data"))


def test_has_charts(page: Page):
    page.goto("https://www.lowcarboncontracts.uk/resources/scheme-dashboards/cfd-historical-data-dashboard/")
    chart_frame = page.locator("iframe").content_frame

    expect(chart_frame.get_by_label(re.compile("Actual CfD"))).to_have_count(2)
    expect(chart_frame.get_by_text("2025 Qtr 1")).to_have_count(2)

    first_chart_plots = chart_frame.get_by_label(re.compile("Actual CfD")).first.get_by_label("Plot area")
    expect(first_chart_plots).to_have_count(2)
    # chart has 7 bar stacks per date
    expect(first_chart_plots.first.get_by_role("listbox")).to_have_count(7)
    # chart has 3 overlaid lines
    expect(first_chart_plots.last.locator("path")).to_have_count(3)

    # check an Offshore wind value
    (expect(first_chart_plots.first
           .get_by_label("Offshore Wind").get_by_role("option").last)
                .to_have_attribute("aria-label", "773975.067"))
