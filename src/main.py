from odds_loader import load_odds_csv
from probability_model import calc_q_values
from trifecta_fair_odds import calc_trifecta_fair_odds
from max_odds_selector import select_max_odds

def main():
    # 1. 複勝オッズを読み込む
    odds = load_odds_csv("data/sample_odds.csv")

    # 2. q_i を計算
    q = calc_q_values(odds)

    # 3. 三連複フェアオッズを計算
    fair = calc_trifecta_fair_odds(q)

    # 4. 勝負ゾーンの最大オッズを決定
    threshold = 200.0  # 例
    max_odds = select_max_odds(fair, threshold)

    print("=== 三連複フェアオッズ（例） ===")
    for k, v in list(fair.items())[:10]:
        print(k, round(v, 2))

    print("\n=== 勝負ゾーンの最大オッズ ===")
    print(max_odds)

if __name__ == "__main__":
    main()
