$(function () {
    $('#daterange').daterangepicker({
        "autoApply": true,
        "autoUpdateInput": false,
        locale: {
            cancelLabel: "Clear",
        },
    });

    $('#daterange').on(
        "apply.daterangepicker",
        function (ev, picker) {
            $(this).val(
                picker.startDate.format("MM/DD/YYYY") +
                    " - " +
                    picker.endDate.format("MM/DD/YYYY")
            );
        }
    )
});

$(document).ready(function () {
    $("#event-list").DataTable({
        info: false,
        scrollX: true,
        sorting: false,
        searching: false,
        columnDefs: [{
            orderable: false,
            targets: -1
        }],
    });
    $("#event-details").DataTable({
        info: false,
        responsive: true,
        columnDefs: [{
            orderable: false,
            targets: -1
        }],
        oLanguage: {
            sSearch: `<i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });
    // All tickets page data table call
    $("#personal-tickets-table").DataTable({
        // responsive: true,
        // columnDefs: [{
        //     orderable: false,
        //     targets: -1
        // }],
        info: false,
        "pageLength": 2,
        "lengthMenu": [2, 4, 8, 16, 24],
        sorting: false,
        oLanguage: {
            sLengthMenu: "Result Per Page _MENU_",
            sSearch: `<i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });
    $("#business-tickets-table").DataTable({
        // responsive: true,
        // columnDefs: [{
        //     orderable: false,
        //     targets: -1
        // }],
        info: false,
        "pageLength": 2,
        "lengthMenu": [2, 4, 8, 16, 24],
        sorting: false,
        oLanguage: {
            sLengthMenu: "Result Per Page _MENU_",
            sSearch: `<i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });
    $("#academy-tickets-table").DataTable({
        // responsive: true,
        // columnDefs: [{
        //     orderable: false,
        //     targets: -1
        // }],
        info: false,
        "pageLength": 2,
        "lengthMenu": [2, 4, 8, 16, 24],
        sorting: false,
        oLanguage: {
            sLengthMenu: "Result Per Page _MENU_",
            sSearch: `<i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });

    $("#business-tickets-table_wrapper").addClass("d-none")
    $("#academy-tickets-table_wrapper").addClass("d-none")
    
    $('.ticketFilterBtn').on('click', function() {
        if($(this).hasClass("personal")){
            $("#personal-tickets-table_wrapper").removeClass("d-none")
            $("#business-tickets-table_wrapper").addClass("d-none")
            $("#academy-tickets-table_wrapper").addClass("d-none")
        }
        else if($(this).hasClass("business")){
            $("#personal-tickets-table_wrapper").addClass("d-none")
            $("#business-tickets-table_wrapper").removeClass("d-none")
            $("#academy-tickets-table_wrapper").addClass("d-none")
        }
        else if($(this).hasClass("academy")){
            $("#personal-tickets-table_wrapper").addClass("d-none")
            $("#business-tickets-table_wrapper").addClass("d-none")
            $("#academy-tickets-table_wrapper").removeClass("d-none")
        }
    });

});

const filterSelect = document.querySelector("#filter");
const byStatus = document.querySelectorAll(".byStatus");
const byMedium = document.querySelectorAll(".byMedium");
const filterBtnContainer = document.querySelector(".filter-btn-container");
const filterBtns = document.querySelectorAll(".event-filter-btn");
const ticketFilterContainer = document.querySelector(".ticket-filter");
const ticketFilterBtns = document.querySelectorAll(".ticketFilterBtn");
const table = document.querySelectorAll("#event-list tbody tr")
const findRow = (sats) => {
    console.log(sats);
    table.forEach(tr => {
        const tData = tr.querySelectorAll(".filter")
        tData.forEach(text => {
            console.log(text.classList.contains(sats));
            if(sats === "all event"){
                text.parentElement.classList.remove( "d-none")
            }
            else if(!text.classList.contains(sats)){
                text.parentElement.classList.add( "d-none")
            }
            else if(text.classList.contains(sats)){
                text.parentElement.classList.remove( "d-none")
            }

        })
    })
}

filterBtns.forEach((filterBtn) => {
    filterBtn.addEventListener("click", () => {
        const curentBtn = filterBtnContainer.querySelector(".active");
        curentBtn.classList.remove("active");
        filterBtn.classList.add("active");
        findRow(filterBtn.innerText.toLowerCase())
    });
});

ticketFilterBtns.forEach((ticketFilterBtn) => {
    ticketFilterBtn.addEventListener("click", () => {
        const curentBtn = ticketFilterContainer.querySelector(".active");
        curentBtn.classList.remove("active");
        ticketFilterBtn.classList.add("active");
    });
});
const stat = document.querySelectorAll(".active, .canceled, .deactivated, .completed")
const med = document.querySelectorAll(".offline, .online")
filterSelect?.addEventListener("change", () => {
    if (filterSelect.value == "status") {
        byStatus.forEach((status) => {
            status.style.display = "inline-block";
        });
        stat.forEach(sta=>{
            sta.classList.add("filter")
        })
        med.forEach(me=>{
            me.classList.remove("filter")
        })
        byMedium.forEach((medium) => {
            medium.style.display = "none";
        });
    }
    if (filterSelect.value == "medium") {
        byStatus.forEach((status) => {
            status.style.display = "none";
        });
        stat.forEach(sta=>{
            sta.classList.remove("filter")
        })
        med.forEach(me=>{
            me.classList.add("filter")
        })
        byMedium.forEach((medium) => {
            medium.style.display = "inline-block";
        });
    }
});

//const deleteBtn = document.querySelectorAll(".trash, .dlt")
//
//deleteBtn.forEach(btn=>{
//    btn.addEventListener("click",()=>{
//        btn.parentElement.parentElement.style.display = "none"
//    })
//})



