$(function() {

$(document).ready(function() 
    { 
        $("#myTable").tablesorter(); 
    } 
); 
$(document).ready(function() 
    { 
        $("#myTable").tablesorter( {sortList: [[0,0], [1,0]]} ); 
    } 
); 
});//ready