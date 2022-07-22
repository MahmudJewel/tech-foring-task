$(document).ready(function () {
  var tab1 = $("#tab-link1");
  var tab2 = $("#tab-link2");
  var tab3 = $("#tab-link3");
  var tab4 = $("#tab-link4");

  var tabPan1 = $("#tab-pan1");
  var tabPan2 = $("#tab-pan2");
  var tabPan3 = $("#tab-pan3");
  var tabPan4 = $("#tab-pan4");
  tab1.click(function () {
    tabPan1.show();
    tabPan2.hide();
    tabPan3.hide();
    tabPan4.hide();
  });
  tab2.click(function () {
    tabPan2.show();
    tabPan1.hide();
    tabPan3.hide();
    tabPan4.hide();
  });
  tab3.click(function () {
    tabPan3.show();
    tabPan2.hide();
    tabPan1.hide();
    tabPan4.hide();
  });
  tab4.click(function () {
    tabPan4.show();
    tabPan2.hide();
    tabPan3.hide();
    tabPan1.hide();
  });
});
