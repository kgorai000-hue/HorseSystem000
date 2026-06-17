def select_max_odds(fair_odds, threshold):
    """
    フェアオッズの中から「買うべき最大オッズ」を選ぶ
    threshold = 勝負ゾーンの合成オッズ O(M) の基準
    """
    selected = {k: v for k, v in fair_odds.items() if v <= threshold}
    if not selected:
        return None
    return max(selected.values())
