def calculateCost(votes):
    if votes >= 5:
        return float2((votes * 0.7) * 100)

    return float2(votes * 100)


def float2(number):
    return int(round(number, 2))
