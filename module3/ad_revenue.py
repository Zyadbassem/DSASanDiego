def ad_revenue(clicks: list, prices: list):
    s_clicks = sorted(clicks, reverse=True)
    s_prices = sorted(prices, reverse=True)

    total_revenue = 0
    for click, price in zip(s_clicks, s_prices):
        total_revenue += (click * price)

    return total_revenue


def main():
    clicks_count, prices, clicks = int(input()), input().split(' '), input().split(' ')
    clicks, prices = [int(x) for x in clicks], [int(y) for y in prices]

    print(ad_revenue(clicks, prices))

main()
