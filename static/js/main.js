$(document).ready(function () {
    document.getElementById("loadMoreButton").addEventListener("click", function () {
        var itemArray = document.getElementsByClassName("profile");
        var itemArrayLength = itemArray.length;
        var lastItem = itemArray[itemArrayLength - 1];
        var proID = lastItem.id.split("-")[1];
        var ProUrl = "ajax/" + proID;
        var ProfileNode = lastItem.parentElement;
        $.get(ProUrl, function (data) {
            ProfileNode.insertAdjacentHTML("afterend", data);
            prodata = data;
        }, "html");
    });
});
