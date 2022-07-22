$(document).ready(function () {
    $("#blogList").DataTable({
        scrollX: true,
        scrollCollapse: true,
        paging: false,
        searching: true,
        info: false,
        sorting: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });
    $("#commentList").DataTable({
        scrollX: true,
        scrollCollapse: true,
        paging: false,
        searching: true,
        info: false,
        sorting: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });
    $("#categoryList").DataTable({
        scrollX: true,
        scrollCollapse: true,
        paging: false,
        searching: true,
        info: false,
        sorting: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });
    $("#subCategoryList").DataTable({
        scrollX: true,
        scrollCollapse: true,
        paging: false,
        searching: true,
        info: false,
        sorting: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });
    $("#filterOptionList").DataTable({
        scrollX: true,
        scrollCollapse: true,
        paging: false,
        searching: true,
        info: false,
        sorting: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });

});
