const serviceSlider = document.querySelectorAll(".happy-slider");
function serviceChange() {
  const services = document.getElementById("services");
  serviceSlider[services.selectedIndex].style.display = "block";
  for (let i = 0; i < serviceSlider.length; i++) {
    if (i != services.selectedIndex) {
      serviceSlider[i].style.display = "none";
    }
  }
}
