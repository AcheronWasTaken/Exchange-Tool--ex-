# Exchange Rate CLI Tool

## Description
This project is a small CLI tool that quickly converts an input amount from one currency code to another. That's it.

![Short video of the command terminal. "ex usd aud 1000" is being inputted, and the output is "USD --> AUD (1000) (Rate=1.4436) = 1443.5"](assets/Markdown/Gifs/example.gif)

## Features
- Uses the public and open source Frankfurter API at https://api.frankfurter.dev/v2/rates (Github: `https://github.com/lineofflight/frankfurter`).
- Caches data received from the API, meaning similar commands does not need to contact the API again, reducing execution time.

## Installation guide
1. Navigate the releases section and find the `.whl` file (wheel)
2. Ensure `pipx` is installed globally on your system, and that `pipx ensurepath` has been ran at least once. You can use `python -m pip install pipx` on any non-venv terminal to install it.
3. Run `pipx install <path to your wheel file>`.
4. `ex` should be available globally as command now.

## Usage
Run `ex --help` to get help on required parameters. General syntax is `ex <base-code> <quote-code> <amount>`.





