#
from pyscript import document

# Dictionary of weather instrumnets
Weather_instrument = {
    "Thermometer": {
        "Measures Air Temperature",
        "Unit of Measurement: Degrees Celsius (°C)" ,
        "Purpose: Measures how hot or cold the air is"
    },

    "Barometer": {
        "Measures Atmospheric Pressure",
        "Unit of Measurement : Hectopascals (hPa)",
        "Purpose : Measures air pressure to help monitor weather changes"
    },

    "Anemometer": {
        "Measures Wind Speed",
        "Unit of Measurement : Kilometers per hour (km/h)",
        "Purpose : Measures how fast the wind blows"
    },

    "Hygrometer": {
        "Measures Relative Humidity",
        "Unit of Measurement : Percent (%)",
        "Purpose : Measures the amount of moisture in the air"
    },

    "Rain Gauge": {
        "Measures Rainfall",
        "Unit of Measurement: Millimeters (mm)",
        "Purpose :Measures the amount of rainfall in an area"
    },

    "Wind Vane": {
        "Measures Wind Direction",
         "Unit of Measurement : Cardinal Directions",
         "Purpose : Identifies the direction from which the wind is blowing"
    },

    "Weather Balloon": (
        "Measures Atmospheric Conditions",
        "Unit of Measurement : Varies",
        "Purpose : Collects atmospheric data at different altitudes"
    ),

    "Pyranometer": (
        "Measures Solar Radiation",
        "Unit of Measurement : Watts per square meter (W/m²)",
        "Purpose : Measures incoming solar radiation"
    )
}


def Search(event):

    # Get the element symbol from HTML
    Element1 = document.querySelector("#Elements").value.strip()
