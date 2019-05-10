var mapModel = new MapModel([51.505, -0.09]);
$('#reset_map').click(function(){
    mapModel.resetMap();
});
let dict = {};
let date_st = document.getElementById('start').value;
let date_fin = document.getElementById('finish').value;
let cloud = document.getElementById('cloud').value;
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

    dict.start=date_st;
    dict.finish=date_fin;
    dict.cloud=cloud;

};
let sub = document.getElementById('sub');
sub.onclick=function(e){

myWin = open('http://127.0.0.1:8000/data-table/')
};

