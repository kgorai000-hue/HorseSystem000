import itertools

def calc_trifecta_fair_odds(q):
    """
    三連複のフェアオッズを計算する
    P(i,j,k) = q_i * q_j * q_k
    O = 1 / P
    """
    fair_odds = {}

    for i, j, k in itertools.combinations(q.keys(), 3):
        p = q[i] * q[j] * q[k]
        fair_odds[(i, j, k)] = 1 / p

    return fair_odds
