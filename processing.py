from flask_restful import Resource
from numpy import column_stack
import pandas as pd
from scipy.io import arff


def map_column_name(df):
    map = [
        "net profit / total assets",
        "total liabilities / total assets",
        "working capital / total assets",
        "current assets / short-term liabilities",
        "[(cash + short-term securities + receivables - short-term liabilities) / (operating expenses - depreciation)] * 365",
        "retained earnings / total assets",
        "EBIT / total assets",
        "book value of equity / total liabilities",
        "sales / total assets",
        "equity / total assets",
        "(gross profit + extraordinary items + financial expenses) / total assets",
        "gross profit / short-term liabilities",
        "(gross profit + depreciation) / sales",
        "(gross profit + interest) / total assets",
        "(total liabilities * 365) / (gross profit + depreciation)",
        "(gross profit + depreciation) / total liabilities",
        "total assets / total liabilities",
        "gross profit / total assets",
        "gross profit / sales",
        "(inventory * 365) / sales",
        "sales (n) / sales (n-1)",
        "profit on operating activities / total assets",
        "net profit / sales",
        "gross profit (in 3 years) / total assets",
        "(equity - share capital) / total assets",
        "(net profit + depreciation) / total liabilities",
        "profit on operating activities / financial expenses",
        "working capital / fixed assets",
        "logarithm of total assets",
        "(total liabilities - cash) / sales",
        "(gross profit + interest) / sales",
        "(current liabilities * 365) / cost of products sold",
        "operating expenses / short-term liabilities",
        "operating expenses / total liabilities",
        "profit on sales / total assets",
        "total sales / total assets",
        "(current assets - inventories) / long-term liabilities",
        "constant capital / total assets",
        "profit on sales / sales",
        "(current assets - inventory - receivables) / short-term liabilities",
        "total liabilities / ((profit on operating activities + depreciation) * (12/365))",
        "profit on operating activities / sales",
        "rotation receivables + inventory turnover in days",
        "(receivables * 365) / sales",
        "net profit / inventory",
        "(current assets - inventory) / short-term liabilities",
        "(inventory * 365) / cost of products sold",
        "EBITDA (profit on operating activities - depreciation) / total assets",
        "EBITDA (profit on operating activities - depreciation) / sales",
        "current assets / total liabilities",
        "short-term liabilities / total assets",
        "(short-term liabilities * 365) / cost of products sold)",
        "equity / fixed assets",
        "constant capital / fixed assets",
        "working capital",
        "(sales - cost of products sold) / sales",
        "(current assets - inventory - short-term liabilities) / (sales - gross profit - depreciation)",
        "total costs /total sales",
        "long-term liabilities / equity",
        "sales / inventory",
        "sales / receivables",
        "(short-term liabilities *365) / sales",
        "sales / short-term liabilities",
        "sales / fixed assets",
    ]
    df.set_axis(map, axis=1, inplace=True)
    return df


if __name__ == "__main__":
    data = arff.loadarff("data/1year.arff")
    df = pd.DataFrame(data[0])
    df.drop(["class"], axis=1, inplace=True)
    map_column_name(df)
    df.to_csv("main/data/data.csv",index=False)
