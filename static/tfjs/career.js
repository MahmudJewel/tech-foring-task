const posbtn = document.querySelectorAll(".pos-btn");
const crossBtn = document.querySelectorAll(".cross-btn");
const psBox = document.querySelectorAll(".position-box");
const cLink = document.querySelectorAll(".c-link");
const circular = document.querySelectorAll(".circular");

posbtn.forEach((element) => {
  element.addEventListener("click", function () {
    element.nextElementSibling.style.display = "block";
  });
});
crossBtn.forEach((element) => {
  element.addEventListener("click", function () {
    element.parentElement.style.display = "none";
  });
});
cLink.forEach((element) => {
  element.addEventListener("click", function () {
    element.nextElementSibling.style.display = "block";
  });
});
