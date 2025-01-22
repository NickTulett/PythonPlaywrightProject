import re


class ChartPage:
    def __init__(self, page):
        self.page = page
        self.chart_frame = page.locator("iframe").content_frame
        self.first_chart_plots = self.chart_frame.get_by_label(re.compile("Actual CfD")).first.get_by_label("Plot area")

    def navigate(self):
        self.page.goto("https://www.lowcarboncontracts.uk/resources/scheme-dashboards/cfd-historical-data-dashboard/")

    def metric_elements(self, metric):
        return self.first_chart_plots.first.get_by_label(metric).get_by_role("option")

    def nth_value_of(self, metric, index):
        return self.metric_elements(metric).nth(index).get_attribute("aria-label")
