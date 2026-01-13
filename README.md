# 🚀 Deep Space Miner - Risk & Reward Simulator

A text-based space exploration game where you play as a freelance asteroid miner. Your goal is to accumulate 500 credits to retire, but space is dangerous—one too many asteroid collisions will destroy your ship.

This project is designed to help beginners master:
* **Probability Logic:** Using `random.random()` to create "chance-based" events (like a 20% fail rate).
* **Game Balancing:** Managing multiple resources (Fuel, Health, Money) that all depend on each other.
* **Multi-Condition Loops:** Using `while` loops with `and` operators to check for both victory and defeat.
* **Upgrades/Multipliers:** Implementing mechanics that allow the player to get stronger over time.

---

## ✨ Features

* **Risk/Reward Mining:** 80% chance of success, 20% chance of taking heavy hull damage.
* **Repair System:** Spend earned credits to fix your ship and stay in the game.
* **Drill Upgrades:** Invest in better technology to multiply your mining yield.
* **Fuel Management:** A limited fuel supply adds another layer of strategy to your turns.
* **Dual Ending States:** Win by reaching the credit goal or lose by losing all hull integrity.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed on your system.

### 2. Setup and Execution
1.  **Save the Code:** Save the Python script as `space_miner.py`.
2.  **Open Terminal:** Navigate to the folder where you saved the file.
3.  **Run the Script:**
    ```bash
    python space_miner.py
    ```

### 3. Gameplay Instructions
* **[M]ine:** Try to find ore. It consumes 1 fuel. Watch out for asteroids!
* **[R]epair:** Costs 20 credits. Restores 30% of your hull.
* **[U]pgrade:** Costs 50 credits. Increases your drill power, allowing you to find more ore per successful mine.
* **Goal:** Reach **500 credits** without letting your hull hit **0%**.

---

## 🧠 Code Structure Highlights

### Probability-Based Events
Unlike a simple dice roll, we use `random.random()` to generate a decimal between 0 and 1. This allows for very precise "drop rates":

```python
event = random.random()
if event < 0.2: # This creates a 20% chance of failure
    # Damage logic here
