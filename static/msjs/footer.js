var footerBox = document.querySelectorAll(".footer-box");
console.log(footerBox);
footerBox.forEach((element, index) => {
  element.addEventListener("click", function () {
    element.classList.toggle("expand-box");
    element.classList.toggle("caret-down");
    for (let i = 0; i < footerBox.length; i++) {
      if (i != index) {
        footerBox[i].classList.remove("expand-box");
        footerBox[i].classList.remove("caret-down");
      }
    }
  });
});
