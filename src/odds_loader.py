import csv

def load_odds_csv(path):
    """
    CSV から複勝オッズを読み込む
    CSV 形式:
    horse_id,place_odds
    """
    odds = {}
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            odds[int(row["horse_id"])] = float(row["place_odds"])
    return odds
