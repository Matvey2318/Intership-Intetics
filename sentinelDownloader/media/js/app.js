var mapModel = new MapModel([51.505, -0.09]);
$('#reset_map').click(function(){
    mapModel.resetMap();
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

    dict.start=date_st.value;
    dict.finish=date_fin.value;
    dict.cloud=cloud.value;

};
let sub = document.getElementById('sub');
sub.onclick=function(e){
    Request();
};

function Request(){
    $.ajax({
  type: "GET",
  url: 'http://127.0.0.1:8000/app/home/findurls',
  data: dict,
  success: openDataTable ,
  dataType:"number",
});
}
function openDataTable(){
    myWin = open('http://127.0.0.1:8000/data-table/')
};

