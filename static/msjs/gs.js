$(document).ready(function () {
  var ccsInput = $("#cc-service");
  var ciInput = $("#ci-service");
  var irInput = $("#ir-service");
  var acaInput = $("#aca-service");

  var ccsBox = $("#cc-service-box");
  var ciBox = $("#ci-service-box");
  var irBox = $("#ir-service-box");
  var acaBox = $("#aca-service-box");

  ccsInput.click(function () {
    if ($(this).prop("checked") == true) {
      ccsBox.show();
      ciBox.hide();
      irBox.hide();
      acaBox.hide();
      ciInput.prop("checked", false);
      irInput.prop("checked", false);
      acaInput.prop("checked", false);
    } else if ($(this).prop("checked") == false) {
      ccsBox.hide();
    }
  });
  ciInput.click(function () {
    if ($(this).prop("checked") == true) {
      ccsBox.hide();
      ciBox.show();
      irBox.hide();
      acaBox.hide();
      ccsInput.prop("checked", false);
      irInput.prop("checked", false);
      acaInput.prop("checked", false);
    } else if ($(this).prop("checked") == false) {
      ciBox.hide();
    }
  });
  irInput.click(function () {
    if ($(this).prop("checked") == true) {
      ccsBox.hide();
      ciBox.hide();
      irBox.show();
      acaBox.hide();
      ccsInput.prop("checked", false);
      ciInput.prop("checked", false);
      acaInput.prop("checked", false);
    } else if ($(this).prop("checked") == false) {
      irBox.hide();
    }
  });
  acaInput.click(function () {
    if ($(this).prop("checked") == true) {
      ccsBox.hide();
      ciBox.hide();
      irBox.hide();
      acaBox.show();
      irInput.prop("checked", false);
      ccsInput.prop("checked", false);
      ciInput.prop("checked", false);
    } else if ($(this).prop("checked") == false) {
      acaBox.hide();
    }
  });

  var callBtn = $("#request-btn");
  var inqueryBtn = $("#inquery-btn");
  var virtualBtn = $("#virtual-btn");

  var request = $("#request");
  var inquery = $("#inquery");
  var virtual = $("#virtual");

  var call_inputs = $(".call-input");
  var inq_inputs = $(".inq-input");
  console.log(call_inputs[0]);
  callBtn.click(function () {
    request.css({ display: "block" });
    $(this).css("border-bottom", "3px solid #111125");
    for (var i = 0; i < call_inputs.length; i++) {
      call_inputs[i].required = true;
    }
    for (var i = 0; i < inq_inputs.length; i++) {
      inq_inputs[i].required = false;
      inq_inputs[i].value = "";
    }
    virtual.hide();
    inquery.hide();
    inqueryBtn.css("border-bottom", "3px solid gray");
    virtualBtn.css("border-bottom", "3px solid gray");
  });
  inqueryBtn.click(function () {
    for (var i = 0; i < inq_inputs.length; i++) {
      inq_inputs[i].required = true;
    }
    for (var i = 0; i < call_inputs.length; i++) {
      call_inputs[i].required = false;
      call_inputs[i].value = "";
    }
    request.hide();
    virtual.hide();
    inquery.show();
    $(this).css("border-bottom", "3px solid #111125");
    callBtn.css("border-bottom", "3px solid gray");
    virtualBtn.css("border-bottom", "3px solid gray");
  });

  virtualBtn.click(function () {
    request.hide();
    virtual.css("display", "flex");
    $(this).css("border-bottom", "3px solid #111125");
    inquery.hide();
    inqueryBtn.css("border-bottom", "3px solid gray");
    callBtn.css("border-bottom", "3px solid gray");
  });

  var ccisInput = $("#cci-service");
  var ccisl = $("#ccisl");
  var osiInput = $("#osi-service");
  var osisl = $("#osisl");

  ccisInput.click(function () {
    if ($(this).prop("checked") == true) {
      ccisl.show();
      osisl.hide();
      osiInput.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      ccisl.hide();
    }
  });

  osiInput.click(function () {
    if ($(this).prop("checked") == true) {
      osisl.show();
      ccisl.hide();
      ccisInput.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      osisl.hide();
    }
  });

  var hrService = $("#hr-service");
  var mrService = $("#mr-service");
  var drService = $("#dr-service");

  var hrList = $("#hr-sub-list");
  var mrList = $("#mr-sub-list");
  var drList = $("#dr-sub-list");

  hrService.click(function () {
    if ($(this).prop("checked") == true) {
      hrList.show();
      mrList.hide();
      drList.hide();

      mrService.prop("checked", false);
      drService.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      hrList.hide();
    }
  });
  mrService.click(function () {
    if ($(this).prop("checked") == true) {
      mrList.show();
      hrList.hide();
      drList.hide();

      hrService.prop("checked", false);
      drService.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      mrList.hide();
    }
  });
  drService.click(function () {
    if ($(this).prop("checked") == true) {
      hrList.hide();
      mrList.hide();
      drList.show();

      mrService.prop("checked", false);
      hrService.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      drList.hide();
    }
  });

  var smhr = $("#smhr");
  var ehr = $("#ehr");
  var dhr = $("#dhr");
  var pcar = $("#pcar");
  var fahr = $("#fahr");
  var sa = $("#sa");
  var hrArrays = [smhr, ehr, dhr, pcar, fahr];
  var sat = $("#select-all-text");

  sa.click(function () {
    if ($(this).prop("checked") == true) {
      for (var i = 0; i < hrArrays.length; i++) {
        hrArrays[i].prop("checked", true);
        sat.text("Unselect All");
      }
    } else {
      for (let i = 0; i < hrArrays.length; i++) {
        hrArrays[i].prop("checked", false);
        sat.text("Select All");
      }
    }
  });

  var ccspService = $("#ccsp-service");
  var ccspsl = $("#ccspsl");

  ccspService.click(function () {
    if ($(this).prop("checked") == true) {
      ccspsl.show();
    } else {
      ccspsl.hide();
    }
  });

  var pcspBtn = $("#pcsp-btn");
  var pcsPart = $("#pcs-part");
  var gtPoint = $(".gt-point2");
  pcspBtn.click(function (e) {
    e.preventDefault();
    gtPoint.css("display", "block");
    var pcsLocation = pcsPart.offset().top;
    $("body, html").animate({ scrollTop: pcsLocation }, 1000);
  });
});
const modalOpenBtn = document.getElementById("pm-open");
const modalCloseBtn = document.getElementById("pm-close");
const pointModal = document.getElementById("point-modal");
const gtPoint = document.getElementById("pcs-part");

modalOpenBtn.addEventListener("click", function () {
  pointModal.style.display = "flex";
  gtPoint.style.display = "none";
});
modalCloseBtn.addEventListener("click", function () {
  pointModal.style.display = "none";
});
console.log(pointModal);
