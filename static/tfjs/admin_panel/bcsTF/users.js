if (document.getElementById("user-info-chart")) {
    let userInfo = document.getElementById("user-info-chart").getContext("2d");
    let userInfoLineChart = new Chart(userInfo, {
        type: "line",
        data: {
            labels: ["text", "text", "text", "text", "text"],
            datasets: [{
                label: "Subscribed client",
                backgroundColor: "#182F59",
                borderColor: "#182F59",
                data: [5, 45, 41, 50, 42],
                fill: false,
            }, {
                label: "non- subscribed client",
                backgroundColor: "#5BBC2E",
                borderColor: "#5BBC2E",
                data: [75, 35, 45, 55, 15],
                fill: false,
            },],
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
}


$(function () {
    $('input[name="daterange"]').daterangepicker({
        autoUpdateInput: false,
        locale: {
            cancelLabel: "Clear",
        },
    });

    $('input[name="daterange"]').on(
        "apply.daterangepicker",
        function (ev, picker) {
            $(this).val(
                picker.startDate.format("MM/DD/YYYY") +
                " - " +
                picker.endDate.format("MM/DD/YYYY")
            );
        }
    );
});

const userInfoFilterContaner = document.querySelector(".filter-options")
const userInfoFilters = document.querySelectorAll(".filter-options .btn")

userInfoFilters.forEach(btn => {
    btn.addEventListener("click", () => {
        const currentOption = userInfoFilterContaner.querySelector(".active")
        currentOption.classList.remove("active")
        btn.classList.add("active")
    })
})

$(document).ready(function () {
    $("#all-user-info").DataTable({
        scrollX: true,
        info: false,
        sorting: false,
        oLanguage: {
            sLengthMenu: "Sub-service list",
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
        "initComplete": function (settings, json) {
            $('body').find('.dataTables_scrollBody').addClass("scrollbar");
        },
        "paging": false,
    });

    $(".selectAll").on("click", function (e) {
        if ($(this).is(":checked")) {
            $("#all-user-info").DataTable().rows().select();
        } else {
            $("#all-user-info").DataTable().rows().deselect();
        }
    });

    $("#individual-user-info").DataTable({
        responsive: true,
        info: false,
        columnDefs: [{
            // className: 'select-checkbox',
            orderable: false,
            targets: [-1]
        }],
        select: {
            style: 'multi+shift',
            selector: 'td:first-child'
        },
        sorting: false,
        oLanguage: {
            sLengthMenu: "Sub-service list",
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
        "paging": false,
    });

    $("#admin-list").DataTable({
        responsive: true,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: [-1]
        }],
        sorting: false,
        searching: false,
        "paging": false,
    });
})








