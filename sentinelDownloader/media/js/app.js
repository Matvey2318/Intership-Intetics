var mapModel = new MapModel([51.505, -0.09]);
$('#reset_map').click(function(){
    mapModel.resetMap();
});

$('#geojson').change(function(){
    data = new FormData($('#geojson').get(0)); // .files
});

$('#get_geo').click(function(){
    console.log('GEO');
    $("#get_geo").prop("disabled", true);

    $.ajax({
        url: 'home/get_geo',
        type: 'POST',

        cache: false,
        //dataType: 'json',
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        data: data, // stringify
        success: function (respond) {
            console.log('SUCCESS')
        }
        })
    console.log('AJAX DONE')
//        }).fail(function (xhr, ajaxOptions, thrownError) {
//        alert(xhr.status);
//        alert(xhr.statusText);
//        alert(xhr.responseText)
//        });
});