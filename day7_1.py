import collections

VAL_CARTAS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
              'J': 11, 'Q': 12, 'K': 13, 'A': 14}

tipo_hand_orden = ["High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind"]
cartas_orden = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

from collections import Counter

def identify_hand(hand):
    card_counts = Counter(hand)

    # Check for five of a kind
    if any(count == 5 for count in card_counts.values()):
        return "Five of a kind"

    # Check for four of a kind
    elif any(count == 4 for count in card_counts.values()):
        return "Four of a kind"

    # Check for full house
    elif len(card_counts) == 2 and any(count in (2, 3) for count in card_counts.values()):
        return "Full house"

    # Check for three of a kind
    elif any(count == 3 for count in card_counts.values()):
        return "Three of a kind"

    # Check for two pair
    elif list(card_counts.values()).count(2) >= 2:
        return "Two pair"

    # Check for one pair
    elif list(card_counts.values()).count(2) == 1:
        return "One pair"

    # High card
    else:
        return "High card"


def comparar_lineas(linea1, linea2):
    if linea1['tipo_hand'] != linea2['tipo_hand']:
        return tipo_hand_orden.index(linea1['tipo_hand']) - tipo_hand_orden.index(linea2['tipo_hand'])

    for carta1, carta2 in zip(linea1['hand'], linea2['hand']):
        if carta1 != carta2:
            return cartas_orden.index(carta1) - cartas_orden.index(carta2)

    return 0

tipos_manos = []

def assign_rank(manos):
    # Group hands by type
    manos_by_type = collections.defaultdict(list)
    for mano in manos:
        manos_by_type[mano['tipo_hand']].append(mano)

    # Sort manos within each type based on specific criteria
    for tipo_mano, mano_list in manos_by_type.items():
        if tipo_mano == "One pair":
            mano_list.sort(key=lambda mano: (mano["hand"][0], mano["hand"][1]), reverse=True)
        elif tipo_mano in ("Two pair", "Full house"):
            mano_list.sort(key=lambda mano: mano["hand"][:4], reverse=True)
        elif tipo_mano == "Three of a kind":
            mano_list.sort(key=lambda mano: (mano["hand"][0], mano["hand"][2]), reverse=True)
        elif tipo_mano == "High card":
            mano_list.sort(key=lambda mano: mano["hand"][::-1])

    # Assign rank based on type order and individual hand position within the type
    rank = 1
    for tipo_mano in tipo_hand_orden:
        if tipo_mano in manos_by_type:
            for mano in manos_by_type[tipo_mano]:
                mano["rank"] = rank
            rank += 1

    # Handle unknown hand types
    for mano in manos:
        if "rank" not in mano:
            print(f"Tipo de mano desconocido: {mano['tipo_hand']}")

    return manos

def calcular_ganancias(manos):
    ganancias = 0
    for mano in manos:
        ganancias += int(mano['bid']) * (mano['rank'])
        print(f"{mano}")

        print(f"{mano['bid']}, {mano['rank']}")

    return ganancias


def read_values_from_file(file_path):
    with open(file_path, 'r') as file:
        manos = []
        for line in file:
            linea = line.strip().split(' ')
            hand = linea[0]
            bid = linea[1]
            tipo_hand = identify_hand(hand)
            li = {'hand': hand, 'bid': bid, 'tipo_hand': tipo_hand, 'rank': 0}
            manos.append(li)

            if not (tipo_hand_orden in tipos_manos):
                tipos_manos.append(tipo_hand)
    return manos

file_path = 'datos7_real.txt'
manos = read_values_from_file(file_path)
manos = assign_rank(manos)
lineas_ordenadas = sorted(manos, key=lambda x: (tipo_hand_orden.index(x['tipo_hand']), *[cartas_orden.index(c) for c in x['hand']]))

cont = 1
for linea in lineas_ordenadas:
    linea['rank'] = cont
    cont += 1

     
    
print(calcular_ganancias(lineas_ordenadas))
