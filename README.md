
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="images/weatherIcon.png" alt="Logo" width="80" height="80">
  <h3 align="center">Weather app</h3>
     <br />
    <br />
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
    <li><a href="#installation">Installation</a></li>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A simple weather app created with python, the aim of the application is to be able to search for any city and get a weather report from this city.  First the application finds the city's longtitude and latitude with <a href="https://geopy.readthedocs.io/en/stable/">GeoPy</a>. Then gets the weather data from <a href="https://openweathermap.org/">OpenWeatherMap</a>. Lastly the app gives the weather report.



<!-- Installation -->
### Installation

To run this application, install with git clone

   ```sh
   git clone https://github.com/jacobsvennevik/Weather.git
   ```

<!-- USAGE EXAMPLES -->
## Usage


After installation open the file in an editor, use the run function. 


![Usage run screenshot][usagesRun]

The weather report wil be shown in your code runner.

![Usage result screenshot][usagesResult]



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [OpenWeatherMap](https://openweathermap.org/)
* [GeoPy](https://geopy.readthedocs.io/en/stable/)


<!-- IMAGES -->
[usagesRun]: images/usagesRun.png
[usagesResult]: images/usagesResult.png







