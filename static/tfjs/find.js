const tabLinkLg = document.querySelectorAll(".link-lg");
const tabLinkSm = document.querySelectorAll(".link-sm");
const tabBoxLg = document.querySelectorAll(".tab-lg");
const tabBoxSm = document.querySelectorAll(".tab-sm");

tabLinkLg.forEach((element, index) => {
  element.addEventListener("click", () => {
    for (var i = 0; i < tabLinkLg.length; i++) {
      if (i != index) {
        tabBoxLg[i].style.display = "none";
        tabBoxSm[i].style.display = "none";
        tabLinkLg[i].classList.remove("link-active");
        tabLinkSm[i].classList.remove("link-active");
      } else {
        tabBoxLg[i].style.display = "block";
        tabBoxSm[i].style.display = "block";
        tabLinkLg[i].classList.add("link-active");
        tabLinkSm[i].classList.add("link-active");
      }
    }
  });
});
tabLinkSm.forEach((element, index) => {
  element.addEventListener("click", () => {
    for (var i = 0; i < tabLinkLg.length; i++) {
      if (i != index) {
        tabBoxLg[i].style.display = "none";
        tabBoxSm[i].style.display = "none";
        tabLinkLg[i].classList.remove("link-active");
        tabLinkSm[i].classList.remove("link-active");
      } else {
        tabBoxLg[i].style.display = "block";
        tabBoxSm[i].style.display = "block";
        tabLinkLg[i].classList.add("link-active");
        tabLinkSm[i].classList.add("link-active");
      }
    }
  });
});
