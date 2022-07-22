$(document).ready(function () {
  var ccsInput = $("#ra-service");
  var ciInput = $("#sc-service");
  var irInput = $("#ir-service");
  var smbInput = $("#smb-service");
  var acaInput = $("#aca-service");

  var ccsBox = $("#ra-service-box");
  var ciBox = $("#sc-service-box");
  var irBox = $("#ir-service-box");
  var ssBox = $("#ss-service-box");
  var acaBox = $("#aca-service-box");

  ccsInput.click(function () {
    if ($(this).prop("checked") == true) {
      ccsBox.show();
      ciBox.hide();
      irBox.hide();
      ssBox.hide();
      acaBox.hide();
      ciInput.prop("checked", false);
      irInput.prop("checked", false);
      smbInput.prop("checked", false);
      acaInput.prop("checked", false);
    } else if ($(this).prop("checked") == false) {
      ccsBox.hide();
    }
  });
  ciInput.click(function () {
    if ($(this).prop("checked") == true) {
      ccsBox.hide();
      ssBox.show();
      irBox.hide();
      ciBox.hide();
      acaBox.hide();
      ccsInput.prop("checked", false);
      irInput.prop("checked", false);
      smbInput.prop("checked", false);
      acaInput.prop("checked", false);
    } else if ($(this).prop("checked") == false) {
      ssBox.hide();
    }
  });
  irInput.click(function () {
    if ($(this).prop("checked") == true) {
      ccsBox.hide();
      ciBox.hide();
      irBox.show();
      ssBox.hide();
      acaBox.hide();
      ccsInput.prop("checked", false);
      ciInput.prop("checked", false);
      smbInput.prop("checked", false);
      acaInput.prop("checked", false);
    } else if ($(this).prop("checked") == false) {
      irBox.hide();
    }
  });
  smbInput.click(function () {
    if ($(this).prop("checked") == true) {
      ccsBox.hide();
      ssBox.hide();
      irBox.hide();
      ciBox.show();
      acaBox.hide();
      ccsInput.prop("checked", false);
      ciInput.prop("checked", false);
      irInput.prop("checked", false);
      acaInput.prop("checked", false);
    } else if ($(this).prop("checked") == false) {
      ciBox.hide();
    }
  });
  acaInput.click(function () {
    if ($(this).prop("checked") == true) {
      ccsBox.hide();
      ciBox.hide();
      irBox.hide();
      acaBox.show();
      ssBox.hide();
      ccsInput.prop("checked", false);
      ciInput.prop("checked", false);
      irInput.prop("checked", false);
      smbInput.prop("checked", false);
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
  var inq_inputs = $(".inq-form");

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
    request.hide();
    virtual.hide();
    inquery.show();
    for (var i = 0; i < call_inputs.length; i++) {
      call_inputs[i].required = false;
      call_inputs[i].value = "";
    }
    for (var i = 0; i < inq_inputs.length; i++) {
      inq_inputs[i].required = true;
    }
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

  var ccisInput = $("#va-service");
  var ccisl = $("#ccisl");
  var osiInput = $("#pt-service");
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

  var mssInput = $("#mss-service");
  var msssl = $("#msssl");
  var ppsInput = $("#pps-service");
  var ppssl = $("#ppssl");

  mssInput.click(function () {
    if ($(this).prop("checked") == true) {
      msssl.show();
      ppssl.hide();
      ppsInput.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      ppssl.hide();
    }
  });

  var isoInput = $("#iso-service");
  var isosl = $("#isosl");
  var pciInput = $("#pci-service");
  var pcisl = $("#pcisl");
  var hippInput = $("#hipp-service");
  var hippsl = $("#hippsl");
  var gdpInput = $("#gdp-service");
  var gdpsl = $("#gdpsl");

  isoInput.click(function () {
    if ($(this).prop("checked") == true) {
      isosl.show();
      pcisl.hide();
      hippsl.hide();
      gdpsl.hide();
      pciInput.prop("checked", false);
      hippInput.prop("checked", false);
      gdpInput.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      isosl.hide();
    }
  });

  pciInput.click(function () {
    if ($(this).prop("checked") == true) {
      isosl.hide();
      pcisl.show();
      hippsl.hide();
      gdpsl.hide();
      isoInput.prop("checked", false);
      hippInput.prop("checked", false);
      gdpInput.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      pcisl.hide();
    }
  });
  hippInput.click(function () {
    if ($(this).prop("checked") == true) {
      isosl.hide();
      pcisl.hide();
      hippsl.show();
      gdpsl.hide();
      pciInput.prop("checked", false);
      isoInput.prop("checked", false);
      gdpInput.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      hippsl.hide();
    }
  });

  gdpInput.click(function () {
    if ($(this).prop("checked") == true) {
      isosl.hide();
      pcisl.hide();
      hippsl.hide();
      gdpsl.show();
      pciInput.prop("checked", false);
      isoInput.prop("checked", false);
      hippInput.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      hippsl.hide();
    }
  });

  var eiInput = $("#ei-service");
  var ctInput = $("#ct-service");
  var lawInput = $("#law-service");

  var eisl = $("#eisl");
  var ctsl = $("#ctsl");
  var lawsl = $("#lawsl");

  eiInput.click(function () {
    if ($(this).prop("checked") == true) {
      ctsl.hide();
      lawsl.hide();
      eisl.show();
      ctInput.prop("checked", false);
      lawInput.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      eisl.hide();
    }
  });

  ctInput.click(function () {
    if ($(this).prop("checked") == true) {
      eisl.hide();
      lawsl.hide();
      ctsl.show();
      eiInput.prop("checked", false);
      lawInput.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      ctsl.hide();
    }
  });

  lawInput.click(function () {
    if ($(this).prop("checked") == true) {
      eisl.hide();
      ctsl.hide();
      lawsl.show();
      ctInput.prop("checked", false);
      eiInput.prop("checked", false);
    }
    if ($(this).prop("checked") == false) {
      lawsl.hide();
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

  var wr = $("#wr");
  var wson = $("#wson");
  var sdc = $("#sdc");
  var ci = $("#ci");
  var fahr = $("#fahr");
  var sa = $("#sa");
  var hrArrays = [wr, wson, sdc, ci, fahr];
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

  var wm = $("#wm");
  var wsonr = $("#wsonr");
  var sdcm = $("#sdcm");
  var sam = $("#sam");
  var mrArrays = [wm, wsonr, sdcm];
  var satm = $("#select-all-textm");

  sam.click(function () {
    if ($(this).prop("checked") == true) {
      for (var i = 0; i < mrArrays.length; i++) {
        mrArrays[i].prop("checked", true);
        satm.text("Unselect All");
      }
    } else {
      for (let i = 0; i < mrArrays.length; i++) {
        mrArrays[i].prop("checked", false);
        satm.text("Select All");
      }
    }
  });

  var bfi = $("#bfi");
  var idti = $("#idti");
  var ehdt = $("#ehdt");
  var sac = $("#sac");
  var drArrays = [bfi, idti, ehdt];
  var satd = $("#select-all-textm");

  sac.click(function () {
    if ($(this).prop("checked") == true) {
      for (var i = 0; i < drArrays.length; i++) {
        drArrays[i].prop("checked", true);
        satd.text("Unselect All");
      }
    } else {
      for (let i = 0; i < drArrays.length; i++) {
        drArrays[i].prop("checked", false);
        satd.text("Select All");
      }
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
