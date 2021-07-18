from dataclasses import dataclass
from typing import List, Optional

@dataclass(frozen=True)
class WeatherLocation:
    '''
    Represents the location of the weather.

    Attributes
    ----------

      name : str
        The name of location.

      lat : str
        The latitude of the location.
    
      long : str
        The longitude of the location.

      timezone : str
        The timezone of location.

      alert : str
        The alert of the location.

      degreetype : str
        The type of degree.

      imagerelativeurl : str
        The URL of the image.

      latitude : str
        An alias for `lat` attribute.

      longitude : str
        An alias for `long` attribute
    
      degree_type : str
        An alias for `degreetype` attribute.

      image_relative_url : str
        An alias for `imagerelativeurl` attribute.
    '''
    name: str = None
    lat: str = None
    long: str = None
    timezone: str = None
    alert: str = None
    degreetype: str = None
    imagerelativeurl: str = None

    # Aliases
    latitude: str = lat
    longitude: str = long
    degree_type: str = degreetype
    image_relative_url: str = imagerelativeurl


@dataclass(frozen=True)
class CurrentWeather:
    '''
    Represents the current weather of the weather object.

    Attributes
    ----------

      temperature : str
        The current temprature.

      skycode : str
        The sky code of weather.

      skytext : str
        The sky text day of weather.

      date : str
        The date of weather.

      day : str
        The day of weather.

      shortday : str
        The short-form of `day` attribute. For example, if `day` attribute is "Saturday" the `shortday` will be "Sat"
    
      observationtime : str
        The time of observation.

      observationpoint : str
        The point of observation.

      feelslike : str
        The 'feels like' temprature.

      humidity : str
        The humidity in weather.

      winddisplay : str
        The wind display.
    
      windspeed : str
        The speed of wind.

      imageUrl : str
        The URL of the weather image.

      sky_code : str
        An alias for the `skycode` attribute.

      sky_text : str
        An alias for the `skytext` attribute.

      observation_time : str
        An alias for the `observationtime` attribute.

      observation_point : str
        An alias for `observationpoint` attribute.

      feels_like : str
        An alias for the `feelslike` attribute.

      wind_display : str
        An alias for the `winddisplay` attribute.

      short_day : str
        An alias for the `shortday` attribute.

      imageURL, image_url, imageurl : str
        Aliases for `imageUrl` attribute.
    '''
    temperature: str = None
    skycode: str = None
    skytext: str = None
    date: str = None
    observationtime: str = None
    observationpoint: str = None
    feelslike: str = None
    humidity: str = None
    winddisplay: str = None
    day: str = None
    shortday: str = None
    windspeed: str = None
    imageUrl: str = None

    # Aliasing
    sky_code: str = skycode
    sky_text: str = skytext
    observation_time: str = observationtime
    observation_point: str = observationpoint
    feels_like: str = feelslike
    wind_display: str = winddisplay
    short_day: str = shortday
    wind_speed: str = windspeed
    image_url: str = imageUrl
    imageURL: str = imageUrl
    imageurl: str = imageUrl

@dataclass(frozen=True)
class WeatherForecast:
    '''
    Represents the forecast of the weather object.

    Attributes
    ----------

      low : str
        The lowest temprature.

      high : str
        The highest temprature

      skycodeday : str
        The sky code day of forecast.

      skytextday : str
        The sky text day of forecast.

      date : str
        The date of forecast day.

      day : str
        The day of forecast.

      shortday : str
        The short-form of `day` attribute. For example, if `day` attribute is "Saturday" the `shortday` will be "Sat"
    
      precip : str
        The precipitation of forecast.

      sky_code_day : str
        An alias for the `skycodeday` attribute.

      sky_text_day : str
        An alias for the `skytextday` attribute.

      short_day : str
        An alias for the `short_day` attribute.

      precipitation : str
        An alias for `precip` attribute.

    '''
    low: str = None
    high: str = None
    skycodeday: str = None
    skytextday: str = None
    date: str = None
    day: str = None
    shortday: str = None
    precip: str = None

    # Aliasing
    sky_code_day: str = skycodeday
    sky_text_day: str = skytextday
    short_day: str = shortday
    precipitation: str = precip

@dataclass(frozen=True)
class Weather:
    '''
    Represents the weather returned by API.

    Attributes
    ----------

      location : WeatherLocation
        The location of weather.

      current : Optional[CurrentWeather]
        The current weather. There's a chance that this might be None.

      forecast : List[WeatherForecast]
        The list of weather forecast of different days.
    '''
    location: WeatherLocation = None
    current: Optional[CurrentWeather] = None
    forecast: List[WeatherForecast] = None