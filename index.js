var map = L.map("map").setView([23.022528, 72.572173], 11);
var points = {};
var geoData;

// var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution:
    '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

const readJSONFile = async () => {
  try {
    const data = await fetch("values.json");
    var response = await data.json();
    return response;
  } catch (e) {
    console.log(e);
    return e;
  }
};

const getData = async () => {
  var data = await readJSONFile();
  geoData = data;  
  data.forEach((item) => {    
    points[item.deviceId] = L.polygon(item.location, {      
      color: item['values'][addHoursToEpoch(0)]['ws']['color'],
      fillcolor: item['values'][addHoursToEpoch(0)]['ws']['color'],
      opacity: 1,
    }).addTo(map);    
  });
};

getData();

function addHoursToEpoch(hours) {
  var baseTime = new Date("2023-06-29T06:00:00"); // Specify the base date and time
  var targetTime = new Date(baseTime.getTime() + hours * 60 * 60 * 1000); // Add hours to the base time

  var epochTime = Math.floor(targetTime.getTime() / 1000); // Convert the target time to epoch time

  return epochTime;
}

function handleSliderChange() {
  var sliderValue = document.getElementById("timeSlider").value;
  var selectedField = document.getElementById("selectedField").value;

  var timeT = addHoursToEpoch(parseInt(sliderValue));
  geoData.forEach((item) => {
    points[item.deviceId].setStyle({
      color: item["values"][timeT][selectedField]["color"],
      fillcolor: item["values"][timeT][selectedField]["color"],
    });
  });
}

var slider = document.getElementById("timeSlider");
slider.addEventListener("input", handleSliderChange);
