#
from pyscript import document

# Dictionary of non-metal elements
Weather_instrument = { 
   "Thermometer" : ("Measures Air Temperature",
                    "UnitofMeasurement"  "Degrees Celsius (°C)",
                    "Purpose" "Measures how hot or cold the air is",)
                     
    "Barometer" :   ("Measures  Atmospheric Pressure",
                     "UnitofMeasurement"  "Hectopascals (hPa)",
                     "Purpose" "Measures air pressure to help monitor weather changes" ),

     "Anemometer" :   ("Measures"  "Relative Humidity"),
                         "UnitofMeasurement" : ("Kilometers per hour (km/h)"),
                         "Purpose" : ("Measures air pressure to help monitorweather changes"),

     "Hygrometer" :   ("Measures" "Atmospheric Pressure"),
                         "UnitofMeasurement" : ("Percent (%)"),
                         "Purpose" : (" " ),
    "Rane Gauge" :   ("Measures" "Rainfall"),
                                  "UnitofMeasurement" : ("Millimeters (mm)"),
                                  "Purpose" : ("Measures the amount of rainfall in an area." ),

     "Wind Vane" :   ("Measures" "Wind Direction"),
                              "UnitofMeasurement" : ("Cardinal Directions"),
                              "Purpose" : ("Identifies the direction from which the wind is blowing. " ),

     "Weather Ballon" :   ("Measures" "Atmospheric Conditions"),
                         "UnitofMeasurement" : ("Varies"),
                         "Purpose" : ("Collects atmospheric data at different altitudes."  ),

      "Pyranometer" :   ("Measures"  "Solar Radiation"),
                             "UnitofMeasurement" :( "Watts per square meter (W/m²)")
                             "Purpose" : ("Measures incoming solar radiation."  ),
}

def Search(event):

    # Get the element symbol from HTML
    Element1 = document.querySelector("#Elements").value.strip()

   