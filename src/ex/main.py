import requests as rq
import click
from pathlib import Path
import json

cwd = Path(__file__).parent

def write_data(data:list[dict], file_name:str) -> list[dict]:
    Path(cwd / "data").mkdir(exist_ok=True)
    with open(cwd / f"data/{file_name}.json", "w") as file:
        json.dump(data, file, indent=4)

        return data

def get_data(base:str) -> tuple[list[dict], str]:
    file_path = Path(cwd / f"data/{base.upper()}.json")
    if file_path.exists():
        with open(file_path, "r") as file:
            return json.load(file), "local"

    url = "https://api.frankfurter.dev/v2/rates"
    payload = {"base": f"{base}"}

    response = rq.get(url, params=payload)

    try:
        response.raise_for_status()
    except rq.HTTPError as e: 
        raise click.ClickException(f"Error with contacting API at {url}: {e}")

    return write_data(response.json(), base.upper()), "api"

@click.command()
@click.argument("base", help="The base currency ISO 4217 code.")
@click.argument("quote", help="The quote currency ISO 4217 code.")
@click.argument("amount", help="The amount of currency you'd like to exchange from base to quote.", type=click.FLOAT)
@click.option("--debug", help="Sets the program to debug mode. Prints extra information", is_flag=True)
def cli(base:str, quote:str, amount:float, debug:bool):
    """CLI tool that exchanges any amount from one currency code to another."""

    if all((not base, not quote, len(base) > 4, len(quote) > 4)):
        raise click.BadArgumentUsage("Base and Quote code should follow the ISO 4217 standard.")

    base = base.lower().strip()
    quote = quote.lower().strip()
    rate = None

    exchange_rates, location_debug = get_data(base)

    for entry in exchange_rates:
        if entry.get("quote") == quote.upper():
            rate = entry.get("rate")
            break

    result = round(amount * rate, 3)

    print(f"{base.upper()} --> {quote.upper()} ({amount}) (RATE={rate}) = {result}")

    if debug:
        print(f"[DEBUG] Data fetched from {location_debug}")

if __name__ == "__main__":
    cli()
    




    