# Web product analyser

This project is a multi-agent system designed to intelligently extract product details from a given webpage. It uses **Google ADK**, **Playwright**, and an LLM-based agent framework to automate image capture of visual content.


## Overview
###  Scenario
The agent automatically navigates through a given website, intelligently identifies product or solution pages, and extracts meaningful content. It summarizes the available products and captures key product interface images that reflect real usage (e.g., dashboards or workflows).

### Input
A single website URL (e.g., homepage or landing page)


### Output
A comprehensive summary of all identified products, including descriptions and key differentiators. A set of relevant product screenshots (if available), each paired with a short caption describing its content or purpose.


### Technologies
- Google ADK – Multi-agent orchestration
- FastAPI – REST API interface
- Playwright – Browser automation

## Create and Activate a Virtual Environment

- `python3 -m venv venv`
- `source venv/bin/activate`

## Install Dependencies
- `pip install -r requirements.txt`
- `playwright install`

## Configure Environment Variables
Create a .env file with your Google API key .

## Run the Application

Start the FastAPI server:
`uvicorn main:app --reload`

Then make a POST request to run the agent:
`POST /run-agent`