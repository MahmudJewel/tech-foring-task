$(document).ready(function () {
  //Service Buttons and Drop Variables
  var serviceBtn = $("#service-btn");
  var serviceDrop = $("#service-drop");
  var ccsBtn = $("#ccs-btn");
  var deviceSecCcs = $("#device-sec-ccs");
  var deviceSecVr = $("#device-sec-vr");
  var mediaSec = $("#media-sec");
  var cloudSec = $("#cloud-sec");
  var emailSec = $("#email-sec");
  var paymentSec = $("#payment-sec");
  var wifiSec = $("#wifi-sec");
  var ciBtn = $("#ci-btn");
  var ciDrop = $("#ci-drop");
  var oi = $("#oi");
  var ci = $("#ci");
  var textBox = $("#text-box");
  var irBtn = $("#ir-btn");
  var irDrop = $("#ir-drop");
  var vr = $("#vr");
  var hr = $("#hr");
  var dr = $("#dr");
  var linkBox = $("#link-box");
  //Social Button and Drop Variables
  var socialBtn = $("#social-btn");
  var socialDrop = $("#social-drop");
  var facebook = $("#facebook");
  var fbInput = $("#fb-input");
  var twitter = $("#twitter");
  var twitterInput = $("#twitter-input");
  var insta = $("#insta");
  var instaInput = $("#insta-input");
  var link = $("#link");
  var linkInput = $("#link-input");
  var pint = $("#pint");
  var pintInput = $("#pint-input");
  var youtube = $("#youtube");
  var youtubeInput = $("#youtube-input");
  var snap = $("#snap");
  var snapInput = $("#snap-input");
  var whats = $("#whats");
  var whatsInput = $("#whats-input");
  // Payment Button and Drop Variables
  var paymentBtn = $("#payment-btn");
  var paymentDrop = $("#payment-drop");
  var paypal = $("#paypal");
  var skrill = $("#skrill");
  var visa = $("#visa");
  var bank = $("#bank");
  var paypalInput = $("#paypal-input");
  var skrillInput = $("#skrill-input");
  var visaInput = $("#visa-input");
  var bankInput = $("#bank-input");
  // Email Button and Drop Variables
  var emailBtn = $("#email-btn");
  var emailDrop = $("#email-drop");
  var yahoo = $("#yahoo");
  var hotmail = $("#hotmail");
  var gmail = $("#gmail");
  var outlook = $("#outlook");
  var customMail = $("#customMail");
  var yahooInput = $("#yahoo-input");
  var hotmailInput = $("#hotmail-input");
  var gmailInput = $("#gmail-input");
  var outlookInput = $("#outlook-input");
  var customMailInput = $("#customMail-input");
  // Cloud Button and Drop Variables
  var cloudBtn = $("#cloud-btn");
  var cloudDrop = $("#cloud-drop");
  var icloud = $("#icloud");
  var gcloud = $("#gcloud");
  var dropbox = $("#dropbox");
  var googleDrive = $("#googleDrive");
  var icloudInput = $("#icloud-input");
  var gcloudInput = $("#gcloud-input");
  var dropboxInput = $("#dropbox-input");
  var googleDriveInput = $("#googleDrive-input");
  // Device Button and Drop Variables
  var deviceBtnCcs = $("#device-btn-ccs");
  var deviceDropCcs = $("#device-drop-ccs");
  var mobileBtnCcs = $("#mobile-btn-ccs");
  var mobileDropCcs = $("#mobile-drop-ccs");
  var androidCcs = $("#android-ccs");
  var androidInputCcs = $("#android-input-ccs");
  var iosCcs = $("#ios-ccs");
  var iosInputCcs = $("#ios-input-ccs");
  var pcBtnCcs = $("#pc-btn-ccs");
  var pcDropCcs = $("#pc-drop-ccs");
  var windowsCcs = $("#windows-ccs");
  var windowsInputCcs = $("#windows-input-ccs");
  var macCcs = $("#mac-ccs");
  var macInputCcs = $("#mac-input-ccs");
  var linuxCcs = $("#linux-ccs");
  var linuxInputCcs = $("#linux-input-ccs");
  var stvBtnCcs = $("#stv-btn-ccs");
  var stvInputCcs = $("#stv-input-ccs");
  //For VR
  var deviceBtnVr = $("#device-btn-vr");
  var deviceDropVr = $("#device-drop-vr");
  var mobileBtnVr = $("#mobile-btn-vr");
  var mobileDropVr = $("#mobile-drop-vr");
  var androidVr = $("#android-vr");
  var androidInputVr = $("#android-input-vr");
  var iosVr = $("#ios-vr");
  var iosInputVr = $("#ios-input-vr");
  var pcBtnVr = $("#pc-btn-vr");
  var pcDropVr = $("#pc-drop-vr");
  var windowsVr = $("#windows-vr");
  var windowsInputVr = $("#windows-input-vr");
  var macVr = $("#mac-vr");
  var macInputVr = $("#mac-input-vr");
  var linuxVr = $("#linux-vr");
  var linuxInputVr = $("#linux-input-vr");
  var stvBtnVr = $("#stv-btn-vr");
  var stvInputVr = $("#stv-input-vr");
  //Service Selection
  serviceBtn.click(function (event) {
    event.preventDefault();
    serviceDrop.slideToggle();
    ciDrop.slideUp();
    irDrop.slideUp();
  });
  ccsBtn.click(function (event) {
    event.preventDefault();
    serviceBtn.text("Concierge Cybersecurity");
    oi.prop("checked", false);
    ci.prop("checked", false);
    vr.prop("checked", false);
    hr.prop("checked", false);
    dr.prop("checked", false);
    textBox.hide();
    linkBox.hide();
    deviceSecVr.hide();
    deviceSecCcs.show();
    mediaSec.show();
    cloudSec.show();
    emailSec.show();
    paymentSec.show();
    wifiSec.show();
    ciDrop.slideUp();
    irDrop.slideUp();
    serviceDrop.slideUp();
  });

  ciBtn.click(function (event) {
    event.preventDefault();
    ciDrop.slideToggle();
    irDrop.slideUp();
    // textBox.hide();
    // linkBox.hide();
    // deviceSecCcs.hide();
    // deviceSecVr.hide();
    // mediaSec.hide();
    // cloudSec.hide();
    // emailSec.hide();
    // paymentSec.hide();
    // wifiSec.hide();
    deviceDropCcs.slideUp();
    deviceDropVr.slideUp();
    mobileDropCcs.slideUp();
    mobileDropVr.slideUp();
    pcDropCcs.slideUp();
    pcDropVr.slideUp();
    socialDrop.slideUp();
    emailDrop.slideUp();
    paymentDrop.slideUp();
    cloudDrop.slideUp();
    vr.prop("checked", false);
    hr.prop("checked", false);
    dr.prop("checked", false);
  });
  oi.click(function () {
    if ($(this).prop("checked") == true) {
      serviceBtn.text("Opensource Intelligence");
      textBox.show();
      linkBox.hide();
      deviceSecCcs.hide();
      deviceSecVr.hide();
      mediaSec.hide();
      cloudSec.hide();
      emailSec.hide();
      paymentSec.hide();
      wifiSec.hide();
      ci.prop("checked", false);
      vr.prop("checked", false);
      hr.prop("checked", false);
      dr.prop("checked", false);
      ciDrop.slideUp();
      serviceDrop.slideUp();
    } else if ($(this).prop("checked") == false) {
      textBox.hide();
      serviceBtn.text("Select the Service");
    }
  });
  ci.click(function () {
    if ($(this).prop("checked") == true) {
      serviceBtn.text("Crime Investigation");
      textBox.show();
      linkBox.hide();
      deviceSecCcs.hide();
      deviceSecVr.hide();
      mediaSec.hide();
      cloudSec.hide();
      emailSec.hide();
      paymentSec.hide();
      wifiSec.hide();
      oi.prop("checked", false);
      vr.prop("checked", false);
      hr.prop("checked", false);
      dr.prop("checked", false);
      ciDrop.slideUp();
      serviceDrop.slideUp();
    } else if ($(this).prop("checked") == false) {
      textBox.hide();
      serviceBtn.text("Select the Service");
    }
  });
  irBtn.click(function (event) {
    event.preventDefault();
    irDrop.slideToggle();
    ciDrop.slideUp();
    // textBox.hide();
    // linkBox.hide();
    // deviceSecCcs.hide();
    // deviceSecVr.hide();
    // mediaSec.hide();
    // cloudSec.hide();
    // emailSec.hide();
    // paymentSec.hide();
    // wifiSec.hide();
    deviceDropCcs.slideUp();
    deviceDropVr.slideUp();
    mobileDropCcs.slideUp();
    mobileDropVr.slideUp();
    pcDropCcs.slideUp();
    pcDropVr.slideUp();
    socialDrop.slideUp();
    emailDrop.slideUp();
    paymentDrop.slideUp();
    cloudDrop.slideUp();
    oi.prop("checked", false);
    ci.prop("checked", false);
  });
  vr.click(function () {
    if ($(this).prop("checked") == true) {
      serviceBtn.text("Virus Removal");
      hr.prop("checked", false);
      dr.prop("checked", false);
      oi.prop("checked", false);
      ci.prop("checked", false);
      textBox.hide();
      linkBox.hide();
      deviceSecVr.show();
      deviceSecCcs.hide();
      mediaSec.hide();
      cloudSec.hide();
      emailSec.hide();
      paymentSec.hide();
      wifiSec.hide();
      irDrop.slideUp();
      serviceDrop.slideUp();
    } else if ($(this).prop("checked") == false) {
      deviceSecVr.hide();
      serviceBtn.text("Select the Service");
    }
  });
  hr.click(function () {
    if ($(this).prop("checked") == true) {
      serviceBtn.text("Hack Recovery");
      dr.prop("checked", false);
      vr.prop("checked", false);
      oi.prop("checked", false);
      ci.prop("checked", false);
      textBox.hide();
      linkBox.hide();
      deviceSecVr.hide();
      deviceSecCcs.show();
      mediaSec.show();
      cloudSec.show();
      emailSec.show();
      paymentSec.show();
      wifiSec.show();
      irDrop.slideUp();
      serviceDrop.slideUp();
    } else if ($(this).prop("checked") == false) {
      deviceSecCcs.hide();
      mediaSec.hide();
      cloudSec.hide();
      emailSec.hide();
      paymentSec.hide();
      wifiSec.hide();
      serviceBtn.text("Select the Service");
    }
  });
  dr.click(function () {
    if ($(this).prop("checked") == true) {
      serviceBtn.text("Data Removal");
      hr.prop("checked", false);
      vr.prop("checked", false);
      oi.prop("checked", false);
      ci.prop("checked", false);
      linkBox.show();
      textBox.show();
      deviceSecCcs.hide();
      deviceSecVr.hide();
      mediaSec.hide();
      cloudSec.hide();
      emailSec.hide();
      paymentSec.hide();
      wifiSec.hide();
      irDrop.slideUp();
      serviceDrop.slideUp();
    } else if ($(this).prop("checked") == false) {
      linkBox.hide();
      textBox.hide();
      serviceBtn.text("Select the Service");
    }
  });
  //Social Section
  socialBtn.click(function (event) {
    event.preventDefault();
    socialDrop.slideToggle();
    paymentDrop.slideUp();
    deviceDropCcs.slideUp();
    emailDrop.slideUp();
    cloudDrop.slideUp();
    ciDrop.slideUp();
    irDrop.slideUp();
    serviceDrop.slideUp();
  });
  facebook.click(function () {
    if ($(this).prop("checked") == true) {
      fbInput.show();
    } else if ($(this).prop("checked") == false) {
      fbInput.hide();
      fbInput.val(0);
    }
  });
  twitter.click(function () {
    if ($(this).prop("checked") == true) {
      twitterInput.show();
    } else if ($(this).prop("checked") == false) {
      twitterInput.hide();
      twitterInput.val(0);
    }
  });
  insta.click(function () {
    if ($(this).prop("checked") == true) {
      instaInput.show();
    } else if ($(this).prop("checked") == false) {
      instaInput.hide();
      instaInput.val(0);
    }
  });
  link.click(function () {
    if ($(this).prop("checked") == true) {
      linkInput.show();
    } else if ($(this).prop("checked") == false) {
      linkInput.hide();
      linkInput.val(0);
    }
  });
  pint.click(function () {
    if ($(this).prop("checked") == true) {
      pintInput.show();
    } else if ($(this).prop("checked") == false) {
      pintInput.hide();
      pintInput.val(0);
    }
  });
  youtube.click(function () {
    if ($(this).prop("checked") == true) {
      youtubeInput.show();
    } else if ($(this).prop("checked") == false) {
      youtubeInput.hide();
      youtubeInput.val(0);
    }
  });
  snap.click(function () {
    if ($(this).prop("checked") == true) {
      snapInput.show();
    } else if ($(this).prop("checked") == false) {
      snapInput.hide();
      snapInput.val(0);
    }
  });
  whats.click(function () {
    if ($(this).prop("checked") == true) {
      whatsInput.show();
    } else if ($(this).prop("checked") == false) {
      whatsInput.hide();
      whatsInput.val(0);
    }
  });

  //Payment Section
  paymentBtn.click(function (event) {
    event.preventDefault();
    paymentDrop.slideToggle();
    socialDrop.slideUp();
    deviceDropCcs.slideUp();
    emailDrop.slideUp();
    cloudDrop.slideUp();
    ciDrop.slideUp();
    irDrop.slideUp();
    serviceDrop.slideUp();
  });
  paypal.click(function () {
    if ($(this).prop("checked") == true) {
      paypalInput.show();
    } else if ($(this).prop("checked") == false) {
      paypalInput.hide();
      paypalInput.val(0);
    }
  });
  skrill.click(function () {
    if ($(this).prop("checked") == true) {
      skrillInput.show();
    } else if ($(this).prop("checked") == false) {
      skrillInput.hide();
      skrillInput.val(0);
    }
  });
  visa.click(function () {
    if ($(this).prop("checked") == true) {
      visaInput.show();
    } else if ($(this).prop("checked") == false) {
      visaInput.hide();
      visaInput.val(0);
    }
  });
  bank.click(function () {
    if ($(this).prop("checked") == true) {
      bankInput.show();
    } else if ($(this).prop("checked") == false) {
      bankInput.hide();
      bankInput.val(0);
    }
  });

  //Email Section
  emailBtn.click(function (event) {
    event.preventDefault();
    emailDrop.slideToggle();
    socialDrop.slideUp();
    paymentDrop.slideUp();
    deviceDropCcs.slideUp();
    cloudDrop.slideUp();
    ciDrop.slideUp();
    irDrop.slideUp();
    serviceDrop.slideUp();
  });
  yahoo.click(function () {
    if ($(this).prop("checked") == true) {
      yahooInput.show();
    } else if ($(this).prop("checked") == false) {
      yahooInput.hide();
      yahooInput.val(0);
    }
  });
  hotmail.click(function () {
    if ($(this).prop("checked") == true) {
      hotmailInput.show();
    } else if ($(this).prop("checked") == false) {
      hotmailInput.hide();
      hotmailInput.val(0);
    }
  });
  gmail.click(function () {
    if ($(this).prop("checked") == true) {
      gmailInput.show();
    } else if ($(this).prop("checked") == false) {
      gmailInput.hide();
      gmailInput.val(0);
    }
  });
  outlook.click(function () {
    if ($(this).prop("checked") == true) {
      outlookInput.show();
    } else if ($(this).prop("checked") == false) {
      outlookInput.hide();
      outlookInput.val(0);
    }
  });
  customMail.click(function () {
    if ($(this).prop("checked") == true) {
      customMailInput.show();
    } else if ($(this).prop("checked") == false) {
      customMailInput.hide();
      customMailInput.val(0);
    }
  });

  // Device Section
  deviceBtnCcs.click(function (event) {
    event.preventDefault();
    deviceDropCcs.slideToggle();
    socialDrop.slideUp();
    paymentDrop.slideUp();
    emailDrop.slideUp();
    cloudDrop.slideUp();
    ciDrop.slideUp();
    irDrop.slideUp();
    serviceDrop.slideUp();
  });
  mobileBtnCcs.click(function (event) {
    event.preventDefault();
    mobileDropCcs.slideToggle();
    pcDropCcs.slideUp();
    stvInputCcs.hide();
  });
  androidCcs.click(function () {
    if ($(this).prop("checked") == true) {
      androidInputCcs.show();
    } else if ($(this).prop("checked") == false) {
      androidInputCcs.hide();
      androidInputCcs.val(0);
    }
  });
  iosCcs.click(function () {
    if ($(this).prop("checked") == true) {
      iosInputCcs.show();
    } else if ($(this).prop("checked") == false) {
      iosInputCcs.hide();
      iosInputCcs.val(0);
    }
  });
  pcBtnCcs.click(function (event) {
    event.preventDefault();
    pcDropCcs.slideToggle();
    mobileDropCcs.slideUp();
    stvInputCcs.hide();
  });
  windowsCcs.click(function () {
    if ($(this).prop("checked") == true) {
      windowsInputCcs.show();
    } else if ($(this).prop("checked") == false) {
      windowsInputCcs.hide();
      windowsInputCcs.val(0);
    }
  });
  linuxCcs.click(function () {
    if ($(this).prop("checked") == true) {
      linuxInputCcs.show();
    } else if ($(this).prop("checked") == false) {
      linuxInputCcs.hide();
      linuxInputCcs.val(0);
    }
  });
  macCcs.click(function () {
    if ($(this).prop("checked") == true) {
      macInputCcs.show();
    } else if ($(this).prop("checked") == false) {
      macInputCcs.hide();
      macInputCcs.val(0);
    }
  });
  stvBtnCcs.click(function (event) {
    event.preventDefault();
    stvInputCcs.toggle();
    mobileDropCcs.slideUp();
    pcDropCcs.slideUp();
  });
  //VR Device
  deviceBtnVr.click(function (event) {
    event.preventDefault();
    deviceDropVr.slideToggle();
    ciDrop.slideUp();
    irDrop.slideUp();
    serviceDrop.slideUp();
  });
  mobileBtnVr.click(function (event) {
    event.preventDefault();
    mobileDropVr.slideToggle();
    pcDropVr.slideUp();
    stvInputVr.hide();
  });
  androidVr.click(function () {
    if ($(this).prop("checked") == true) {
      androidInputVr.show();
    } else if ($(this).prop("checked") == false) {
      androidInputVr.hide();
      androidInputVr.val(0);
    }
  });
  iosVr.click(function () {
    if ($(this).prop("checked") == true) {
      iosInputVr.show();
    } else if ($(this).prop("checked") == false) {
      iosInputVr.hide();
      iosInputVr.val(0);
    }
  });
  pcBtnVr.click(function (event) {
    event.preventDefault();
    pcDropVr.slideToggle();
    mobileDropVr.slideUp();
    stvInputVr.hide();
  });
  windowsVr.click(function () {
    if ($(this).prop("checked") == true) {
      windowsInputVr.show();
    } else if ($(this).prop("checked") == false) {
      windowsInputVr.hide();
      windowsInputVr.val(0);
    }
  });
  linuxVr.click(function () {
    if ($(this).prop("checked") == true) {
      linuxInputVr.show();
    } else if ($(this).prop("checked") == false) {
      linuxInputVr.hide();
      linuxInputVr.val(0);
    }
  });
  macVr.click(function () {
    if ($(this).prop("checked") == true) {
      macInputVr.show();
    } else if ($(this).prop("checked") == false) {
      macInputVr.hide();
      macInputVr.val(0);
    }
  });
  stvBtnVr.click(function (event) {
    event.preventDefault();
    stvInputVr.toggle();
    mobileDropVr.slideUp();
    pcDropVr.slideUp();
  });
  //Cloud Section
  cloudBtn.click(function (event) {
    event.preventDefault();
    cloudDrop.slideToggle();
    deviceDropCcs.slideUp();
    socialDrop.slideUp();
    paymentDrop.slideUp();
    emailDrop.slideUp();
    ciDrop.slideUp();
    irDrop.slideUp();
    serviceDrop.slideUp();
  });
  icloud.click(function () {
    if ($(this).prop("checked") == true) {
      icloudInput.show();
    } else if ($(this).prop("checked") == false) {
      icloudInput.hide();
      icloudInput.val(0);
    }
  });
  gcloud.click(function () {
    if ($(this).prop("checked") == true) {
      gcloudInput.show();
    } else if ($(this).prop("checked") == false) {
      gcloudInput.hide();
      gcloudInput.val(0);
    }
  });
  dropbox.click(function () {
    if ($(this).prop("checked") == true) {
      dropboxInput.show();
    } else if ($(this).prop("checked") == false) {
      dropboxInput.hide();
      dropboxInput.val(0);
    }
  });
  googleDrive.click(function () {
    if ($(this).prop("checked") == true) {
      googleDriveInput.show();
    } else if ($(this).prop("checked") == false) {
      googleDriveInput.hide();
      googleDriveInput.val(0);
    }
  });
});
