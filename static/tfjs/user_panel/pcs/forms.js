 allServices = document.querySelectorAll('form .sub-services .form-check');

 allServicesFormContainer = document.querySelector('form .information-form');

 allServicesInputForm =
     document.querySelectorAll('form .information-form .info-type');

 allServices.forEach((check, index) => {
     check.addEventListener('click', e => {
         allServicesFormContainer.classList.remove('d-none');
         if (allServicesInputForm.length == 0) {
             //do something later
         } else if (check.children[0].checked)
             allServicesInputForm[index].classList.remove('d-none');
         else
             allServicesInputForm[index].classList.add('d-none');
     })
 });

 // for hack recovery

 quesDiv = document.querySelectorAll(".ques");
 quesTitle = document.querySelectorAll(".ques-title");
 acTypeDiv = document.querySelectorAll(".account-type");
 selectedAc = document.querySelectorAll(".selected-account");
 mainInput = document.querySelectorAll(".main-input");
 quesAccount = document.querySelectorAll(".account-ques");
 quesInput = document.querySelectorAll(".ques-input");
 quesCategory = document.querySelectorAll(".ques-category");
 mainQuesCategory = document.querySelectorAll(".main-ques-category");
 initSelect = document.querySelectorAll(".init-select");
 finalQues = document.querySelectorAll(".final-ques");



 quesTitle.forEach((element, index) => {
     element.addEventListener("click", function() {
         if (acTypeDiv[index].style.maxHeight) {
             divHide(index);
         } else {
             divShow(index);
         }
     });
 });

 acTypeDiv.forEach((element, index) => {
     let i = index;
     element.childNodes.forEach((data) => {
         data.addEventListener("click", function() {
             let value = data.children[0].value;
             selectedAc[i].innerText = value;
             divHide(i);
         });
     });
 });

 mainInput.forEach((element, index) => {
     element.addEventListener("click", function() {
         for (let j = 0; j < quesAccount.length; j++) {
             quesAccount[index].style.display = "block";
             mainQuesCategory[index].style.display = "block";
             quesInput[j].children[0].checked = false;
             quesCategory[j].style.display = "none";
             initSelect[j].innerText = "";
             if (j != index) {
                 quesAccount[j].style.display = "none";
                 mainQuesCategory[j].style.display = "none";
             }
         }
         for (let m = 0; m < finalQues.length; m++) {
             finalQues[m].checked = false;
         }
     });
 });

 quesInput.forEach((element, index) => {
     element.addEventListener("click", function() {
         for (let k = 0; k < quesInput.length; k++) {
             quesCategory[index].style.display = "block";
             if (k != index) {
                 quesCategory[k].style.display = "none";
             }
         }
     });
 });

 // form script 


 g_form = document.querySelector(".g-form");
 selected_account = document.getElementById("account-type");
 account_name = document.querySelectorAll(".init-select");
 final_ques = document.querySelectorAll(".final-ques");
 general_ques = document.querySelectorAll(".general-ques");
 general_ques_title = document.querySelectorAll(".general-ques-title");
 more_account = document.querySelector(".more-account");
 account_close = document.querySelectorAll(".account-close");
 errorTxt = document.getElementById("small-error");

 for (let i = 0; i < general_ques.length; i++) {
     general_ques[i].value = "...";
 }