from flask import Flask, render_template, request, jsonify  # Fixed typo and added missing imports
import random

app = Flask(__name__)

# Define payouts
payouts = [
    {"name": "7️⃣", "payouts": {3: 500, 2: 25}},
    {"name": "💎", "payouts": {3: 25, 2: 10}},
    {"name": "🎰", "payouts": {3: 5, 2: 3}},
    {"name": "🔔", "payouts": {3: 3, 2: 2}},
    {"name": "👞", "payouts": {3: 2, 2: 1}},
    {"name": "🍋", "payouts": {3: 1, 2: 1}},
    {"name": "🍉", "payouts": {3: 0.75, 2: 1}},
    {"name": "❤️", "payouts": {3: 0.5, 2: 0.75}},
    {"name": "🍒", "payouts": {3: 0.5, 2: 0.25}},
]

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML template

@app.route('/slots', methods=['POST'])
def slots():
    bet = request.json.get('bet')
    if bet == 'm':
        bet_amount = 100  # Example max bet
    elif bet == 'a':
        bet_amount = 500  # Example all-in amount
    else:
        try:
            bet_amount = float(bet)
        except ValueError:
            return jsonify({"error": "Invalid bet amount"}), 400

    symbols = [symbol["name"] for symbol in payouts]
    result = random.choices(symbols, k=3)  # Simulate slot spin
    
    # Count matches
    counts = {symbol: result.count(symbol) for symbol in symbols}
    best_payout = 0

    for symbol, count in counts.items():
        for payout in payouts:
            if payout["name"] == symbol and count in payout["payouts"]:
                best_payout = max(best_payout, payout["payouts"][count])
    
    total_payout = best_payout * bet_amount
    message = f"You won {total_payout} credits!" if best_payout > 0 else "Better luck next time!"
    return jsonify({"spin_result": result, "payout": total_payout, "message": message})

@app.route('/slots/reset', methods=['POST'])
def reset():
    return jsonify({"message": "Game has been reset."})

if __name__ == '__main__':
    app.run(debug=True)