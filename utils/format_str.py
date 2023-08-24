import locale


def format_financial_number(input_number):
    number = float(input_number)
    # Save the current locale setting
    current_locale = locale.getlocale()

    # Set the locale to the desired financial format (e.g., en_US for US format)
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    # Format the number as a financial string
    formatted_number = locale.currency(number, grouping=True)

    # Reset the locale to the original setting
    locale.setlocale(locale.LC_ALL, current_locale)

    return formatted_number
