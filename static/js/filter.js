function myFunction() {

    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("list");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
    if (document.getElementById("myInput").value == "")
        remove();
}

function show() {

    var tr, td, i;
    tr = document.getElementById("list").getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];

        td.style.display = 'block';
    }

    myFunction();
}

function remove() {

    var tr, td, i;
    tr = document.getElementById("list").getElementsByTagName("tr");

    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];

        td.style.display = 'none';

    }


}

function select(arg) {
    document.getElementById("myInput").value = arg;
    remove();
}