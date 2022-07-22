const circle1 = document.querySelectorAll(".circle1");
const circle5 = document.querySelectorAll(".circle5");
for (let i = 0; i < circle1.length; i++) {
  circle1[i].style.animationDelay = i + "s";
}
for (let i = 0; i < circle5.length; i++) {
  circle5[i].style.animationDelay = i + "s";
}
const circle3 = document.querySelectorAll(".circle3");
for (let i = 0; i < circle3.length; i++) {
  circle3[i].style.animationDelay = i + "s";
}