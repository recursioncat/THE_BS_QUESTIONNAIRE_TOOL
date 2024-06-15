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

function checkOptionTicked(question){
    const boxes = question.querySelectorAll('.check');
    for (let i = 0; i < boxes.length; i++) {
        if(boxes[i].checked){
            return true;
        }
    }
    return false;
}

function checkInputs(){
    let flag = 0;
    const inputs = document.querySelectorAll('textarea:not([readonly])');
    console.log(inputs[0])
    for (let i = 0; i < inputs.length; i++){
        if (inputs[i].value === ""){
            flag = 1;
            break;
        }
    }

    if(flag !== 0){
        return false;
    }

    else{
        return true;
    }
    
}


function generate(){
    const containers = document.querySelectorAll(".question-container");
    for (let i = 0; i < containers.length; i++) {
        const container = containers[i];
        
        if (container.querySelector('#question-type').value === "MCQ" && container.querySelector('#selection').value === "Custom") {
            if (!checkOptionValues(container)) {
                alertContainer(container);
                alert("Values must add up to a Hundred");
                return;
            }
        } 
            
        else if (container.querySelector('#question-type').value === "MCQ" && container.querySelector('#selection').value === "Perticular") {
            if (!checkOptionTicked(container)) {
                alertContainer(container);
                alert("Please Tick One box for the answer");
                return;
            }
        }

    }
        
    if (!checkInputs()){
        alert("All Questions and Answers must have value");
        return;
    }

    generateJSON();
}


function generateJSON(){
    // Layer 1 : Whole Questionnaire
    const mainForm = document.querySelector('main');
    const copies = document.getElementById('copies').value;
    const title = mainForm.querySelector('.h1').value;
    const detail = mainForm.querySelector('.additional').textContent;

    // Layer 2 : Questions
    const questions = document.querySelectorAll('.question-container');
    let listOfQuestions = []
    questions.forEach( question => {
        const questionText = question.querySelector('.question').value;
        const questionType = question.querySelector('#question-type').value;
        const algoType = question.querySelector('#selection').value;

        // Layer 3 : Options
        let optionList = []
        const options =  question.querySelectorAll(".option-container");
        options.forEach( option => {
            const check = option.querySelector('.check').checked;
            const optionText = option.querySelector('.option-text').value;
            const value = Number(option.querySelector('.slider-value').value)/100;

            const optionDetail = {
                check: check,
                text: optionText,
                value: value
            }
            optionList.push(optionDetail);
        } );

        const questionDetail = {
            text: questionText,
            type: questionType,
            algo: algoType,
            optionList: optionList
        }

        listOfQuestions.push(questionDetail);

    });

    const completeJSON = {
        amount : copies,
        title: title,
        detail: detail,
        questions: listOfQuestions
    }

    console.log(JSON.stringify(completeJSON, null, 2));

    // Create a form and submit it to /process
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '/process-questionnaire';

    const input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'data';
    input.value = JSON.stringify(completeJSON);

    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
}