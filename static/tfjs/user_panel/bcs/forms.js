 allServices = document.querySelectorAll('form .sub-services .form-check');

 allServicesFromContainer = document.querySelector('form .information-form');

 allServicesInputFrom =
     document.querySelectorAll('form .information-form .info-type');

 allServices.forEach((check, index) => {
     check.addEventListener('click', e => {
         allServicesFromContainer.classList.remove('d-none');
         console.log(e);
         if (check.children[0].checked)
             allServicesInputFrom[index].classList.remove('d-none');
         else
             allServicesInputFrom[index].classList.add('d-none');
     })
 });