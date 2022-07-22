$(document).ready(function () {
    // console.log('data-table');
    $("#notification-table").DataTable({
        scrollY: "210px",
        scrollCollapse: true,
        info: false,
        "order": [],
        "initComplete": function(settings, json) {
            $('body').find('.dataTables_scrollBody').addClass("scrollbar");
        },
        oLanguage: {
            sSearch: `<i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });
});


const deleteRowBtn = document.querySelectorAll(".dlt")

deleteRowBtn.forEach(btn=>{
    btn.addEventListener("click", ()=>{
        btn.parentElement.parentElement.classList.add("d-none")
    })
})