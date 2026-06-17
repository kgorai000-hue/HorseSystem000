def calc_q_values(place_odds_dict):
    """
    複勝オッズ F_i から 3着以内確率 q_i を計算する
    q_i = (1/F_i) / Σ(1/F_j)
    """
    inv = {k: 1/v for k, v in place_odds_dict.items()}
    total = sum(inv.values())
    q = {k: inv[k] / total for k in inv}
    return q
