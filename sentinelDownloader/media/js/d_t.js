let table = document.getElementById('date');
 let dataTb = document.createElement('tr');
//function fillingDataTable(arr) {
//      arr=[1,2,3,4,5,6];
    for (item of arr) {
        let dataTb = document.createElement('tr');
        dataTb.innerHTML = `

                <td><a href="${item}">${item}</a></td>
                <td>ID</td>
               
           `;
        table.appendChild(dataTb);
    }
    // $('.pop-outer').fadeIn('slow');
    //myWin = open('http://127.0.0.1:8000/data-table/')
//};
