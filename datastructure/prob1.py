hedge_fund_portfolio = {
    "fund_name": "Alpha Investments",
    "portfolio_value": 50000000,
    "investments": [
        {
            "type": "Equity",
            "holdings": [
                {"ticker": "AAPL", "quantity": 10000, "average_buy_price": 120},
                {"ticker": "TSLA", "quantity": 5000, "average_buy_price": 600}
            ]
        },
        {
            "type": "Fixed Income",
            "holdings": [
                {"bond_issue": "US Treasuries", "amount": 10000000, "yield": 1.5}
            ]
        },
        {
            "type": "Derivatives",
            "holdings": [
                {"instrument": "Options", "details": {"underlying": "GOOGL", "type": "Call", "strike_price": 1500}}
            ]
        }
    ],
    "performance_metrics": {
        "year_to_date_return": 5.2,
        "five_year_annualized_return": 7.1
    }
}
name='TSLA'

ans=hedge_fund_portfolio['investments'][0]['holdings'][1]['quantity']
print(ans)
dict1={
            "type": "Real Estate",
            "holdings": [
                {"instrument": "property", "details": {'Downtown Complex':2000000}}
            ]
        }

hedge_fund_portfolio['investments'].append(dict1)
print(hedge_fund_portfolio)

hedge_fund_portfolio['portfolio_value']=51000000

hedge_fund_portfolio['investments'].pop(2)
print(hedge_fund_portfolio)

dict2={"ticker": "AMZN", "quantity": 3000, "average_buy_price": 3100}
hedge_fund_portfolio['investments'][0]['holdings'].append(dict2)

del hedge_fund_portfolio['investments'][0]['holdings'][0]
print(hedge_fund_portfolio)