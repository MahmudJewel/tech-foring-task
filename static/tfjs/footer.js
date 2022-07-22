// $(document).ready(function () {
//   var footerBox = $(".footer-box");
//   console.log(footerBox);
//   $.each(footerBox, function (index, element) {
//     console.log(element);
//     element.click(function () {
//       console.log("Element" + index);
//     });
//   });
// });
var footerBox = document.querySelectorAll(".footer-box");
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
