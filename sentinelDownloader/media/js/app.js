var mapModel = new MapModel([51.505, -0.09]);
$('#reset_map').click(function(){
    mapModel.resetMap();
});

$('#get_geo').click(function(){
    console.log('GEO');
    $("#get_geo").prop("disabled", true);
    var fd = new FormData;
    var $input = $('input[name="geojson"');
    fd.append('polygon_data', $input.prop('files')[0]);
    $.ajax({
        url: 'home/get_geo',
        type: 'POST',
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        data: fd,
        success: function (respond) {
            console.log('SUCCESS');
        }
        });
});

let dict = {};
let date_st = document.getElementById('start');
let date_fin = document.getElementById('finish');
let cloud = document.getElementById('cloud');
cloud.onchange= function (e) {
    dataRecord();
};
date_fin.onchange= function (e) {
    dataRecord();
};

date_st.onchange= function (e) {
    dataRecord();
};


function dataRecord (){

    dict.beginposition=date_st.value;
    dict.endposition=date_fin.value;
    dict.cloudcoverpercentage=cloud.value;

};
let sub = document.getElementById('sub');
sub.onclick=function(e){
    Request();
};

function Request(){
    $.ajax({
  type: "GET",
  url: 'home/findurls',
  data: dict,
  success: openDataTable ,
  dataType:"number",
});
}
function openDataTable(){
    myWin = open('http://127.0.0.1:8000/data-table/')
};

var inputRange = document.getElementById('cloud');
var inputNumb = document.getElementById('num');
inputRange.oninput = function (e) {
    inputNumb.value = inputRange.value;

};

inputNumb.onchange = function (e) {
    inputRange.value = inputNumb.value;

};