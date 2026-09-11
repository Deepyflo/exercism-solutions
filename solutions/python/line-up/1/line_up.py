def line_up(name, number):
    ordinal = ""
    if str(number).endswith("1") and not str(number).endswith("11"):
        ordinal = "st"
    elif str(number).endswith("2") and not str(number).endswith("12"):
        ordinal = "nd"
    elif str(number).endswith("3") and not str(number).endswith("13"):
        ordinal = "rd"
    else:
        ordinal = "th"
    return f"{name}, you are the {str(number) + ordinal} customer we serve today. Thank you!"