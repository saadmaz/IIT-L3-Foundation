DropMe Cab Service Console Application
Project Overview
The DropMe Cab Service Console Application is a command-line utility designed for passengers in the Kingdom of Miranda. It provides an automated way to calculate trip fares between cities, choose preferred modes of transport, apply promotional discounts, and generate detailed digital invoices.


Features

Fare Calculation: Instantly calculate the gross price for travel between various cities based on distance and vehicle type.



Transport Modes: Users can choose between three vehicle types:



Trishaw: The default mode (Multiplier: 1).



Car: Premium comfort (Multiplier: 2).


Van: For larger groups (Multiplier: 3).


Promo Codes: Support for multiple promo codes (e.g., pro1 to pro15) that provide flat-rate KMD reductions on the total bill.



Random Discounts: An independent feature that may randomly apply a 5 KMD reduction to the fare for some passengers.



Invoice Generation: Automatically generates a .txt invoice for every trip, saved with a unique timestamped filename.


System Requirements

Language: Python 3.x.

Standard Modules Used:


sys: For system-specific functions.



datetime: To capture real-time trip data for invoices.



random: To handle random discount logic and unique file naming.



math: (Imported for extended calculations).


Operating Guidelines

Start Location: Enter the city you are departing from.


Destination: Enter the city you wish to reach.

Transport Mode: Input Trishaw, Car, or Van. The system is case-insensitive.



Promotions: When prompted, enter a valid promo code to receive a discount.



Receipt: Upon completion, the console will display the name of the generated text file containing your receipt.


Supported Cities
The service operates across the following cities in Miranda:


Alvin

Jamz

Razi

Mali

Zuhar

Invoice Format
The generated invoice text files include the following data points:


Date and Time: Precise moment of the booking.


Locations: Start and end city names.


Amount: The original gross fare before any deductions.


Promo/Reduction: Specific amounts deducted via codes or random luck.


Final Payment: The total amount due after all reductions.

Credits

Student ID: 20221804.


Student Name: Muhammed Saad Mazhar.


Module: DOC 333 - Computer Programming.


Module Leader: Mr. Nishan Saliya.


Institution: Informatics Institute of Technology.