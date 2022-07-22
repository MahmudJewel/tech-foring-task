const tabLink = document.querySelectorAll(".pro-tab-link");
const tab = document.querySelectorAll(".pro-tab");

tabLink.forEach((element, index) => {
  element.addEventListener("click", function () {
    for (var i = 0; i < tab.length; i++) {
      if (i != index) {
        tab[i].style.display = "none";
        tabLink[i].classList.remove("pro-tab-active");
      } else {
        tab[i].style.display = "block";
        tabLink[i].classList.add("pro-tab-active");
      }
    }
  });
});
