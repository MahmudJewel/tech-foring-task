$(document).ready(function () {
    $("#sub-service-list").DataTable({
        scrollY: "410px",
        scrollCollapse: true,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: -1
        }],
        sorting: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
        "initComplete": function (settings, json) {
            $('body').find('.dataTables_scrollBody').addClass("scrollbar");
        },
        "paging": false,
    });
    $("#reading-list").DataTable({
        scrollX: true,
        scrollCollapse: true,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: -1
        }],
        sorting: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
        "paging": false,
    });
})


const addServiceBtn = document.querySelector(".addService")
const addServiceFormCloses = document.querySelectorAll(".form-close")
const backToList = document.querySelector(".form-close-back")
const addServiceForm = document.querySelector(".add-form")
const tableContainer = document.querySelector(".table-container")
const formFirstPart = document.querySelectorAll("#div_id_category,#div_id_service_icon,#div_id_service_title,#div_id_short_description, #div_id_has_sub_service, #div_id_is_subscription_based,#div_sales")
const formSecondPart = document.querySelectorAll("#div_id_service_header, #div_id_service_body, #div_id_service_footer, .saveService")
const serviceHeader = document.querySelector("#div_id_service_header")
console.log(formFirstPart)
// display service form
addServiceBtn.addEventListener("click", () => {
    // hide service List
    tableContainer.classList.add("d-none")
    // show service List
    addServiceForm.classList.remove("d-none")
    // show back Button
    backToList.classList.remove("d-none")
    // show first part of the form
    formFirstPart.forEach(item => {
        item.classList.remove("d-none")
    })
    // show hide rich text editors
    formSecondPart.forEach(item => {
        item.classList.add("d-none")
    })
    // check if next button exist
    const nextBtnCheck = document.querySelector(".nextBtn")
    if (nextBtnCheck === null) {
        const nextBtn = document.createElement("button")
        nextBtn.classList.add('btn', 'btn-primary', 'nextBtn', 'text-capitalize')
        nextBtn.textContent = "Next"
        serviceHeader.insertAdjacentElement("beforebegin", nextBtn)
        nextBtn.addEventListener("click", (e) => {
            e.preventDefault()
            formSecondPart.forEach(item => {
                item.classList.remove("d-none")
            })
            formFirstPart.forEach(item => {
                item.classList.add("d-none")
            })
            nextBtn.remove()
        })
    }
})

const nextBtnCheck = document.querySelector(".nextBtn")

addServiceFormCloses.forEach(addServiceFormClose => {
    addServiceFormClose.addEventListener("click", () => {
        addServiceForm.classList.add("d-none")
        backToList.classList.add("d-none")
        tableContainer.classList.remove("d-none")
    })
})