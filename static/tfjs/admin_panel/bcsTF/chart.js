let infoChart = document.getElementById("info-chart").getContext("2d");

let infoLineChart = new Chart(infoChart, {});
let getChartData = (type, start, end) => {

    fetch(`${mainOrigin}/api/bcs/${(start && end) ? `bcs_admin_range_chart/?start_date=${start}&end_date=${end}` : `bcs_admin_${type}_chart`}`, {
        credentials: 'include'
    })
        .then(response => {
            return response.json()
        })
        .then(data => {
            infoLineChart.destroy();
            infoLineChart = new Chart(infoChart, {
                type: "line",
                data: {
                    labels: data.x_axis,
                    datasets: [{
                        label: "Subscribed client",
                        backgroundColor: "#182F59",
                        borderColor: "#182F59",
                        data: data.datas.for_subscription,
                        fill: false,
                    }, {
                        label: "non- subscribed client",
                        backgroundColor: "#5BBC2E",
                        borderColor: "#5BBC2E",
                        data: data.datas.for_unsubscription,
                        fill: false,
                    }, {
                        label: "total client",
                        backgroundColor: "#111125",
                        borderColor: "#111125",
                        data: data.datas.total_count,
                        fill: false,
                    },],
                },
                options: {
                    responsive: true,
                    legend: {
                        display: true,
                        labels: {
                            fontColor: "black",
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

        });
}

getChartData('all');


//if(window.innerWidth <=769){
//    infoLineChart.options.legend.display=false;
// }