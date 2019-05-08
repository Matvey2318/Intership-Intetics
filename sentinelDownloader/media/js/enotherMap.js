let mymap = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox.streets'
}).addTo(mymap);


// L.circle([51.508, -0.11], 500, {
//     color: 'red',
//     fillColor: '#f03',
//     fillOpacity: 0.5
// }).addTo(mymap).bindPopup("I am a circle.");
let ref = document.getElementById('map').innerHTML;

const button = document.getElementById('button');
const inputRange = document.forms[0].elements[0];
const inputNumb = document.forms[0].elements[1];

inputNumb.onchange = function (e) {
    inputRange.value = inputNumb.value;

};
inputRange.onchange = function (e) {
    inputNumb.value = inputRange.value;

};


let dateDefaultStart = new Date();
let dateDefaultFinish = new Date();
dateDefaultStart.setDate(dateDefaultStart.getDate() - 3);
document.getElementById('finish').valueAsDate = dateDefaultFinish;
document.getElementById('finish').maxAsDate = dateDefaultFinish;
document.getElementById('start').valueAsDate = dateDefaultStart;
let popup = L.popup();
let position = [];

    button.onclick = function (e) {
    position = [];
    console.log('Done');
$(#map){}
    document.getElementById('map').innerHTML = ref;


};





function onMapClick(e) {
    if (position.length < 4) {
        position.push([e.latlng.lat, e.latlng.lng]);
       let mark = L.marker([e.latlng.lat, e.latlng.lng]).addTo(mymap).openPopup();
       L.layerGroup([mark]);
    } else {
        return
    }
    popup
        .setLatLng(e.latlng)
        .setContent(e.latlng.toString())
        .openOn(mymap);
    if (position.length === 4 || position.length !== 3) {
        L.polygon(position).addTo(mymap).bindPopup("I am a polygon.");
    }



    console.log(e.latlng.lat, e.latlng.lng);
}

mymap.on('click', onMapClick);

