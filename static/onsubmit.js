function checkOptionValues(Question){
    const values = Question.querySelectorAll('.slider-value');
    let sum = 0;
    values.forEach(value => {
        sum+= parseInt(value.value, 10);
    });


    if (sum !== 100){
        console.log(sum)
        console.log('false');
        return false;
    }
    else{
        console.log('true');
        return true;
    }
}

function alertContainer(question){
    question.scrollIntoView({ behavior: 'smooth', block: 'center' });
    
    question.classList.add('alert-border');
    setTimeout(function(){
        question.classList.remove('alert-border');
        }, 2000);
}


function generate(){
    const containers = document.querySelectorAll(".question-container");
    containers.forEach(container => {
        if (container.querySelector('#question-type').value === "MCQ"  &&  container.querySelector('#selection').value === "Custom"){
            if (!checkOptionValues(container)){
                alertContainer(container);
                alert("Values must add up to a Hundred")
            }
        }
    });
}