let current = 0;
const slides = document.querySelectorAll('.active')

setInterval(()=>{
    slides[current].classList.remove('sctive');
    current = (current + 1) % slides.length;
    slides[current].classList.add('active');
},3000);