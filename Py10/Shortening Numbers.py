def shorten(suffixes, base):
    def transform_number(number):
        if isinstance(number, str) and number.isdigit():
            number = int(number)
            for suffix in suffixes:
                if number < base:
                    return f"{number} {suffix}"
                number //= base
        return str(number)
    return transform_number
