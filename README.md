## Slot Machine Feature

### Endpoint: `/slots/bet`
- **Method**: POST
- **Parameters**:
  - `bet` (string): The amount to bet. Use `m` for max and `a` for all-in.
- **Response**:
  - `spin_result` (array): The symbols from the slot machine spin.
  - `payout` (number): The payout based on the spin result.
  - `message` (string): A message summarizing the spin result.
- **Example**:
  ```json
  {
      "spin_result": ["7️⃣", "💎", "🍒"],
      "payout": 25.0,
      "message": "You won 25.0 credits!"
  }
  ```

### Endpoint: `/slots/reset`
- **Method**: POST
- **Response**:
  - `message` (string): Confirmation that the game has been reset.
- **Example**:
  ```json
  {
      "message": "Game has been reset."
  }
  ```

### How to Play
1. Select your bet amount from the dropdown menu (`m` for max, `a` for all-in).
2. Click "Spin" to spin the slot machine.
3. View the spin result, payout, and message below the buttons.
4. Click "Reset Game" to reset the game state and start fresh.

### Payout Logic
The best odds match will be selected. For example, if you get 3 bells and 2 bars, the payout will be for 2 bars.