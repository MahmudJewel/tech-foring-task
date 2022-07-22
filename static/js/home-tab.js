const hTab = document.querySelectorAll(".htab");
const hTabBox = document.querySelectorAll(".hs-tab-box");
const hTabSm = document.querySelectorAll(".htab-sm");
const hTabBoxSm = document.querySelectorAll(".hs-tab-box-sm");

const colors = ["#e4202c", "#ffc922", "#2c235a", "#11adf7"];
hTab.forEach((element, index) => {
  element.addEventListener("click", function () {
    hTabBox[index].style.display = "block";
    hTabBoxSm[index].style.display = "block";
    element.style.borderBottom = "3px solid " + colors[index];
    hTabSm[index].style.borderBottom = "3px solid " + colors[index];
    for (let i = 0; i < hTabBox.length; i++) {
      if (i != index) {
        hTabBox[i].style.display = "none";
        hTab[i].style.borderBottom = "3px solid white";
        hTabBoxSm[i].style.display = "none";
        hTabSm[i].style.borderBottom = "3px solid white";
      }
    }
  });
});

hTabSm.forEach((element, index) => {
  element.addEventListener("click", function () {
    hTabBoxSm[index].style.display = "block";
    hTabBox[index].style.display = "block";
    element.style.borderBottom = "3px solid " + colors[index];
    hTab[index].style.borderBottom = "3px solid " + colors[index];
    for (let i = 0; i < hTabBoxSm.length; i++) {
      if (i != index) {
        hTabBoxSm[i].style.display = "none";
        hTabSm[i].style.borderBottom = "3px solid white";
        hTabBox[i].style.display = "none";
        hTab[i].style.borderBottom = "3px solid white";
      }
    }
  });
});
