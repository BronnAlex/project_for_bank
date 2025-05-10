card = "Maestro 7000792289606361"

card_string = ''
for symbol in card:
    if symbol.isdigit():
        card_string += symbol
card_mask_account = card_string[:4] + "*" * (len(card_string) - 10) + card_string[-4:]
list1 = []
index_start = 0
index_end = 4
for _ in card_mask_account[:: 4]:

    list1.append(card_mask_account[index_start:index_end])
    index_start += 4
    index_end += 4
total_result = ' '.join(list1)
print(card[0:-16] + total_result)
