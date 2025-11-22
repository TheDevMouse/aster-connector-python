import logging
import os
import sys
from typing import Optional, Any

# Import from the custom library
from aster.rest_api import Client
from aster.lib.utils import config_logging

def setup_environment() -> int:
    """
    Determines the logging level from environment variables.
    Defaults to INFO if not specified.
    """
    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    return getattr(logging, level_name, logging.INFO)

def fetch_ticker_data(client: Client, symbol: str) -> Optional[Any]:
    """
    Safely fetches ticker data with error handling.
    """
    try:
        logging.info(f"Fetching 24hr price change for {symbol}...")
        data = client.ticker_24hr_price_change(symbol)
        return data
    except Exception as e:
        # Catch network or API errors to prevent the script from crashing unexpectedly
        logging.error(f"Failed to fetch data for {symbol}: {e}")
        return None

def main():
    """
    Main execution entry point.
    """
    # 1. Configure Logging
    log_level = setup_environment()
