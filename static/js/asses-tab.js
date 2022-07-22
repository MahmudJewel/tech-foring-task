const assesImg = document.querySelectorAll(".asses-img");
const assesBox = document.querySelectorAll(".asses-box");
const assesImgSm = document.querySelectorAll(".asses-img-sm");
const assesTab = document.querySelectorAll(".asses-tab");
console.log(assesImg);
console.log(assesBox);
console.log(assesImgSm);
console.log(assesTab);

assesImg.forEach((element, index) => {
  element.addEventListener("click", function () {
    assesBox[index].style.display = "block";
    assesTab[index].style.display = "block";
    for (let i = 0; i < assesBox.length; i++) {
      if (i != index) {
        assesBox[i].style.display = "none";
        assesTab[i].style.display = "none";
      }
    }
  });
});
assesImgSm.forEach((element, index) => {
  element.addEventListener("click", function () {
    assesBox[index].style.display = "block";
    assesTab[index].style.display = "block";
    for (let i = 0; i < assesBox.length; i++) {
      if (i != index) {
        assesBox[i].style.display = "none";
        assesTab[i].style.display = "none";
      }
    }
  });
});
