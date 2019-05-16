var mapModel = new MapModel([51.505, -0.09]);
$('#reset_map').click(function () {
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
cloud.onchange = function (e) {
    dataRecord();
};
date_fin.onchange = function (e) {
    dataRecord();
};

date_st.onchange = function (e) {
    dataRecord();
};


function dataRecord() {

    dict.beginposition = date_st.value;
    dict.endposition = date_fin.value;
    dict.cloudcoverpercentage = cloud.value;

};
let sub = document.getElementById('sub');
sub.onclick = function (e) {
    Request();
};

function Request() {
    $.ajax({

  type: "GET",
  url: 'home/findurls',
  data: dict,
  success: openDataTable ,
  dataType:"json",
  success: function(data) {
  console.log(data.urls);
  }
});

}

function openDataTable() {
    myWin = open('http://127.0.0.1:8000/data-table/')
};
//
var inputRange = document.getElementById('cloud');
var inputNumb = document.getElementById('num');
inputRange.oninput = function (e) {
    inputNumb.value = inputRange.value;

};

inputNumb.onchange = function (e) {
    inputRange.value = inputNumb.value;

};
// Modal data-table room for improvement
$(document).ready(function () {
    $('#sub').click(function () {
        $('.pop-outer').fadeIn('slow');
       $('.map').fadeOut('slow');
        //$('.geo-submit').fadeOut('slow');
        //$('.footer').fadeOut('slow');
    });

    $('.close').click(function () {
        $('.pop-outer').fadeOut('slow');
        $('.map').fadeIn('slow');
        $('.geo-submit').fadeIn('slow');
        $('.footer').fadeIn('slow');
    })
});

// fixed date for finish
$(function(){
    let dtToday = new Date();

    let month = dtToday.getMonth() + 1;
    let day = dtToday.getDate();
    let year = dtToday.getFullYear();
    if(month < 10)
        month = '0' + month.toString();
    if(day < 10)
        day = '0' + day.toString();

    let maxDate = year + '-' + month + '-' + day;

    $('#finish').attr('max', maxDate);
});
//fixed date for start
$(function(){
    let dtToday = new Date();

    let month = dtToday.getMonth() + 1;
    let day = dtToday.getDate() - 3;
    let year = dtToday.getFullYear();
    if(month < 10)
        month = '0' + month.toString();
    if(day < 10)
        day = '0' + day.toString();

    let maxDate = year + '-' + month + '-' + day;

    $('#start').attr('max', maxDate);
});
//disable submit
$(document).ready(function () {
    $('#map').click(function () {
        $(".geo-submit").addClass("disabled");
    });
});
//disable map
$(document).ready(function () {
    $('.geo-submit').change(function () {
        $('.map').addClass("disabled");
    })
});


// button cancel-file
$(document).ready(function () {
    $('.cancel-file').click(function () {
        $('.map').removeClass("disabled");

    })
});

// button cancel-map
$(document).ready(function () {
    $('.cancel-map').click(function () {
        $('.geo-submit').removeClass("disabled");
    })
});

