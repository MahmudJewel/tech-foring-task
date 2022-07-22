$(document).ready(function () {
  var $tabs = $("#horizontalTab");
  $tabs.responsiveTabs({
    startCollapsed: "accordion",
    collapsible: "accordion",
  });
});

const openModal = document.getElementById("video-open-btn");
// const closeModal = document.getElementById("video-close-btn");
const videoModal = document.getElementById("video-modal");
openModal.addEventListener("click", function () {
  videoModal.style.display = "flex";
});

new Glide(".glide", {
  type: "carousel",
  startAt: 0,
  perView: 2,
  autoplay: 3000,
  keyboard: true,
  breakpoints: {
    800: {
      perView: 1,
    },
  },
}).mount();
