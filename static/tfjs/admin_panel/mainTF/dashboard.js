// let expanded = false;

const showCheckboxes = (checkboxes) => {
    console.log(checkboxes);
    if (!expanded) {
        checkboxes.style.display = "block";
        expanded = true;
    } else {
        checkboxes.style.display = "none";
        expanded = false;
    }
};

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

$(document).ready(function () {
    // console.log('data-table');
    $("#activites-table").DataTable({
        scrollY: "210px",
        scrollCollapse: true,
        paging: false,
        searching: false,
        info: false,
        sorting: false,
    });
    $("#users-table").DataTable({
        scrollY: "210px",
        scrollCollapse: true,
        paging: false,
        searching: false,
        info: false,
        sorting: false,
    });
});
const firstBox = document.getElementById("firstBox");
const secondBox = document.getElementById("secondBox");

const showDetailOption = (box) => {
    if (box == firstBox) {
        secondBox.classList.remove("show-detail");
        box.classList.add("show-detail");
    } else {
        firstBox.classList.remove("show-detail");
        box.classList.add("show-detail");
    }
};

const useraStats = document.querySelectorAll(".user-stat-bubble");
const businessUsersDetail = document.querySelector(".business-users-detail");
const individualUser = document.querySelector(".individual-users");
const businessUser = document.querySelector(".business-users");
const businessUsersDetailClose = document.querySelector(".business-btn-close");
const individualUsersDetailClose = document.querySelector(".individual-btn-close");
const individualUsersDetail = document.querySelector(".individual-users-detail");
useraStats.forEach((useraStat) => {
    useraStat.addEventListener("click", () => {
        if (useraStat.classList.contains("business-users") === true) {
            useraStat.style.opacity = "0";
            businessUsersDetail.style.transform = "translateX(0)";
            businessUsersDetail.style.display = "block";
            individualUser.style.opacity = "1";
            individualUsersDetail.style.transform = "translateX(-100rem)"
            individualUsersDetail.style.display = "none";
        } else {
            useraStat.style.opacity = "0";
            businessUsersDetail.style.transform = "translateX(-100rem)";
            businessUsersDetail.style.display = "none";
            businessUser.style.opacity = "1";
            individualUsersDetail.style.transform = "translateX(0)"
            individualUsersDetail.style.display = "block";
        }
        businessUsersDetailClose.addEventListener("click", () => {
            businessUsersDetail.style.transform = "translateX(-100rem)";
            businessUsersDetail.style.display = "none";
            useraStat.style.opacity = "1";
        });
        individualUsersDetailClose.addEventListener("click", () => {
            individualUsersDetail.style.transform = "translateX(-100rem)";
            useraStat.style.opacity = "1";
            individualUsersDetail.style.display = "none";
        });
    });
});
