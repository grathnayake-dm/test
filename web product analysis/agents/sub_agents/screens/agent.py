import asyncio
from playwright.async_api import async_playwright
from model import MODEL
from google.adk.agents import Agent
from google.adk.tools.function_tool import FunctionTool

from typing import List, Dict
import asyncio
from playwright.async_api import async_playwright
from google.adk.tools.function_tool import FunctionTool
from .prompt import SCREEN_CAPTURING_PROMPT


async def get_all_images(urls: List[str]) -> Dict[str, List[str]]:

    image_data = {}
    all_images = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for url in urls:
            try:
                await page.goto(url, wait_until="networkidle")
                image_urls = await page.eval_on_selector_all(
                    "img", "elements => elements.map(el => el.src)"
                )
                all_images.extend(image_urls)
            except Exception as e:
                print(f"Failed to load {url}: {e}")

        await browser.close()

    return {
        "all_images": all_images
    }

extract_images_tool = FunctionTool(
    func=get_all_images,
)

screen_capturing_agent = Agent(
    name="product_screenshot_agent",
    model=MODEL,
    description="An agent that identifies the most relevant product UI screen image from each product page, summarizes it, and returns a JSON.",
    instruction=SCREEN_CAPTURING_PROMPT,
    tools=[extract_images_tool]
)
