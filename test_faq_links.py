import pytest
from playwright.sync_api import Page

pages = [
    "https://www.lowcarboncontracts.uk/resources/faqs/supplier-cfd-rab-faqs/",
    "https://www.lowcarboncontracts.uk/resources/faqs/contracts-for-difference-faqs/",
    "https://www.lowcarboncontracts.uk/resources/faqs/why-cannot-cmu-portfolios-be-modelled/"
]
@pytest.mark.parametrize("faq_page", pages)
def test_links(page: Page, faq_page):
    print("\n\n\nPAGE:", faq_page)
    page.goto(faq_page)
    faq_sections = page.locator(".os-faq")
    for faq_section in faq_sections.all():
        faq_links = faq_section.locator("a")
        for faq_link in faq_links.all():
            print('\nLINK TEXT:', faq_link.text_content())
            href = faq_link.get_attribute("href")
            if href:
                print("LINK HREF:", href)
                page.goto(href)
                if page.get_by_role("heading", name="Not Found").is_visible():
                    print("BROKEN LINK!")
                else: print("LINK OK")
                page.go_back()
            else: print("MISSING LINK!")

