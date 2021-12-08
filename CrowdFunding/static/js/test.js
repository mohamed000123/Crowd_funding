$("#one").click(function () {
    $("#myprojects").toggle(3000);
    $("#mydonations").hide(3000);
    $("#edit").hide(3000);
    $("#additinal").hide(3000);
    $("#delete").hide(3000)
})

$("#two").click(function () {
    $("#edit").toggle(3000);
    $("#mydonations").hide(3000);
    $("#myprojects").hide(3000);
    $("#additinal").hide(3000);
    $("#delete").hide(3000);
})

$("#three").click(function () {
    $("#mydonations").toggle(3000);
    $("#myprojects").hide(3000);
    $("#edit").hide(3000);
    $("#additinal").hide(3000);
    $("#delete").hide(3000);
})

$("#four").click(function () {
    $("#additinal").toggle(3000);
    $("#myprojects").hide(3000);
    $("#edit").hide(3000);
    $("#mydonations").hide(3000);
    $("#delete").hide(3000);
})

$("#five").click(function () {
    $("#delete").toggle(3000);
    $("#additinal").hide(3000);
    $("#myprojects").hide(3000);
    $("#edit").hide(3000);
    $("#mydonations").hide(3000);
})
