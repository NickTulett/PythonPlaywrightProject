import re



class ChartPage:
    base_url = "https://www.lowcarboncontracts.uk/resources/scheme-dashboards/"
    dashboards = {
        "CfD": {
            "Actuals": {
                "Allocation Rounds": "cfd-allocation-rounds",
                "Daily Levy Rates": "cfd-daily-levy-rates",
                "Historical Data": "cfd-historical-data-dashboard",
                "Operational Costs": "cfd-operational-costs-levy-dashboard",
                "Supplier Payments": "cfd-supplier-payments"
            },
            "Forecasts": {

            }
        },
        "CM": {
            "Actuals": {

            },
            "Capacity Provider": {

            },
            "Forecast": {
                "Cost": "forecast-dashboardcm"
            }
        }
    }

    def __init__(self, page):
        self.page = page
        self.chart_frame = page.locator("iframe").content_frame
        self.first_chart_plots = self.chart_frame.get_by_label(re.compile("Actual CfD")).first.get_by_label("Plot area")

    def navigate(self, dashboard_url):
        self.page.goto(f"{self.base_url}{dashboard_url}/")

    def metric_elements(self, metric):
        return self.first_chart_plots.first.get_by_label(metric).get_by_role("option")

    def nth_value_of(self, metric, index):
        return self.metric_elements(metric).nth(index).get_attribute("aria-label")
