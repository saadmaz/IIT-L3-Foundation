# 🚕 DropMe Cab Service Console Application

## Project Overview

**DropMe Cab Service** is a Python-based console application designed for passengers in the Kingdom of **Miranda**. The system automates cab fare calculation between cities, allows users to select transport modes, applies promotional and random discounts, and generates detailed digital invoices for every trip.

🔗 **Project Deployment:**
👉 [https://dropme.saadmaz.com](https://dropme.saadmaz.com)

---

## ✨ Features

### Fare Calculation

* Automatically calculates the **gross fare** based on:

  * Distance between cities
  * Selected vehicle type

### Transport Modes

Users can choose from three transport options:

* **Trishaw** (Default)
  Multiplier: `1`
* **Car** (Premium comfort)
  Multiplier: `2`
* **Van** (Larger groups)
  Multiplier: `3`

### Promo Codes

* Supports multiple promo codes (`pro1` to `pro15`)
* Each promo code applies a **flat-rate KMD discount** to the total fare

### Random Discounts

* A bonus feature where selected users may randomly receive a **5 KMD discount**

### Invoice Generation

* Automatically generates a **`.txt` invoice** for every completed trip
* Each invoice is saved using a **unique timestamp-based filename**

---

## 🛠 System Requirements

* **Language:** Python 3.x
* **Standard Modules Used:**

  * `sys` – System-level operations
  * `datetime` – Captures real-time trip and invoice data
  * `random` – Handles random discounts and unique file naming
  * `math` – Imported for extended fare calculations

---

## ▶️ Operating Guidelines

1. **Start Location**
   Enter the city you are departing from.

2. **Destination**
   Enter the city you wish to travel to.

3. **Transport Mode**
   Choose one of:

   * Trishaw
   * Car
   * Van
     *(Input is case-insensitive)*

4. **Promotions**
   When prompted, enter a valid promo code to apply a discount.

5. **Receipt**
   After completion, the console displays the filename of the generated invoice.

---

## 🌍 Supported Cities

The DropMe service operates across the following cities in Miranda:

* Alvin
* Jamz
* Razi
* Mali
* Zuhar

---

## 🧾 Invoice Format

Each generated invoice includes:

* **Date & Time** – Exact booking timestamp
* **Trip Locations** – Start and destination cities
* **Gross Amount** – Fare before deductions
* **Discounts Applied** – Promo code and/or random discount
* **Final Payment** – Total payable amount

---

## 🎓 Credits

* **Student ID:** 20221804
* **Student Name:** Muhammed Saad Mazhar
* **Module:** DOC 333 – Computer Programming
* **Module Leader:** Mr. Nishan Saliya
* **Institution:** Informatics Institute of Technology
