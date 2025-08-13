from typing import List
from google.adk.tools.function_tool import FunctionTool
from google.adk.agents import Agent

from model import MODEL
from typing import List
from playwright.async_api import async_playwright

from .prompt import PRODUCT_PAGE_CALLING_PROMPT


async def extract_links_from_url(url: str) -> List[str]:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(url, wait_until="networkidle")
            hrefs = await page.eval_on_selector_all(
                "a",
                "elements => elements.map(el => el.href).filter(href => href)"
            )
            return hrefs
        finally:
            await browser.close()

extract_links_tool = FunctionTool(
    func=extract_links_from_url
)

product_page_calling_agent = Agent(
    name="product_page_calling_agent",
    model=MODEL,
    description="Agent that extracts and filters product-related sub-pages from a given company website.",
    tools=[extract_links_tool],
    instruction=PRODUCT_PAGE_CALLING_PROMPT
)
