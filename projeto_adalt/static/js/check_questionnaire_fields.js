function check_questionnaire_fields() {

    var numOfQuestions = 10;
    var rest = 0;

    var q1 = document.forms['quiz']['questao1'].value;
    var q2 = document.forms['quiz']['questao2'].value;
    var q3 = document.forms['quiz']['questao3'].value;
    var q4 = document.forms['quiz']['questao4'].value;
    var q5 = document.forms['quiz']['questao5'].value;
    var q6 = document.forms['quiz']['questao6'].value;
    var q7 = document.forms['quiz']['questao7'].value;
    var q8 = document.forms['quiz']['questao8'].value;
    var q9 = document.forms['quiz']['questao9'].value;
    var q10 = document.forms['quiz']['questao10'].value;

    for (var i = 1; i <= numOfQuestions; i++) {
        if (eval('q' + i)) {
            alert("Você não respondeu a questão " + i);
            rest = 1;
        }
    }
    return false;

}
