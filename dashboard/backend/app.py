from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route("/api/oil-prices", methods=["GET"])
def get_oil_prices():
    """
    API endpoint to fetch Brent oil prices.
    """
    data = pd.read_csv("../../data/processed_data.csv")
    response = {"dates": data["Date"].tolist(), "prices": data["Price"].tolist()}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
