# Cultivo

**Cultivo** is a machine learning and AI-based crop consultant developed in Python using Django. Cultivo leverages advanced data analytics and predictive modeling to provide farmers and agricultural decision-makers with insights and recommendations tailored to their local conditions, supporting more informed and profitable planting decisions.

## Overview

Cultivo introduces a scalable, accurate, and cost-effective method to predict crop yield by using publicly available datasets and machine learning techniques. The platform applies Regression Analysis, K-Fold, and Batch Training algorithms to predict crop yields with high spatial resolution months before harvest, based solely on globally accessible data. Cultivo's predictions and recommendations assist users in planning crop production, setting adequate food reserves, identifying low-yield areas, and managing risks associated with crop yield variability.

## Introduction

Cultivo serves as a digital crop consultant, utilizing machine learning models extensively trained on data from reliable agricultural and environmental sources. Users can access valuable insights for specific crops in their locality, along with recommendations for alternative crops based on historical agricultural patterns in the area. Cultivo provides a success rate prediction for each crop, helping farmers and stakeholders make data-driven, accurate, and profitable planting decisions.

## Algorithms Used

- **Customized Multiple Linear Regression**: Applied to model the relationship between crop yield and various predictors.
- **Customized K-Fold Method**: Used for training and validating models to improve prediction accuracy and reliability.

## Features

Cultivo provides a comprehensive range of agricultural insights, including:

- **Current Weather Details**: Real-time weather data for the specified region.
- **Soil Conditions**: Historical soil condition data for the past 10 days.
- **Predicted Crop Parameters**:
  - **Imports** and **Exports**: Trends for the past 10 years.
  - **Production**: Total and per unit area production metrics.
  - **Gross Production Value**: Economic value of crop production.
- **Final Success Rate**: Estimated likelihood of a successful crop yield.
- **Alternative Crop Suggestions**: Recommendations for other crops suitable for the area based on historical success rates.

### Sample Test Cases

- **Howrah, Wheat**: 84.944% success rate
- **Anantapur, Rice**: 81.899% success rate
- **Gaya, Sugarcane**: 95.403% success rate

## APIs Used

Cultivo integrates various APIs to gather essential data:

1. **Weather Information**:
   - **Weather API** by OpenWeatherMap
   - **Geocoding API** by The Open Cage

2. **Soil Information**:
   - **AgWeather API** by WeatherBit

## Success Rate Calculation

The final success rate for each crop prediction is calculated using five primary factors, analyzed over the past 10 years:

1. **Imports**: Trends in crop import data.
2. **Exports**: Trends in crop export data.
3. **Production**: Historical production volume.
4. **Production per Unit Area**: Crop yield density in the area.
5. **Gross Production Value**: Economic yield value over the years.

## Getting Started

Follow these instructions to set up Cultivo on your local machine.

### Prerequisites

- **Python 3.8+**
- **Django**: For the backend framework
- **APIs**: Sign up for API keys from OpenWeatherMap, The Open Cage, and WeatherBit

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/devanshalok/cultivo.git
   cd cultivo
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**: 

   Create a `.env` file and add your API keys:

   ```plaintext
   OPENWEATHERMAP_API_KEY=your_openweathermap_key
   OPENCAGE_API_KEY=your_opencage_key
   WEATHERBIT_API_KEY=your_weatherbit_key
   ```

4. **Run Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Start the Server**:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://localhost:8000`.

## Usage

1. **Enter Crop and Location**: Input the crop type and locality to receive customized crop insights and success rate predictions.
2. **Review Predictions**: Analyze predicted weather, soil, import/export, and production metrics.
3. **View Alternative Crops**: Check recommendations for alternative crops with high success rates in your area.

## Built With

- **Python** - Core programming language
- **Django** - Backend framework
- **Machine Learning Libraries** - For predictive analytics and data processing
- **APIs** - For real-time data gathering

## Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for our guidelines on code submissions and reporting issues.

## Authors

- **Devansh Alok** - Initial work - [devanshalok](https://github.com/devanshalok)

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- Thanks to data sources and API providers for supporting agricultural data needs.
- Special acknowledgment to mentors and contributors who provided insights during development.
