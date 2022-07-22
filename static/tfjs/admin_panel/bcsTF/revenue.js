let revenueChart = document.getElementById("revenue-chart").getContext("2d");
let infoChart = document.getElementById("info-chart").getContext("2d");

let revenuePieChart = new Chart(revenueChart, {
    type: "pie",
    data: {
        labels: ["Total", "Subscribed", "One Time Purchased"],
        datasets: [{
            label: "Subscribed client",
            backgroundColor: ['#182F59','#5C5CBC','#182F59',],
            data: [60, 16, 20],
        },  ],
    },
      
    options: {
        responsive: true,
        legend: {
            display: true,
            labels: {
                fontColor: "black",
                boxWidth:15,
            },
            // maxWidth: 30,
            position: "left",
        },        
    },
});
let infoLineChart = new Chart(infoChart, {
    type: "line",
    data: {
        labels: ["text", "text", "text", "text", "text"],
        datasets: [{
            label: "Subscribed client",
            backgroundColor: "#182F59",
            borderColor: "#182F59",
            data: [5, 4, 14, 10, 4],
            fill: false,
        }, {
            label: "One time Purchased client",
            backgroundColor: "#5BBC2E",
            borderColor: "#5BBC2E",
            data: [15, 3, 5, 8, 15],
            fill: false,
        }, {
            label: "total client",
            backgroundColor: "#111125",
            borderColor: "#111125",
            data: [6, 5, 7, 9, 2],
            fill: false,
        }, ],
    },
    options: {
        responsive: true,
        legend: {
            display: true,
            labels: {
                fontColor: "black",
                boxWidth: 20,
                boxHeight: 20,
            },
            position: "top",
        },
        title: {
            display: false,
            position: "top",
            align: 'start',
            text: "all users",
        },
        tooltips: {
            mode: "index",
            intersect: false,
        },
        hover: {
            mode: "nearest",
            intersect: true,
        },
        scales: {
            xAxes: [{
                gridLines: {
                    display: false
                }
            }],
            yAxes: [{
                gridLines: {
                    display: false
                }
            }]
        },
    },
});