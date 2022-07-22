// console.log($("#subscription-list"));
const baseUrl = mainOrigin + "/api/"
console.log(baseUrl)

$(document).ready(function () {
    $("#subscription-list").DataTable({
        scrollX: true,
        scrollCollapse: true,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: -1
        }],
        sorting: false,
        searching: false,
        // oLanguage: {
        //     sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
        //     sSearchPlaceholder: "Search...",
        // },
        "paging": false,
    });

});


let packageChart = document.getElementById("package-chart").getContext("2d");

let revenuePieChart = new Chart(packageChart, {
    type: "pie",
    data: {
        labels: ["CUSTOM", "BASIC", "ADVANCE", "MEDIUM"],
        datasets: [{
            label: "Subscribed client",
            backgroundColor: ['#182F59', '#5BBC2E', '#FFD500', '#DC143C'],
            data: [45, 25, 10, 20],
        },],
    },

    options: {
        responsive: true,
        legend: {
            display: true,
            labels: {
                fontColor: "black",
                boxWidth: 15,
            },
            // maxWidth: 30,
            position: "left",
        },
    },
});
