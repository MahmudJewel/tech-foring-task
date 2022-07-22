
$(document).ready(function () {
    $("#individual-user-info").DataTable({
        responsive: false,
        "scrollX": true,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: [-1]
        }],
        select: {
            style:    'multi+shift',
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
const overviewRow = document.querySelectorAll("#individual-user-info .service")
const overviewDialogue = document.querySelector(".overview-dialogue")
const overviewDialogueClose = document.querySelector(".close-overview")
overviewRow.forEach(items =>{
    items.addEventListener("click", ()=>{
        overviewDialogue.classList.remove("d-none")
    })
})
overviewDialogueClose.addEventListener("click", ()=>{
    overviewDialogue.classList.add("d-none")
})

