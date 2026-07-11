cost_price = float(input("Enter the cost price of the game: "))
no_of_players_in_group = int(input("Enter the number of players in the group: "))
in_players = []

for i in range(no_of_players_in_group):
    player_name = input(f"Enter the name of the player {i+1}: ")
    in_status = int(input(f"Enter 1 for in, and 0 for out for {player_name}: "))
    if in_status == 1:
        in_players.append(player_name)

print("Players who are in:")
for player in in_players:
    print(player)

no_of_in_players = len(in_players)
if no_of_in_players == 0:
    print("No players in the game.")
else:
    cost_per_player = cost_price / no_of_in_players
    print(f"Cost per player: {cost_per_player}")

    in_paid_players = []
    paid_amounts = []
    for player in in_players:
        paid_status = int(input(f"Did {player} pay? Enter 1 for yes, 0 for no: "))
        if paid_status == 1:
            paid_amt = float(input(f"Enter the amount paid by {player}: "))
            in_paid_players.append(player)
            paid_amounts.append(paid_amt)

    unpaid_players = []
    for player in in_players:
        if player not in in_paid_players:
            unpaid_players.append(player)

    print(f"\nNumber of unpaid players: {len(unpaid_players)}")
    print(f"Unpaid players: {unpaid_players}")

    balances = []
    for player in in_players:
        if player in in_paid_players:
            paid_amt = paid_amounts[in_paid_players.index(player)]
        else:
            paid_amt = 0
        balance = paid_amt - cost_per_player
        balances.append([player, balance])

    debtors = []
    creditors = []
    for entry in balances:
        player = entry[0]
        amount = entry[1]
        if amount < 0:
            debtors.append([player, abs(amount)])
        elif amount > 0:
            creditors.append([player, amount])

    print("WHO OWES WHO: ")
    i = 0
    j = 0
    while i < len(debtors) and j < len(creditors):
        debtor_name = debtors[i][0]
        debtor_amt = debtors[i][1]
        creditor_name = creditors[j][0]
        creditor_amt = creditors[j][1]

        if debtor_amt > creditor_amt:
            print(f"{debtor_name} owes {creditor_name} Rs. {creditor_amt:.2f}")
            debtors[i][1] = debtor_amt - creditor_amt
            creditors[j][1] = 0
            j += 1
        elif debtor_amt < creditor_amt:
            print(f"{debtor_name} owes {creditor_name} Rs. {debtor_amt:.2f}")
            debtors[i][1] = 0
            creditors[j][1] = creditor_amt - debtor_amt
            i += 1
        else:
            print(f"{debtor_name} owes {creditor_name} Rs. {debtor_amt:.2f}")
            debtors[i][1] = 0
            creditors[j][1] = 0
            i += 1
            j += 1

    print("\nFinal Balances: ")
    for entry in balances:
        player = entry[0]
        amount = entry[1]
        if amount < 0:
            print(f"{player} still needs to pay Rs. {abs(amount):.2f}")
        elif amount > 0:
            print(f"{player} should receive Rs. {amount:.2f}")
        else:
            print(f"{player} is settled")
