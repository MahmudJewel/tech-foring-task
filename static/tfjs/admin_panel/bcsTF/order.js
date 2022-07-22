
$(document).ready(function () {
    // console.log('data-table');
    $("#order-table").DataTable({
        scrollx: true,
        scrollCollapse: true,
        paging: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
        info: false,
        sorting: false,
    });;
});
