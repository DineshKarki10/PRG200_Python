def ticket_price():
    price_map = {"Regular": 300, "Gold": 500, "Platinum": 1000}

    user_input = input("Enter seat type and count (e.g. Regular, 2, Gold, 5, Platinum, 4): ")
    entries = [x.strip() for x in user_input.split(",")]

    grand_total = 0
    sections = {}

    for i in range(0, len(entries), 2):
        seat_type = entries[i]
        count = int(entries[i + 1])
        price = price_map[seat_type]
        subtotal = price * count
        grand_total += subtotal
        sections[seat_type] = (count, subtotal)

    for seat_type, (count, subtotal) in sections.items():
        print(f"{seat_type}: {count} x {price_map[seat_type]} = {subtotal}")

    print(f"Total: {grand_total}")


ticket_price()
