let userChart = document.getElementById("user-chart").getContext("2d");
let userLineChart = new Chart(userChart, {
    type: "line",
    data: {
        labels: ["January", "February", "March", "April", "May"],
        datasets: [{
            label: "New User",
            backgroundColor: "black",
            borderColor: "black",
            data: [5, 45, 41, 50, 42],
            fill: false,
        }, {
            label: "Total User",
            backgroundColor: "#182f59",
            borderColor: "#182f59",
            data: [75, 35, 70, 90, 15],
            fill: false,
        }, ],
    },
    options: {
        responsive: true,
        legend: {
            display: false,
            labels: {
                fontColor: "black",
            },
            position: "top",
        },
        title: {
            display: false,
            text: "Users Number / Month",
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