function setUpSlider(){
    sliders = document.querySelectorAll('.slider');
    sliders.forEach(slider => {
        slider.addEventListener("input", function(){
            const value = slider.closest('.slider-container').querySelector('.slider-value');
            value.value = slider.value;
        });
    });

    vals = document.querySelectorAll('.slider-value');
    vals.forEach(val => {
        val.addEventListener('input', function(){
            const slider = val.closest('.slider-container').querySelector('.slider');
            slider.value = val.value;
        });
    });
}

setUpSlider();