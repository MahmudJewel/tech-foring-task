$(document).ready(function () {
  //Tap to Link
  var scrollLink = $(".scroll");
  scrollLink.click(function (e) {
    e.preventDefault();
    $("body, html").animate(
      {
        scrollTop: $(this.hash).offset().top - 135,
      },
      800
    );
  });
  $(window).scroll(function () {
    var scrollPos = $(this).scrollTop();
    var navSec = $("#sticky-nav");
    if (scrollPos >= 2756) {
      navSec.css({ opacity: "0" });
    }
    if (scrollPos < 2756) {
      navSec.css({ opacity: "1" });
    }
    scrollLink.each(function () {
      var sectionLocation = $(this.hash).offset().top - 140;
      if (sectionLocation <= scrollPos) {
        $(this).addClass("sticky-active");
        $(this).siblings().removeClass("sticky-active");
      }
    });
  });
});
